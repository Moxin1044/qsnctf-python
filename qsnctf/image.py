# -*- coding: utf-8 -*-
"""图片工具（EXIF 读取等）

依赖可选库 Pillow：``pip install Pillow``
"""

try:
    from PIL import Image, ExifTags
except ImportError:
    Image = None
    ExifTags = None

__all__ = ['exif_read']


def _require_pillow():
    if Image is None:
        raise ImportError("图片功能需要可选依赖 'Pillow'（pip install Pillow）")


def _gps_to_decimal(values):
    """GPS 度分秒 → 十进制度数"""
    degrees, minutes, seconds = (float(value) for value in values)
    return degrees + minutes / 60 + seconds / 3600


def _parse_gps(exif):
    """解析 GPS IFD，返回含十进制经纬度的字典"""
    try:
        gps_ifd = exif.get_ifd(0x8825)
    except Exception:
        gps_ifd = exif.get(0x8825) or {}
    if not gps_ifd:
        return {}
    result = {}
    for tag_id, value in gps_ifd.items():
        name = ExifTags.GPSTAGS.get(tag_id, str(tag_id)) if ExifTags else str(tag_id)
        result[name] = value
    try:
        latitude = _gps_to_decimal(gps_ifd[2])
        longitude = _gps_to_decimal(gps_ifd[4])
        if gps_ifd.get(1) in ('S', b'S'):
            latitude = -latitude
        if gps_ifd.get(3) in ('W', b'W'):
            longitude = -longitude
        result['Latitude'] = round(latitude, 8)
        result['Longitude'] = round(longitude, 8)
    except Exception:
        pass
    return result


def exif_read(path):
    """读取图片 EXIF 信息

    :param path: 图片路径
    :return: 字典 {标签名: 值}；含 GPS 时额外给出 'GPS' 子字典（含十进制 Latitude/Longitude）
    """
    _require_pillow()
    with Image.open(path) as image:
        exif = image.getexif()
    if not exif:
        return {}
    result = {}
    for tag_id, value in exif.items():
        name = ExifTags.TAGS.get(tag_id, str(tag_id))
        result[name] = value
    gps = _parse_gps(exif)
    if gps:
        result['GPS'] = gps
    return result
