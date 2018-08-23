#!usr/bin/env python
'''
#-*- coding:utf-8 -*-
@Author HardyYao
@Time 2017/10/2 7:27
'''

import requests
import xlwt
import time
import random
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
from http.client import RemoteDisconnected, IncompleteRead
from urllib3.exceptions import ProtocolError
from requests.exceptions import ConnectionError, ChunkedEncodingError
from conn import headers

class getDaLianFutures(object):
    def get_data(self, place_dalian, variety, variety_id, contract_id, year, month, day, path):

        form_data = {'memberDealPosiQuotes.variety': '{}'.format(variety_id),
                     'memberDealPosiQuotes.trade_type':  '0',
                     'year': year,
                     'month': '{}'.format(month),
                     'day': '{}'.format(day),
                     'contract.contract_id': '{}'.format(contract_id),
                     'contract.variety_id': '{}'.format(variety_id),
                     }

        try:
            req = requests.post("http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html",
                            data=form_data, headers=headers())
            if str(req) != '<Response [200]>':
                print(str(req) + '{}.{}.{}无法获取URL，响应内容长度为零，重新进行获取！'.format(year, int(month) + 1, day))
                self.get_data(place_dalian, variety, variety_id, contract_id, year, month, day, path)

            else:
                try:
                    html = req.text.encode(req.encoding).decode('utf-8')
                except(URLError, HTTPError) as e:
                    print("Error: {}".format(e))

                try:
                    bsObj = BeautifulSoup(html, "html.parser")
                except AttributeError as e:
                    print("Error" + e)
                try:
                    tab = bsObj.findAll('table')

                    if len(tab) > 1:  ######
                        tab1 = tab[1]
                        tds = tab1.findAll('tr')

                        tr_index = len(tds) - 1
                        if tr_index > 1:  # 如果当天有数据，就进行获取
                            # 创建workbook（即excel文件）
                            workbook = xlwt.Workbook()
                            # 创建表
                            worksheet = workbook.add_sheet('Sheet1')
                            first_col = worksheet.col(0)
                            first_col.width = 256 * 16
                            seco_col = worksheet.col(1)
                            seco_col.width = 256 * 16
                            third_col = worksheet.col(2)
                            third_col.width = 256 * 16
                            four_col = worksheet.col(3)
                            four_col.width = 256 * 16
                            five_col = worksheet.col(4)
                            five_col.width = 256 * 16
                            six_col = worksheet.col(5)
                            six_col.width = 256 * 16
                            seve_col = worksheet.col(6)
                            seve_col.width = 256 * 16
                            eight_col = worksheet.col(7)
                            eight_col.width = 256 * 16
                            nine_col = worksheet.col(8)
                            nine_col.width = 256 * 16
                            ten_col = worksheet.col(9)
                            ten_col.width = 256 * 16
                            elev_col = worksheet.col(10)
                            elev_col.width = 256 * 16
                            twel_col = worksheet.col(11)
                            twel_col.width = 256 * 16
                            thritteen_col = worksheet.col(12)
                            thritteen_col.width = 256 * 16
                            fourteen_col = worksheet.col(13)
                            fourteen_col.width = 256 * 16
                            fifteen_col = worksheet.col(14)
                            fifteen_col.width = 256 * 16
                            sixteen_col = worksheet.col(15)
                            sixteen_col.width = 256 * 16

                            # 写标题行数据
                            worksheet.write(0, 0, '日期')
                            worksheet.write(0, 1, '交易所')
                            worksheet.write(0, 2, '品种')
                            worksheet.write(0, 3, '合约')
                            worksheet.write(0, 4, '成交量名次')
                            worksheet.write(0, 5, '成交量会员简称')
                            worksheet.write(0, 6, '成交量')
                            worksheet.write(0, 7, '成交量增减')
                            worksheet.write(0, 8, '持买单量名次')
                            worksheet.write(0, 9, '持买单量会员简称')
                            worksheet.write(0, 10, '持买单量')
                            worksheet.write(0, 11, '持买单量增减')
                            worksheet.write(0, 12, '持卖单量名次')
                            worksheet.write(0, 13, '持卖单量会员简称')
                            worksheet.write(0, 14, '持卖单量')
                            worksheet.write(0, 15, '持卖单量增减')

                            # 写列表内容数据
                            for trIter in tds[1:tr_index]:  # 下标为0的那一行为表格标题，已写好，无需遍历
                                trIter = trIter.findAll('td')  # 只需收集非表格标题行的列表内容
                                # print(len(trIter))
                                tempList = []
                                for item in trIter:
                                    tempList.append(item.string)

                                if tempList[0:4] or tempList[4:8] or tempList[8:12]:
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 0,
                                                    '{}/{}/{}'.format(year, int(month) + 1, day))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 1, '{}'.format(place_dalian))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 2, '{}'.format(variety))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 3, '{}'.format(contract_id))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 4,
                                                    str(tempList[0]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 5,
                                                    str(tempList[1]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 6,
                                                    str(tempList[2]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 7,
                                                    str(tempList[3]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 8,
                                                    str(tempList[4]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 9,
                                                    str(tempList[5]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 10,
                                                    str(tempList[6]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 11,
                                                    str(tempList[7]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 12,
                                                    str(tempList[8]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 13,
                                                    str(tempList[9]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 14,
                                                    str(tempList[10]).replace('\xa0', ''))
                                    worksheet.write(int(tempList[0]) if tempList[0] != '\xa0'
                                                    else (int(tempList[4]) if tempList[4] != '\xa0'
                                                          else (int(tempList[8]) if tempList[8] != '\xa0'
                                                                else tr_index - 1)), 15,
                                                    str(tempList[11]).replace('\xa0', ''))

                            workbook.save('{}\\{}.{}.{}.xls'.format(path, year, int(month) + 1, day))
                            print('{}.{}.{}的({}-{})数据已采集到并保存为excel文件'.format(year, int(month) + 1, day, variety,
                                                                             contract_id))
                finally:
                    pass

        except (RemoteDisconnected, IncompleteRead, ProtocolError, ConnectionError, ChunkedEncodingError):
            print('网络异常，重新发送请求！')
            self.get_data(place_dalian, variety, variety_id, contract_id, year, month, day, path)


        time.sleep(random.randint(0, 1))