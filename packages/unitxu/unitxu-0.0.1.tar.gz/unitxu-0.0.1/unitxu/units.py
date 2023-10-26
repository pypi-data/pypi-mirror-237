#!/usr/bin/env python
# -*- coding=utf-8 -*-
import gzip
import json
import math
import os
import sys
import tarfile
import zipfile

from PIL import Image
from loguru import logger
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap, Normalize, ListedColormap
# import gdal
# from gdal import osr
# from osgeo import gdal
# from osgeo import osr
import numpy as np
import matplotlib.pyplot as plt
#from netCDF4 import Dataset






def merge_color(color1='autumn_r', color2='winter'):
    colora = cm.get_cmap(color1, 128)
    colorb = cm.get_cmap(color2, 128)
    cmp = np.vstack((colorb(np.arange(128)), colora(np.arange(128))))
    newcmp = ListedColormap(cmp, name='newcmp')
    return newcmp


def addcheckpoint(checkpoint_filename, file):
    if not os.path.exists(os.path.dirname(checkpoint_filename)):
        os.makedirs(os.path.dirname(checkpoint_filename))
    # 追加记录标记
    with open(checkpoint_filename, 'a') as w:
        w.write(file + '\n')


def clearcheckpoint(checkpoint_filename):
    if isinstance(checkpoint_filename, str) and os.path.exists(checkpoint_filename):
        os.remove(checkpoint_filename)


def get_files(dirname, flag=True, method_filter=None, checkpoint='checkpoint'):
    files = []
    if not os.path.exists(dirname):
        return files
    def dfs(dir_name):
        if os.path.isfile(dir_name):
            files.append(dir_name)
        else:
            for dirn in os.listdir(dir_name):
                dfs(os.path.join(dir_name, dirn))
    dfs(dirname)

    if flag:
        files = files
    else:
        if method_filter is not None:
            files = list(filter(method_filter, files))
        if os.path.exists(checkpoint):
            with open(checkpoint, 'r', encoding='utf8') as f:
                yidu_files = f.readlines()
            yidu_files = [yidu_file.strip() for yidu_file in yidu_files]
            files = list(filter(lambda x: x not in yidu_files, files))
    return sorted(files, reverse=True)


def getSRSPair(dataset):
    # return 投影坐标系 地理坐标系
    prosrs = osr.SpatialReference()
    if dataset.GetProjection():
        prosrs.ImportFromWkt(dataset.GetProjection())
    else:
        pro = 'PROJCS["unnamed",GEOGCS["Coordinate System imported from GRIB file",' \
              'DATUM["unknown",SPHEROID["Sphere",6371200,0]],PRIMEM["Greenwich",0],' \
              'UNIT["degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic_2SP"],' \
              'PARAMETER["standard_parallel_1",30],PARAMETER["standard_parallel_2",60],' \
              'PARAMETER["latitude_of_origin",30],PARAMETER["central_meridian",100],' \
              'PARAMETER["false_easting",0],PARAMETER["false_northing",0]]'
        prosrs.ImportFromWkt(pro)
    geosrs = prosrs.CloneGeogCS()
    return prosrs, geosrs


def geo2lonlat(dataset, x, y):
    print(dataset.GetProjection())
    prosrs, geosrs = getSRSPair(dataset)
    ct = osr.CoordinateTransformation(prosrs, geosrs)
    if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        xyshape = x.shape
        x = x.flatten().tolist()
        y = y.flatten().tolist()
        xs = []
        ys = []
        for xx, yy in zip(x, y):
            coords = ct.TransformPoint(xx, yy)
            xs.append(coords[0])
            ys.append(coords[1])
        print('lonmin', np.array(xs).min())
        print('lonmax', np.array(xs).max())
        print('latmin', np.array(ys).min())
        print('latmax', np.array(ys).max())
        return np.array(xs).reshape(xyshape), np.array(ys).reshape(xyshape)
    elif isinstance(x, float) and isinstance(y, float):
        coords = ct.TransformPoint(x, y)
        return coords[:2]
    else:
        return None, None


def image2geo(dataset, row, col):
    trans = dataset.GetGeoTransform()
    px = trans[0] + col * trans[1] + row * trans[2]
    py = trans[3] + col * trans[4] + row * trans[5]
    print(px, py)
    # return geo2lonlat(dataset, px, py)
    return px, py


def jieya_tar(inputfile, outfile):
    if os.path.exists(outfile):
        logger.debug('文件夹存在【%s】' % outfile)
        return
    with tarfile.open(inputfile, 'r:') as input_stream:
        input_stream.extractall(outfile)
    logger.debug('文件解压成功【%s】--->【%s】' % (inputfile, outfile))


def unzip(inputfile, outfile):
    r = zipfile.is_zipfile(inputfile)
    if not os.path.exists(outfile):
        os.makedirs(outfile)
    filelist = []
    if r:
        fz = zipfile.ZipFile(inputfile, 'r')
        for f in fz.namelist():
            fz.extract(f, outfile)
            filelist.append(os.path.join(outfile, f))
    logger.debug('文件解压成功【%s】--->【%s】' % (inputfile, outfile))
    return filelist


def jieya_bz2(inputfile, outfile):
    if os.path.exists(outfile):
        logger.debug('文件存在【%s】' % outfile)
        return
    if not os.path.exists(os.path.dirname(outfile)):
        os.makedirs(os.path.dirname(outfile))
    with open(outfile, 'wb') as new_file, bz2.BZ2File(inputfile, 'rb') as file:
        for data in iter(lambda : file.read(100 * 1024), b''):
            new_file.write(data)

def insert_db(con, sql):
    logger.debug(sql)
    try:
        con.execute(sql)
        logger.debug('数据插入成功【%s】' % sql)
    except Exception as e:
        logger.error("数据插入失败【%s】" % str(e))


def lambert2latlon(LonRef, LatRef, Slat, Nlat, deltaY, deltaX, EarA, EarB):
    """
    char Projection;
          :grid_mapping_name = "lambert_conformal_conic";
          :latitude_of_projection_origin = 30.0; // double LatRef
          :longitude_of_central_meridian = 100.0; // double LonRef
          :standard_parallel = 30.0, 60.0; // double Slat Nlat
          :earth_radius = 6371229.0; // double
          :_CoordinateTransformType = "Projection";
          :_CoordinateAxes = "x y";
    lambert2latlon(100, 30, 30, 60, x, y, 6371229.0, 6356755.00)
        /// 兰伯特投影转换为经纬投影，手动指定长半轴和短半轴
        /// </summary>
        /// <param name="LonRef">参考经度，为了方便，按照角度输入</param>
        /// <param name="LatRef">参考纬度，为了方便，按照角度输入</param>
        /// <param name="Slat">m=1时的南纬度，为了方便，按照角度输入</param>
        /// <param name="Nlat">m=1时的北纬度，为了方便，按照角度输入</param>
        /// <param name="deltaY">Y方向上的距离，以米为单位</param> 需要计算的y方向距离坐标值
        /// <param name="deltaX">X方向上的距离，以米为单位</param> 需要计算的x方向距离坐标值
        /// <param name="EarA">地球长半轴</param>
        /// <param name="EarB">地球短半轴</param>
        /// <returns></returns>
    """
    pi = np.pi
    a = EarA # 地球长半轴
    b = EarB # 地球短半轴
    L0 = LonRef
    B0 = LatRef
    B1 = Slat
    B2 = Nlat
    Y = deltaY
    X = deltaX
    # 各种输入经纬度转化成弧度
    L0 = L0 / 180 * pi
    B0 = B0 / 180 * pi
    B1 = B1 / 180 * pi
    B2 = B2 / 180 * pi
    f = (a - b) / a
    e = np.power((2 * f - np.power(f, 2)), 0.5)
    mB1 = np.cos(B1) / np.power((1 - np.power(e, 2) * np.sin(B1) * np.sin(B1)), 0.5)
    mB2 = np.cos(B2) / np.power((1 - np.power(e, 2) * np.sin(B2) * np.sin(B2)), 0.5)
    tB0 = np.tan(pi / 4 - B0 / 2) / np.power(((1 - e * np.sin(B0)) / (1 + e * np.sin(B0))), (e / 2))
    tB1 = np.tan(pi / 4 - B1 / 2) / np.power(((1 - e * np.sin(B1)) / (1 + e * np.sin(B1))), (e / 2))
    tB2 = np.tan(pi / 4 - B2 / 2) / np.power(((1 - e * np.sin(B2)) / (1 + e * np.sin(B2))), (e / 2))
    n = np.log(mB1 / mB2) / np.log(tB1 / tB2)
    F = mB1 / (n * np.power(tB1, n))
    r0 = a * F * np.power(tB0, n)
    rd = np.sign(n) * np.power((np.power(Y, 2) + np.power((r0 - X), 2)), 0.5)
    td = np.power((rd / (a * F)), (1 / n))
    Thetad = np.arctan(Y / (r0 - X))
    L = Thetad / n + L0
    B = B0
    errf = 1
    num = 0
    while (np.abs(errf) > (float)(1e-8) and num < 2000):
        B1 = pi / 2 - 2 * np.arctan(td * np.power(((1 - e * np.sin(B)) / (1 + e * np.sin(B))), (e / 2)))
        errf = B1 - B
        B = B1
        num = num + 1
    B = B * 180 / pi
    L = L * 180 / pi
    return L, B


def get_argvs():
    if len(sys.argv) >=3:
        return sys.argv[1], sys.argv[2]
    else:
        return None


def insert_log(con, tablename, lists):
    sql = 'insert into %s(id, file, resolve_flag, starttime, endtime, datatime, name, datatype, message)' \
          ' values%s' % (tablename, str(tuple(lists))[1:-2])
    logger.debug(sql)
    con.execute(sql)


if __name__ == '__main__':
    # for i in range(10):
    #     addcheckpoint('checkpoint_upp', 'sdfds')
    # s = r'\ZHSDATA\20200911\WRFPRS_d01.00.nc'
    # print(geo2lonlat(gdal.Open(s), 2912418, -1806785))
    # jieya(r'GF5_VIMS_N10.0_E114.0_20190502_005224_L10000154524.tar.gz',
    #       r'GF5_VIMS')
    # lambert2latlon(LonRef, LatRef, Slat, Nlat, deltaY, deltaX, EarA, EarB)
    # lambert2latlon(70, 2.5, 30, 60, -3571673.59, -5677671, 6371229.0, 6356755.00)
    # xs, ys = readxy()
    # dataset = gdal.Open('/Multi_source_data_fusion/data/LAPS/lc3/192130400.nc')
    # lats = []
    # lons = []
    # for xx, yy in zip(xs, ys):
    #     xtemp = []
    #     ytemp = []
    #     for x, y in zip(xx, yy):
    #         lat, lon = lambert2latlon(100, 30, 30, 60, x, y, 6371229.0, 6356755.00)
    #         xtemp.append(lat)
    #         ytemp.append(lon)
    #     lons.append(xtemp.copy())
    #     lats.append(ytemp.copy())
    # print(np.array(lats).min())
    # print(np.array(lats).max())
    # print(np.array(lons).min())
    # print(np.array(lons).max())
    # dataset = gdal.Open('/Multi_source_data_fusion/ZHSDATA/WRFPRS_d01.00.nc')
    # print(geo2lonlat(dataset, xs, ys))
    unzip('20211102_001704.00.003.001_5.00_R0.zip',
          '/result')
