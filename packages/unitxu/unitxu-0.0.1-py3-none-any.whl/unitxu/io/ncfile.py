#!/usr/bin/env python
# coding=utf-8

"""
@author: xu
@license: MIT
@file: ncfile.py
@date: 2023/10/23 22:33
@desc: 
"""

import time
import traceback

import numpy as np
from numpy.ma import MaskedArray
import netCDF4 as nc
from datetime import datetime, timedelta
# from osgeo import gdal, osr
# from loguru import logger
import os
from ..draw import array2png
# 单个nc数据ndvi数据读取为多个tif文件，并将ndvi值化为-1-1之间
# from grid.read_grib import read_gridfile


class NCformat:
    """定义netcdf文件格式，通过set_dim函数确定nc文件中关键维度的名字，如果文件中没有该维度可以不设置；通过set_target设置nc文件中
    物理量名字和数据库中的映射，如果不设置即数据库字段名和文件一样，并且全量数据导入数据库"""
    def __init__(self):
        """
        grid_map_type 设置投影类型，默认为等经纬的，1--等经纬  2--兰伯特（此时需要设置standard_parallel_1 ，standard_parallel_2，
        latitude_of_origin， longitude_of_central_meridian这四个变量）
        """
        self.set_dim()
        self.set_target()
        self.standard_parallel_1 = 35
        self.standard_parallel_2 = 35
        self.latitude_of_origin = 35
        self.longitude_of_central_meridian = 105
        self.grid_map_type = 1


    def set_dim(self, timename=None, levelname=None, xname=None, yname=None):
        self.timename = ['time', 'times', 't', timename]
        self.levelname = ['level', 'hght', 'height', 'znu', 'znw', 'zs', 'bottom_top', 'soil_layers_stag',
                          'bottom_top_stag', levelname]
        self.xname = ['x', 'xlon', 'xlons', 'lon', 'lons', 'xlong', 'longitude', 'xlong_u', 'xlong_v', 'west_east_stag',
                      'west_east', xname]
        self.yname = ['y', 'xlat', 'xlats', 'lat', 'lats', 'latitude', 'xlat_u', 'xlat_v', 'south_north',
                      'south_north_stag', yname]

    def set_target(self, **kwargs):
        self.target_dict = kwargs


class NC2Tiff:
    """
    将nc数据转换成tiff，需要通过NCformat类里的方法set_dim设置维度名字用以区分各维度信息，通过set_target设置需要解析的变量，默认全部；
    resolve_target处理解析方法 对设置的要素转换为tiff文件
    """
    def __init__(self, ncfile, output_folder, qibaotime=None, ncformat=None):
        if ncformat is None:
            self.ncformat = NCformat()
        else:
            self.ncformat = ncformat
        self.output_folder = output_folder
        self.ncfile = ncfile
        self.qibaotime = '' if qibaotime is None else qibaotime
        self.pro_map = None
        self.dset = nc.Dataset(self.ncfile)


    def show_nc(self, targets=None):
        if targets is None:
            for i in self.dset.variables.keys():
                print(i, self.dset.variables[i].shape)
        else:
            if isinstance(targets, str) and targets in self.dset.variables.keys():
                print(targets, self.dset.variables[targets].shape)
            elif isinstance(targets, list):
                for target in targets:
                    print(target, self.dset.variables[target].shape)



    def get_tiff(self, target, dims):
        dims_format = []
        for d in dims:
            if isinstance(d, str):
                temp = d.replace(' ', '').replace('-', '').replace(':', '')
                dims_format.append({temp: temp}.get(temp, '999'))
            else:
                dims_format.append(str(round(d, 4)).replace('.', 'p'))
        output = os.path.join(self.output_folder, os.sep.join(dims_format))
        if not os.path.exists(output):
            os.makedirs(output)
        tiff = os.path.join(output, target + '.Tiff')
        return tiff

    def get_metadata(self, **kwargs):
        metadata = {
            'target': '', 'unit': '', 'level': '0', 'qibaotime': '',
            'yubaotime': ''
        }
        for k, v in kwargs.items():
            metadata[k] = v
        return metadata


    def get_dimtar2datatar(self, dimtar=None, dimtar_lat=None):
        dimtar_lower = dimtar.lower()
        tars = []
        # todo: 判断dimtar为时间，计算时间的变量名
        if dimtar_lower in self.ncformat.timename:
            for tar in self.targets:
                if tar.lower() in self.ncformat.timename:
                    tars.append(tar)
            if len(tars) > 1:
                for tar in tars:
                    if dimtar in self.dset.variables[tar].dimensions:
                        inde = self.dset.variables[tar].dimensions.index(dimtar)
                        if self.dset.variables[tar].shape[inde] == self.dset.dimensions[dimtar].size:
                            return tar
            elif len(tars) > 1:
                return tars[0]
        # todo: 判断dimtar为高度，计算高度的变量名
        if dimtar_lower in self.ncformat.levelname:
            for l in self.targets:
                if l.lower() in self.ncformat.levelname:
                    tars.append(l)
            if len(tars) == 1:
                return tars[0]
            else:
                for l in tars:
                    if self.dset.dimensions[dimtar].size == self.dset.variables[l].size:
                        return l
        # todo: 判断dimtar为经度，计算经度的变量名
        if dimtar_lower in self.ncformat.xname:
            for lon in self.targets:
                if lon.lower() in self.ncformat.xname:
                    tars.append(lon)
            if len(tars) > 1:
                for tar in tars:
                    tar_dim_num = len(self.dset.variables[tar][:].squeeze().shape)
                    if tar_dim_num>1 and dimtar in self.dset.variables[tar].dimensions and dimtar_lat in self.dset.variables[tar].dimensions:
                        inde = self.dset.variables[tar].dimensions.index(dimtar)
                        inde_lat = self.dset.variables[tar].dimensions.index(dimtar_lat)
                        if self.dset.variables[tar].shape[inde] == self.dset.dimensions[dimtar].size and\
                            self.dset.variables[tar].shape[inde_lat] == self.dset.dimensions[dimtar_lat].size:
                            return tar
                    elif tar_dim_num==1 and dimtar in self.dset.variables[tar].dimensions:
                        inde = self.dset.variables[tar].dimensions.index(dimtar)
                        if self.dset.variables[tar].shape[inde] == self.dset.dimensions[dimtar].size:
                            return tar
            elif len(tars) == 1:
                return tars[0]
        # todo: 判断dimtar为纬度，计算纬度的变量名
        if dimtar_lower in self.ncformat.yname:
            for lat in self.targets:
                if lat.lower() in self.ncformat.yname:
                    tars.append(lat)
            if len(tars) > 1:
                for tar in tars:
                    tar_dim_num = len(self.dset.variables[tar][:].squeeze().shape)
                    if tar_dim_num>1 and dimtar in self.dset.variables[tar].dimensions and dimtar_lat in self.dset.variables[tar].dimensions:
                        inde = self.dset.variables[tar].dimensions.index(dimtar)
                        inde_lat = self.dset.variables[tar].dimensions.index(dimtar_lat)
                        if self.dset.variables[tar].shape[inde] == self.dset.dimensions[dimtar].size and \
                            self.dset.variables[tar].shape[inde_lat] == self.dset.dimensions[dimtar_lat].size:
                            return tar
                    elif tar_dim_num==1 and dimtar in self.dset.variables[tar].dimensions:
                        inde = self.dset.variables[tar].dimensions.index(dimtar)
                        inde_lat = self.dset.variables[tar].dimensions.index(dimtar_lat)
                        if self.dset.variables[tar].shape[inde] == self.dset.dimensions[dimtar].size:
                            return tar
            elif len(tars) > 1:
                return tars[0]
        return dimtar

    def ns2s(self, ts):
        if isinstance(ts, float):
            dt = (datetime.now() + timedelta(days=365)).timestamp()
            while ts > dt:
                ts = ts / 1000
        else:
            ts = ''.join([i.decode() for i in ts[:].squeeze()])
            ts_obj = datetime.strptime(ts, '%Y-%m-%d_%H:%M:%S')
            ts = ts_obj.timestamp()
        return ts

    def getSRSPair(self, dataset=None):
        # return 投影坐标系 地理坐标系
        prosrs = osr.SpatialReference()
        if dataset is not None and dataset.GetProjection():
            self.pro_map = dataset.GetProjection()
            prosrs.ImportFromWkt(dataset.GetProjection())
        else:
            pro = 'PROJCS["unnamed",GEOGCS["Coordinate System imported from GRIB file",' \
                  'DATUM["unknown",SPHEROID["Sphere",6371393,0]],PRIMEM["Greenwich",0],' \
                  'UNIT["degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic_2SP"],' \
                  'PARAMETER["standard_parallel_1",%f],PARAMETER["standard_parallel_2",%f],' \
                  'PARAMETER["latitude_of_origin",%f],PARAMETER["central_meridian",%f],' \
                  'PARAMETER["false_easting",0],PARAMETER["false_northing",0]]' % (
                self.ncformat.standard_parallel_1, self.ncformat.standard_parallel_2, self.ncformat.latitude_of_origin,
                self.ncformat.longitude_of_central_meridian
            )
            self.pro_map = pro
            prosrs.ImportFromWkt(pro)
        geosrs = prosrs.CloneGeogCS()
        return prosrs, geosrs


    def lonlat_to_xy(self, lon, lat):
        '''
        经纬度坐标转换为投影坐标
        :param gcs:地理空间坐标信息，可由get_file_info()函数获取
        :param pcs:投影坐标信息，可由get_file_info()函数获取
        :param lon:经度坐标
        :param lat:纬度坐标
        :return:地理空间坐标对应的投影坐标
        '''
        #
        prosrs, geosrs = self.getSRSPair()
        ct = osr.CoordinateTransformation(geosrs, prosrs)
        # print(lon, lat, 'lon, lat', type(lat), type(lon))
        coordinates = ct.TransformPoint(float(lon), float(lat))
        return coordinates[0], coordinates[1]


    def get_equidistant_box(self, lons, lats, units):
        # data_shape = self.lons.squeeze().shape
        # 数据为兰伯特的，存的是经纬度，转成距离
        lonmax, lonmin = lons.max(), lons.min()
        latmax, latmin = lats.max(), lats.min()
        if self.ncformat.grid_map_type == 2 and ('degree' in units.lower() or lons.max() < 360):
            lons = lons.squeeze()
            lats = lats.squeeze()
            lon_1line_min, lon_1line_max = lons[0].min(), lons.max()
            lon_nline_min, lon_nline_max = lons[-1].min(), lons.max()
            lon_left_down, lon_right_up = max(lon_1line_min, lon_nline_min), max(lon_1line_max, lon_nline_max)
            lat_left_down, lat_right_up = min(lats[:, 0]), max(lats[:, 0])
            left_down = self.lonlat_to_xy(lon_left_down, lat_left_down)
            right_up = self.lonlat_to_xy(lon_right_up, lat_right_up)
            return [left_down[1], right_up[1], left_down[0], right_up[1]]
        # 数据为等经纬的，存的是距离的坐标
        elif self.ncformat.grid_map_type == 2 and ('m' in units.lower() or lons.max() > 360):
            pro = 'PROJCS["unnamed",GEOGCS["Coordinate System imported from GRIB file",' \
                  'DATUM["unknown",SPHEROID["Sphere",6371393,0]],PRIMEM["Greenwich",0],' \
                  'UNIT["degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic_2SP"],' \
                  'PARAMETER["standard_parallel_1",%f],PARAMETER["standard_parallel_2",%f],' \
                  'PARAMETER["latitude_of_origin",%f],PARAMETER["central_meridian",%f],' \
                  'PARAMETER["false_easting",0],PARAMETER["false_northing",0]]' % (
                      self.ncformat.standard_parallel_1, self.ncformat.standard_parallel_2,
                      self.ncformat.latitude_of_origin,
                      self.ncformat.longitude_of_central_meridian
                  )
            self.pro_map = pro
            return [latmin, latmax, lonmin, lonmax]
        else:
            return [latmin, latmax, lonmin, lonmax]

    def getdata(self, data):
        lons = self.lons.flatten()
        lats = self.lats.flatten()
        if lats[0] < lats[-1]:
            data = data[::-1]
        if lons[0]>lons[-1]:
            data = data[:, ::-1]
        return data


    def resolve_target(self):
        """
        解析nc文件里指定变量或者全部变量，如果变量为二维即只有经纬度维度，如果变量为三维即预报时次（浮点数）、经纬度或者高度、经纬度，
        如果变量为四维即数据为预报时次（浮点数）、高度、经纬度，将数据拆成一个个tiff文件, 不支持坐标分辨率变化的格点数据
        :return:
        """
        self.out_tiffs = []
        self.targets = self.dset.variables.keys()
        for target in self.targets:
            if target in self.ncformat.target_dict or not self.ncformat.target_dict:
                # todo:满足条件的变量解析入库
                data_obj = self.dset.variables[target]
                data_dim_tar = data_obj.dimensions
                # coordinates = [] if 'coordinates' not in dir(data_obj) else data_obj.coordinates.split()
                data_dim = len(data_obj[:].shape)
                unit = '' if 'unit' not in dir(data_obj) else data_obj.unit
                unit = data_obj.units if 'units' in dir(data_obj) else unit
                if data_dim < 2 or self.get_dimtar2datatar(data_dim_tar[-2], data_dim_tar[-1]) not in self.dset.variables.keys() \
                        or self.get_dimtar2datatar(data_dim_tar[-1], data_dim_tar[-2]) not in self.dset.variables.keys():
                    continue
                try:
                    self.lats = self.dset.variables[self.get_dimtar2datatar(data_dim_tar[-2], data_dim_tar[-1])][:]
                    self.lons = self.dset.variables[self.get_dimtar2datatar(data_dim_tar[-1], data_dim_tar[-2])][:]
                    latlon_units_obj = self.dset.variables[self.get_dimtar2datatar(data_dim_tar[-1], data_dim_tar[-2])]
                    latlon_units = '' if 'unit' not in dir(latlon_units_obj) else latlon_units_obj.unit
                    latlon_units = latlon_units_obj.units if 'units' in dir(latlon_units_obj) else latlon_units
                    if data_dim == 2 and (data_dim_tar[1].lower() in self.ncformat.xname or data_dim_tar[1] in self.ncformat.yname):
                        latlons = self.get_equidistant_box(self.lons, self.lats, latlon_units)
                        tiff = self.get_tiff(target, [self.qibaotime, '999'])
                        self.array2draw(latlons, self.getdata(data_obj[:]), tiff, self.get_metadata(target=self.ncformat.target_dict.get(target, target), unit=unit,
                                                                           qibaotime=self.qibaotime, yubaotime=self.qibaotime),
                                                                           pro_map=self.pro_map)
                        self.out_tiffs.append(tiff)
                    elif data_dim == 3:
                        latlons = self.get_equidistant_box(self.lons, self.lats, latlon_units)
                        if data_dim_tar[0].lower() in self.ncformat.timename:
                            for inde, ts in enumerate(self.dset.variables[self.get_dimtar2datatar(data_dim_tar[0])][:]):
                                yubaotime = datetime.fromtimestamp(self.ns2s(ts)).strftime('%Y-%m-%d %H:%M:%S')
                                tiff = self.get_tiff(target, [yubaotime, '999'])
                                self.array2draw(latlons, self.getdata(data_obj[inde]), tiff, self.get_metadata(target=self.ncformat.target_dict.get(target, target), unit=unit,
                                                                                    qibaotime=self.qibaotime,
                                                                                    yubaotime=yubaotime),
                                                                                    pro_map=self.pro_map)
                                self.out_tiffs.append(tiff)
                        elif data_dim_tar[0].lower() in self.ncformat.levelname:
                            for inde, level in enumerate(self.dset.variables[self.get_dimtar2datatar(data_dim_tar[0])][:].squeeze()):
                                tiff = self.get_tiff(target, [self.qibaotime, self.get_dimtar2datatar(data_dim_tar[1]), level])
                                self.array2draw(latlons, self.getdata(data_obj[inde]), tiff, self.get_metadata(target=self.ncformat.target_dict.get(target, target), unit=unit,
                                                                                    qibaotime=self.qibaotime,
                                                                                    yubaotime=self.qibaotime,
                                                                                    level=str(level)),
                                                                                    pro_map=self.pro_map)
                                self.out_tiffs.append(tiff)
                    elif data_dim == 4:
                        latlons = self.get_equidistant_box(self.lons, self.lats, latlon_units)
                        for ts_inde, ts in enumerate(self.dset.variables[self.get_dimtar2datatar(data_dim_tar[0])][:]):
                            for level_inde, level in enumerate(self.dset.variables[self.get_dimtar2datatar(data_dim_tar[1])][:].squeeze()):
                                yubaotime = datetime.fromtimestamp(self.ns2s(ts)).strftime('%Y-%m-%d %H:%M:%S')
                                tiff = self.get_tiff(target, [yubaotime, self.get_dimtar2datatar(data_dim_tar[1]), level])
                                self.array2draw(latlons, self.getdata(data_obj[ts_inde][level_inde]), tiff, self.get_metadata(target=self.ncformat.target_dict.get(target, target), unit=unit,
                                                                                       qibaotime=self.qibaotime,
                                                                                       yubaotime=yubaotime,
                                                                                       level=str(level)),
                                                                                       pro_map=self.pro_map)
                                self.out_tiffs.append(tiff)
                except Exception as e:
                    print(traceback.format_exc())
                    print(target, 'ssdddddddd', self.lats, self.lons)


    def array2draw(self, latlons=[], arrays=[], tiff_outfile=None, metadata={}, pro_map=None):
        latmin, latmax, lonmin, lonmax = latlons
        y, x = arrays.shape
        lat = np.linspace(latmax, latmin, y)
        lon = np.linspace(lonmin, lonmax, x)
        lons, lats = np.meshgrid(lon, lat)
        array2png(arrays, lats, lons, imagename=tiff_outfile.replace('Tiff', 'png'))


    def array2tiff(self, latlons=[], arrays=[], tiff_outfile=None, metadata={}, pro_map=None):
        latmin, latmax, lonmin, lonmax = latlons
        if isinstance(arrays, list):
            lat_n, lon_n = arrays[0].shape
            band_num = len(arrays)
        else:
            lat_n, lon_n = arrays.shape
            band_num = 1
        lat_res = (latmax - latmin) / (lat_n - 1)
        lon_res = (lonmax - lonmin) / (lon_n - 1)
        print('latres, lonres', lat_res, lon_res)
        driver = gdal.GetDriverByName('GTiff')
        tiff = driver.Create(tiff_outfile, lon_n, lat_n, band_num, gdal.GDT_Float32)
        # print(metadata)
        tiff.SetMetadata(metadata)
        print('lonmin, lon_res, 0, latmax, 0, -lat_res', lonmin, lon_res, 0, latmax, 0, -lat_res)
        # 设置影像的显示范围
        tiff.SetGeoTransform((lonmin, lon_res, 0, latmax, 0, -lat_res))
        # 获取地理坐标系统信息，用于选取需要的地理坐标系统
        src = osr.SpatialReference()
        # 定义输出的坐标系为"WGS 84"，AUTHORITY["EPSG","4326"]
        src.ImportFromEPSG(4326)
        # print(pro_map)
        # 给新建图层赋予投影信息
        if pro_map is None:
            tiff.SetProjection(src.ExportToWkt())
        else:
            tiff.SetProjection(pro_map)
        if isinstance(arrays, list) or (isinstance(arrays, np.ndarray) and len(arrays.shape) == 3):
            for inde, array in enumerate(arrays):
                # 数据写出
                tiff.GetRasterBand(1 + inde).WriteArray(arrays[inde])
        else:
            tf = tiff.GetRasterBand(1)
            tf.WriteArray(arrays)
        # 将数据写入硬盘
        tiff.FlushCache()
        del tiff
        # logger.info("文件生成【%s 】" % tiff_outfile)


def read_tiff(tiff_file):
    dataset = gdal.Open(tiff_file)
    cols = dataset.RasterXSize  # 图像长度
    rows = (dataset.RasterYSize)  # 图像宽度
    im_proj = (dataset.GetProjection())  # 读取投影
    im_Geotrans = (dataset.GetGeoTransform())  # 读取仿射变换
    im_data = dataset.ReadAsArray(0, 0, cols, rows)  # 转为
    print(im_data)


if __name__ == '__main__':
    file = '/Users/xujimao/project/aierda/cmacast/NWP_MCTR_002/ECMF_DAM/PUB/W_NAFP_C_ECMF_20211019060050_P_C1D10190000102021001'
    file = '../../data/gfs.0p25.2021080318.f000.grib2'
    # file = '../../data/00192130100.nc'
    file = '/Users/xujimao/project/nanhai/result/radar/20211002/meiji0000_20211002120543006.nc'
    # file = '../../data/run_d1_d2-d2.nc'
    # file = './20220617152007/999/Precip.Tiff'
    # starttime = time.time()
    ncf = NCformat()
    # ncf.grid_map_type = 2
    # ncf.standard_parallel_1 = 30
    # ncf.standard_parallel_2 = 60
    # ncf.latitude_of_origin = 30
    # ncf.longitude_of_central_meridian = 100
    # ncf.set_target(**{})
    nctiff = NC2Tiff(file, '.', qibaotime='2022-01-01 10:10:10', ncformat=ncf)
    nctiff.show_nc()
    # nctiff.resolve_target()
    # print(time.time() - starttime)

    # gribs = read_gridfile(file, allname=True)
    # lists = []
    # for g in gribs:
    #     latlons = [g.latmin, g.latmax, g.lonmin, g.lonmax]
    #     print('g.shortname', g.shortname, g.__str__(), type(g.datas))
    #     array2tiff(latlons, g.datas, '../../tiff/' + g.shortname.replace(' ', '_') + "_" +
    #                str(g.level).replace(' ', '') + '.tiff')
    # read_tiff(file)

    latlons = [1, 10, 0, 9]
    lat = np.linspace(1, 10, 10)
    lon = np.linspace(1, 10, 10)
    lons, lats = np.meshgrid(lon, lat)
    datas = np.arange(1, 101).reshape(10, 10)[::-1]
    metadata = {
        'target': 'test', 'unit': 'degree', 'level': '0', 'qibaotime': '2022-01-01 12:00:00',
        'yubaotime': '2022-01-01 15:00:00'
    }
    # array2tiff(latlons, datas, 'test.tiff', metadata)
    # g.SetMetadata({"d": 't'}, "")
