# -*- coding: UTF-8 -*-
# @Time : 2022/8/17 15:44 
# @Author : 刘洪波
import random


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

user_agents = [
    'Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
    'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
    'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
]

random_headers = {
    'user-agent': random.choice(user_agents),
}


class ContentType(object):
    app_json = 'application/json',
    app_xwfu = 'application/x-www-form-urlencoded',
    app_xml = 'application/xml',
    mul_fd = 'multipart/form-data',
    text_xml = 'text/xml'
    app_json_headers = {"Content-Type": "application/json;charset=utf-8"}
    app_xwfu_headers = {"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
    app_xml_headers = {"Content-Type": "application/xml;charset=utf-8"}
    mul_fd_headers = {"Content-Type": "multipart/form-data;charset=utf-8"}
    text_xml_headers = {"Content-Type": "text/xml;charset=utf-8"}


en_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class DateType(object):
    """
    常用日期格式：
    YYYY年MM月DD日
    YYYY/MM/DD
    YYYYMMDD
    YYYY.MM.DD
    YYYY-MM-DD
    """
    # YYYY-MM-DD
    y_1_m = '%Y-%m-%d %H:%M'
    m_1_m = '%m-%d-%Y %H:%M'
    d_1_m = '%d-%m-%Y %H:%M'
    y_1_s = '%Y-%m-%d %H:%M:%S'
    m_1_s = '%m-%d-%Y %H:%M:%S'
    d_1_s = '%d-%m-%Y %H:%M:%S'
    y_1 = '%Y-%m-%d'
    m_1 = '%m-%d-%Y'
    d_1 = '%d-%m-%Y'

    # YYYY年MM月DD日
    y_2_m = '%Y年%m月%d日 %H:%M'
    m_2_m = '%m月%d日%Y年 %H:%M'
    y_2_s = '%Y年%m月%d日 %H:%M:%S'
    m_2_s = '%m月%d日%Y年 %H:%M:%S'
    y_2_m_z = '%Y年%m月%d日 %H时%M分'
    m_2_m_z = '%m月%d日%Y年 %H时%M分'
    y_2_s_z = '%Y年%m月%d日 %H时%M分%S秒'
    m_2_s_z = '%m月%d日%Y年 %H时%M分%S秒'
    y_2 = '%Y年%m月%d日'
    m_2 = '%m月%d日%Y年'

    # YYYY.MM.DD
    y_3_m = '%Y.%m.%d %H:%M'
    m_3_m = '%m.%d.%Y %H:%M'
    y_3_s = '%Y.%m.%d %H:%M:%S'
    m_3_s = '%m.%d.%Y %H:%M:%S'
    y_3 = '%Y.%m.%d'
    m_3 = '%m.%d.%Y'

    # YYYYMMDD
    y_4_m = '%Y%m%d %H:%M'
    y_4_s = '%Y%m%d %H:%M:%S'
    y_4 = '%Y%m%d'

    # YYYY/MM/DD
    y_5_m = '%Y/%m/%d %H:%M'
    m_5_m = '%m/%d/%Y %H:%M'
    y_5_s = '%Y/%m/%d %H:%M:%S'
    m_5_s = '%m/%d/%Y %H:%M:%S'
    y_5 = '%Y/%m/%d'
    m_5 = '%m/%d/%Y'


class RePattern(object):
    window_INITIAL_STATE = r"window.__INITIAL_STATE__=(.*?}});"
