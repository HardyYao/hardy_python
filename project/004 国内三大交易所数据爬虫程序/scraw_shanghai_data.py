#!usr/bin/env python
'''
#-*- coding:utf-8 -*-
@Author HardyYao
@Time 2017/10/2 7:28
'''

import requests
import xlwt
import time
import random
from urllib.error import URLError, HTTPError
from json.decoder import JSONDecodeError
from conn import headers

class getShangHaiFutures(object):
    def scraw_shanghai_data(self, place_shanghai, variety, contract_id, year, month, day, url, path):
        req = requests.get(url.format(year, month, day), headers=headers())
        if req.status_code == 200:
            try:
                jsonData = req.json()
            except(URLError, HTTPError, JSONDecodeError) as e:
                print('Error:{}'.format(e))

            if len(jsonData['o_cursor']) > 10:
                # 创建一个空的excel文件
                workbook = xlwt.Workbook()
                # 创建表
                worksheet = workbook.add_sheet('Sheet1')
                first_col = worksheet.col(0)
                first_col.width = 256 * 16
                secon_col = worksheet.col(1)
                secon_col.width = 256 * 16
                third_col = worksheet.col(2)
                third_col.width = 256 * 16
                four_col = worksheet.col(3)
                four_col.width = 256 * 16
                five_col = worksheet.col(4)
                five_col.width = 256 * 16
                six_col = worksheet.col(5)
                six_col.width = 256 * 16
                seven_col = worksheet.col(6)
                seven_col.width = 256 * 16
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

                for i in range(len(jsonData['o_cursor'])):
                    if jsonData['o_cursor'][i]['INSTRUMENTID'].replace(' ', '') == contract_id:
                        if jsonData['o_cursor'][i]['RANK'] != -1 and jsonData['o_cursor'][i]['RANK'] != 0 and jsonData['o_cursor'][i]['RANK'] != 999:
                            worksheet.write(int(jsonData['o_cursor'][i]['RANK']), 0, '{}/{}/{}'.format(year, month, day))   # 日期
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 1, place_shanghai)  # 交易所
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 2, variety)    # 品种
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 3, contract_id)   # 合约
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 4, jsonData['o_cursor'][i]['RANK'])    # 成交量名次
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 5, jsonData['o_cursor'][i]['PARTICIPANTABBR1'],)   # 成交量会员简称
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 6, jsonData['o_cursor'][i]['CJ1'])     # 成交量
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 7, jsonData['o_cursor'][i]['CJ1_CHG'])     # 成交量增减
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 8, jsonData['o_cursor'][i]['RANK'])        # 持买单量名次
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 9, jsonData['o_cursor'][i]['PARTICIPANTABBR2'])        # 持买单量会员简称
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 10, jsonData['o_cursor'][i]['CJ2'])        # 持买单量
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 11, jsonData['o_cursor'][i]['CJ2_CHG'])    # 持买单量增减
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 12, jsonData['o_cursor'][i]['RANK'])       # 持卖单量名次
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 13, jsonData['o_cursor'][i]['PARTICIPANTABBR3'])       # 持卖单量会员简称
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 14, jsonData['o_cursor'][i]['CJ3'])     # 持卖单量
                            worksheet.write(jsonData['o_cursor'][i]['RANK'], 15, jsonData['o_cursor'][i]['CJ3_CHG'])        # 持卖单量增减
                workbook.save('{}\\{}.{}.{}.xls'.format(path, year, month, day))
                print('{}.{}.{}的({}-{})数据已采集到并保存为excel文件'.format(year, month, day, variety, contract_id))

        time.sleep(random.randint(0, 1))