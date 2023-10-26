#!/usr/bin/env python
# coding=utf-8

"""
@author: xu
@license: MIT
@file: draw.py
@date: 2023/10/23 21:02
@desc: 
"""
import matplotlib
matplotlib.use('Agg')
import os
import sys
import json
from PIL import Image
from loguru import logger
from matplotlib.colors import LinearSegmentedColormap, Normalize, ListedColormap
import numpy as np
import matplotlib.pyplot as plt

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


def array2png(data, lats, lons, imagename=None):
    latmin, latmax, lonmin, lonmax = np.nanmin(lats), np.nanmax(lats), np.nanmin(lons), np.nanmax(lons)
    height, width = data.shape
    minu = np.nanmin(data)
    maxu = np.nanmax(data)
    data_copy = (data - minu) / (maxu - minu)
    data_copy = (data_copy * 255).astype(np.uint8)
    datas = np.zeros(data.shape + (4,), dtype=np.uint8)
    datas[:, :, 0] = data_copy
    datas[:, :, 3] = 255
    dicts = {'min': minu if not np.isnan(minu) else '',
             'max': maxu if not np.isnan(maxu) else '',
             'width': width, 'height': height, 'lonmin': lonmin, 'latmin': latmin,
             'lonmax': lonmax, 'latmax': latmax, 'datas': np.where(np.isnan(data), None, data).tolist()}
    if os.path.exists(imagename):
        logger.debug("[%s]已存在" % imagename)
        # return dicts
    im = Image.fromarray(datas)
    im.save(imagename)
    im.close()
    with open(imagename.replace('png', 'json'), 'w', encoding='utf8') as w:
        w.write(json.dumps(dicts, cls=MyEncoder))
    # logger.debug(json.dumps(dicts, cls=MyEncoder))
    logger.debug('create image[%s] success' % imagename)
    logger.debug('create json[%s] success' % imagename.replace('png', 'json'))
    return dicts


def draw_image(data, lats, lons, imagename=None, drawtype=True):
    """
    绝大部分数值小于10的时候，经纬度信息为nan，
    :param data:
    :param lats:
    :param lons:
    :param imagename:
    :return:
    """
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_axes([0.1, 0.1, 0.7, 0.7])
    ax.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
    plt.margins(0, 0)
    target = os.path.basename(imagename).split('_')[-2]
    latmin, latmax, lonmin, lonmax = np.nanmin(lats), np.nanmax(lats), np.nanmin(lons), np.nanmax(lons)
    mindata = np.nanmin(data)
    maxdata = np.nanmax(data)
    if mindata == maxdata:
        return
    copy_data = (copy_data - mindata) / (maxdata - mindata)
    lists = [(i / 255, 0, 0) for i in range(256)]
    cmap = LinearSegmentedColormap.from_list('huise', lists, N = 256)
    # coll = plt.contour(lons, lats, copy_data, cmap=cmap, norm=Normalize(vmax=1, vmin=0))
    if target not in []:
        plt.pcolor(lons, lats, copy_data, cmap=cmap, norm=Normalize(vmax=1, vmin=0))
    else:
        plt.contourf(lons, lats, copy_data, cmap=cmap, norm=Normalize(vmax=1, vmin=0))
    # datad1 = np.array(data).flatten()
    # co = (datad1-mindata) / (maxdata - mindata)
    # co = list(zip(co.tolist(), np.zeros(len(co)), np.zeros(len(co))))
    # plt.scatter(np.array(lons), np.array(lats), c=co, s=.5, marker='s')
    dicts = {'min': mindata, 'max': maxdata,
             'width': int(100*0.7*9), 'height': int(100 * 0.7* 6), 'lonmin': lonmin, 'latmin': latmin,
             'lonmax': lonmax, 'latmax': latmax, 'datas': np.where(np.isnan(data), None, data).tolist(), 'datas_height': data.shape[0], 'data_width': data.shape[1]}
    with open(imagename.replace('png', 'json'), 'w', encoding='utf8') as w:
        w.write(json.dumps(dicts, cls=MyEncoder))
    logger.debug(json.dumps({'min': mindata, 'max': maxdata,
             'width': int(100*0.7*9), 'height': int(100 * 0.7* 6), 'lonmin': lonmin, 'latmin': latmin,
             'lonmax': lonmax, 'latmax': latmax}, cls=MyEncoder))
    logger.debug('create image[%s] success' % imagename)
    logger.debug('create json[%s] success' % imagename.replace('png', 'json'))
    plt.savefig(imagename, transparent=True, bbox_inches='tight', dpi=100, pad_inches=0.0)
    plt.close(fig)
    return dicts


def draw_uv_image(u, v, lats, lons, imagename=None):
    """
        :param data:
        :param lats:
        :param lons:
        :param imagename:
        :return:
        """
    latmin, latmax, lonmin, lonmax = np.nanmin(lats), np.nanmax(lats), np.nanmin(lons), np.nanmax(lons)
    height, width = u.shape
    minu = np.nanmin(u)
    maxu = np.nanmax(u)
    minv = np.nanmin(v)
    maxv = np.nanmax(v)
    u = (u - minu) / (maxu - minu)
    v = (v - minv) / (maxv - minv)
    if np.isnan(minu) or minu == maxu or minv == maxv:
        return
    uint8 = (u * 255).astype(np.uint8)
    vint8 = (v * 255).astype(np.uint8)
    datas = np.zeros(u.shape + (4,), dtype=np.uint8)
    datas[:, :, 0] = uint8
    datas[:, :, 1] = vint8
    datas[:, :, 3] = 255
    im = Image.fromarray(datas)
    im.save(imagename)
    dicts = {'umin': minu, 'umax': maxu, 'vmin': minv, 'vmax':maxv,
             'width': width, 'height': height, 'lonmin': lonmin, 'latmin': latmin,
             'lonmax': lonmax, 'latmax': latmax}
    with open(imagename.replace('png', 'json'), 'w', encoding='utf8') as w:
        w.write(json.dumps(dicts, cls=MyEncoder))
    logger.debug(json.dumps(dicts, cls=MyEncoder))
    logger.debug('create image[%s] success' % imagename)
    logger.debug('create json[%s] success' % imagename.replace('png', 'json'))
    return dicts
