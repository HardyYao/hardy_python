#!usr/bin/env python
'''
#-*- coding:utf-8 -*-
@Author HardyYao
@Time 2017/10/2 7:32
'''

import scraw_dalian_data
import scraw_shanghai_data
import scraw_zhengzhou_2015
import scraw_zhengzhou_2015_sum
import scraw_zhengzhou_data
import scraw_zhengzhou_sum
import os


class mainClass(object):
    def getDalianData(self):
        variety = input('请输入品种名：')
        variety_id = input('请输入品种id：')
        contract_id = input('请输入合约：')
        choice = input('查询某一日数据请输入0，查询某一月数据请输入1，查询某上半年数据请输入2，查询某下半年数据查询请输入3，'
                       '查询某一整年数据请输入4：')
        # 查询某一日数据
        if choice == '0':
            year, month, day = input('请输入年：'), input('请输入月：'), input('请输入日：')
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            scraw_dalian_data.getDaLianFutures().get_data(place, variety, variety_id, contract_id, year,
                                                          month, day, path)

        # 查询某一月数据
        elif choice == '1':
            year, month = input('请输入年份：'), input('请输入月份：')
            days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            for day in days:
                scraw_dalian_data.getDaLianFutures().get_data(place, variety, variety_id, contract_id, year,
                                                              month, day, path)

        # 查询某上半年数据
        elif choice == '2':
            year = input('请输入年份：')
            months = ['0', '1', '2', '3', '4', '5']
            days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            for month in months:
                for day in days:
                    scraw_dalian_data.getDaLianFutures().get_data(place, variety, variety_id, contract_id, year,
                                                                  month, day, path)

        # 查询某下半年数据
        elif choice == '3':
            year = input('请输入年份：')
            months = ['6', '7', '8', '9', '10', '11']
            days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            for month in months:
                for day in days:
                    scraw_dalian_data.getDaLianFutures().get_data(place, variety, variety_id, contract_id, year,
                                                                  month, day, path)

        # 查询某一年数据
        else:
            year = input('请输入年份：')
            months = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
            days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            for month in months:
                for day in days:
                    scraw_dalian_data.getDaLianFutures().get_data(place, variety, variety_id, contract_id, year,
                                                                  month, day, path)

    def getShanghaiData(self):
        variety = input('请输入品种名：')
        contract_id = input('请输入合约：')
        url = 'http://www.shfe.com.cn/data/dailydata/kx/pm{}{}{}.dat'
        choice = input('查询某一日数据请输入0，查询某一月数据请输入1，查询某上半年数据请输入2，查询某下半年数据查询请输入3，'
                       '查询某一整年数据请输入4：')

        # 查询某一日数据
        if choice == '0':
            year, month, day = input('请输入年：'), input('请输入月：'), input('请输入日：')
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            scraw_shanghai_data.getShangHaiFutures().scraw_shanghai_data(place, variety,
                                                                         contract_id, year, month, day, url,
                                                                         path)

        # 查询某一月数据
        elif choice == '1':
            year, month = input('请输入年份：'), input('请输入月份：')
            days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            for day in days:
                scraw_shanghai_data.getShangHaiFutures().scraw_shanghai_data(place, variety,
                                                                             contract_id, year, month, day, url,
                                                                             path)

        # 查询某上半年数据
        elif choice == '2':
            year = input('请输入年份：')
            months = ['01', '02', '03', '04', '05', '06']
            days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            for month in months:
                for day in days:
                    scraw_shanghai_data.getShangHaiFutures().scraw_shanghai_data(place, variety,
                                                                                 contract_id, year, month, day, url,
                                                                                 path)

        # 查询某下半年数据
        elif choice == '3':
            year = input('请输入年份：')
            months = ['07', '08', '09', '10', '11', '12']
            days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            for month in months:
                for day in days:
                    scraw_shanghai_data.getShangHaiFutures().scraw_shanghai_data(place, variety,
                                                                                 contract_id, year, month, day, url,
                                                                                 path)

        # 查询某一年数据
        else:
            year = input('请输入年份：')
            months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
            days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
            disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
            path = '{}:\\{}-{}'.format(disk, variety, contract_id)
            if os.path.exists(path) == False:
                os.mkdir(path)
            for month in months:
                for day in days:
                    scraw_shanghai_data.getShangHaiFutures().scraw_shanghai_data(place, variety,
                                                                                 contract_id, year, month, day, url,
                                                                                 path)

    def getZhengzhouData(self):
        variety = input('请输入品种：')
        contract_id = input('请输入合约：')
        if contract_id == '汇总':
            choice = input('查询某一日数据请输入0，查询某一月数据请输入1，查询某上半年数据请输入2，查询某下半年数据查询请输入3，'
                           '查询某一整年数据请输入4：')
            # 查询某一日数据
            if choice == '0':
                year, month, day = input('请输入年：'), input('请输入月：'), input('请输入日：')
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    scraw_zhengzhou_2015_sum.getZhengZhou2015Sum().get_data(place, variety, contract_id, year, month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    scraw_zhengzhou_sum.getZhengZhouSum().get_data(place, variety, contract_id, year, month, day, path)

            # 查询某一月数据
            elif choice == '1':
                year, month = input('请输入年份：'), input('请输入月份：')
                days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for day in days:
                        scraw_zhengzhou_2015_sum.getZhengZhou2015Sum().get_data(place, variety, contract_id, year, month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for day in days:
                        scraw_zhengzhou_sum.getZhengZhouSum().get_data(place, variety, contract_id, year, month, day, path)

            # 查询某上半年数据
            elif choice == '2':
                year = input('请输入年份：')
                months = ['01', '02', '03', '04', '05', '06']
                days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_2015_sum.getZhengZhou2015Sum().get_data(place, variety, contract_id, year, month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_sum.getZhengZhouSum().get_data(place, variety, contract_id, year, month, day,
                                                                           path)

            # 查询某下半年数据
            elif choice == '3':
                year = input('请输入年份：')
                months = ['07', '08', '09', '10', '11', '12']
                days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_2015_sum.getZhengZhou2015Sum().get_data(place, variety, contract_id, year, month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_sum.getZhengZhouSum().get_data(place, variety, contract_id, year, month, day,
                                                                           path)

            # 查询某一年数据
            else:
                year = input('请输入年份：')
                months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
                days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_2015_sum.getZhengZhou2015Sum().get_data(place, variety, contract_id, year, month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_sum.getZhengZhouSum().get_data(place, variety, contract_id, year, month, day,
                                                                           path)


        else:
            choice = input('查询某一日数据请输入0，查询某一月数据请输入1，查询某上半年数据请输入2，查询某下半年数据查询请输入3，'
                           '查询某一整年数据请输入4：')
            # 查询某一日数据
            if choice == '0':
                year, month, day = input('请输入年：'), input('请输入月：'), input('请输入日：')
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    scraw_zhengzhou_2015.getZhengZhou2015().get_data(place, variety, contract_id, year,
                                                                                    month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    scraw_zhengzhou_data.getZhengZhouFutures().get_data(place, variety, contract_id, year, month,
                                                                            day, path)

            # 查询某一月数据
            elif choice == '1':
                year, month = input('请输入年份：'), input('请输入月份：')
                days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for day in days:
                        scraw_zhengzhou_2015.getZhengZhou2015().get_data(place, variety, contract_id, year,
                                                                                month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for day in days:
                        scraw_zhengzhou_data.getZhengZhouFutures().get_data(place, variety, contract_id, year, month,
                                                                        day, path)

            # 查询某上半年数据
            elif choice == '2':
                year = input('请输入年份：')
                months = ['01', '02', '03', '04', '05', '06']
                days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_2015.getZhengZhou2015().get_data(place, variety, contract_id, year,
                                                                                    month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_data.getZhengZhouFutures().get_data(place, variety, contract_id, year,
                                                                                month, day, path)

            # 查询某下半年数据
            elif choice == '3':
                year = input('请输入年份：')
                months = ['07', '08', '09', '10', '11', '12']
                days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_2015.getZhengZhou2015().get_data(place, variety, contract_id, year,
                                                                                    month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_data.getZhengZhouFutures().get_data(place, variety, contract_id, year,
                                                                                month, day, path)

            # 查询某一年数据
            else:
                year = input('请输入年份：')
                months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
                days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                if int(year) < 2016:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_2015.getZhengZhou2015().get_data(place, variety, contract_id, year,
                                                                                    month, day, path)
                else:
                    disk = input('请选择存储数据的磁盘：C，D，E或F盘：')
                    path = '{}:\\{}-{}'.format(disk, variety, contract_id)
                    if os.path.exists(path) == False:
                        os.mkdir(path)
                    for month in months:
                        for day in days:
                            scraw_zhengzhou_data.getZhengZhouFutures().get_data(place, variety, contract_id, year,
                                                                                month, day, path)


if __name__ == '__main__':
    print('''
    @Author HardyYao
    @Time 2017/10/2 7:32
    ''')
    print('********************************************************************************')
    print('由于三大交易所的网站结构各不相同，因此查询方式也有所不同')
    print('在查询大连交易所的数据时，输入的月份要从0开始算起，即查询一月份的数据时，要输入的月份为0，')
    print('依此类推，查询1到12月份的数据时，分别需要提供的月份参数为：0, 1, 2, 3, 4, ... , 11')
    print('由于提交表单数据的需要，查询大连交易所数据时还需要输入品种id，如铁矿石的品种id为：i')
    print('查询上海和郑州交易所时，需要输入的月份参数相同，都是：01, 02, 03, 04, ... , 12')
    print('其余查询时所需要的参数并无特别之处，需要注意的是品种名以及合约必须与官网上的相同，')
    print('否则将导致查询、采集数据结果出错。')
    print('********************************************************************************')

    place = input('请输入交易所名称：')

    # 如果查询的是大连商品交易所的数据
    if place == '大连':
        mainClass().getDalianData()

    # 如果查询的是上海商品交易所的数据
    elif place == '上海':
        mainClass().getShanghaiData()

    # 如果查询的是郑州商品交易所的数据
    elif place == '郑州':
        mainClass().getZhengzhouData()

    else:
        print('请输入正确的商品交易所名称！')

    continue_or_no = input('继续查询请输入y，退出请输入n：')
    while continue_or_no == 'y':
        place = input('请输入交易所名称：')

        # 如果查询的是大连商品交易所的数据
        if place == '大连':
            mainClass().getDalianData()

        # 如果查询的是上海商品交易所的数据
        elif place == '上海':
            mainClass().getShanghaiData()

        # 如果查询的是郑州商品交易所的数据
        elif place == '郑州':
            mainClass().getZhengzhouData()

        else:
            print('请输入正确的商品交易所名称！')

        continue_or_no = input('继续查询请输入y，退出请输入n：')