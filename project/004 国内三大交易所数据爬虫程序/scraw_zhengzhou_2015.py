#!usr/bin/env python
'''
#-*- coding:utf-8 -*-
@Author HardyYao
@Time 2017/10/11 19:48
'''

import requests
import xlwt
import time
import random
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
from conn import headers

class getZhengZhou2015(object):
    def get_data(self, place, variety, contract_id, year, month, day, path):
        req = requests.get('http://www.czce.com.cn/portal/exchange/{}/datatradeholding/{}{}{}.htm'.format(year, year, month, day), headers=headers())

        if str(req) != '<Response [200]>':
            pass
        else:
            try:
                html = req.text.encode(req.encoding).decode('gbk')
            except(HTTPError, URLError) as e:
                print('Error:' + e)
            try:
                bsObj = BeautifulSoup(html, 'html.parser')
            except AttributeError as e:
                print('Error:' + e)

            tab = bsObj.findAll('table')
            if len(tab) > 0:
                tab1 = tab[2]
                tr = tab1.findAll('tr')

                contract_index = 0

                for trItem in tr:
                    contract_index += 1
                    if trItem.text.replace('\n', '').replace('\xa0', '').find('合约：{}'.format(contract_id)) == True:
                        break

                if contract_index < len(tr):
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
                    for trIter in tr[contract_index+1:]:
                        tempList = []
                        trIter = trIter.findAll('td')
                        for item in trIter:
                            tempList.append(item.string)

                        if tempList[0] == '合计':
                            break
                        if tempList[0:9]:
                            worksheet.write(int(tempList[0]), 0, '{}/{}/{}'.format(year, month, day))
                            worksheet.write(int(tempList[0]), 1, place)
                            worksheet.write(int(tempList[0]), 2, variety)
                            worksheet.write(int(tempList[0]), 3, contract_id)
                            worksheet.write(int(tempList[0]), 4, tempList[0])
                            worksheet.write(int(tempList[0]), 5, tempList[1])
                            worksheet.write(int(tempList[0]), 6, tempList[2])
                            worksheet.write(int(tempList[0]), 7, tempList[3])
                            worksheet.write(int(tempList[0]), 8, tempList[0])
                            worksheet.write(int(tempList[0]), 9, tempList[4])
                            worksheet.write(int(tempList[0]), 10, tempList[5])
                            worksheet.write(int(tempList[0]), 11, tempList[6])
                            worksheet.write(int(tempList[0]), 12, tempList[0])
                            worksheet.write(int(tempList[0]), 13, tempList[7])
                            worksheet.write(int(tempList[0]), 14, tempList[8])
                            worksheet.write(int(tempList[0]), 15, tempList[9])
                    workbook.save('{}\\{}.{}.{}-{}.xls'.format(path, year, month, day, contract_id))
                    print('{}.{}.{}的({}-{})数据已采集到并保存为excel文件'.format(year, month, day, variety, contract_id))

        time.sleep(random.randint(0, 1))