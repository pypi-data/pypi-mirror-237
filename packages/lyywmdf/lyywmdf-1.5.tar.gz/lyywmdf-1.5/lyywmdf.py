
import pandas as pd
import numpy as np
import MyTT
import os
import sys
import lyytools
import tqdm
from datetime import datetime
from pytdx.hq import TdxHq_API


def 分钟线合成日K(df) -> pd.DataFrame:
    所有分钟线 = df.copy()
    所有分钟线['day'] = pd.to_datetime(所有分钟线['day'])
    完美日K线 = 所有分钟线.resample('D', on='day').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum'}).dropna()
    完美日K线 = 完美日K线.reset_index(drop=False)
    完美日K线['day'] = 完美日K线['day'].dt.date
    return (完美日K线)


def 分钟线5合15(所有分钟线) -> pd.DataFrame:
    多分钟K线 = 所有分钟线.resample('15min', on='day').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum'}).dropna()
    多分钟K线 = 多分钟K线.reset_index(drop=False)
    多分钟K线['time'] = 多分钟K线['day'].dt.strftime('%H%M')
    多分钟K线['day'] = 多分钟K线['day'].dt.date
    # 多分钟K线.drop(columns=['day'], inplace = True)
    十点K线 = pd.DataFrame(多分钟K线, columns=['time', 'day', 'high'])[多分钟K线['time'] == '1000']
    # 成功。从result中抽取时间和日期和最高价，生成当日的冲高数据
    return (十点K线)


def 多周期K线合并(完美日K线, 十点K线) -> pd.DataFrame:
    # print(十点K线['date'].tail(1).apply(type).value_counts())
    # 用每天早上情况生成新日线。其中，o,h,l,c都是9点半到10点K线。CC为当天收盘价。UP为high/ref(cc,1)
    mg1_test = 十点K线.loc[:, ('high', 'day',)]
    mg1_test.rename(columns={'high': 'tenhigh'}, inplace=True)
    多周期合成K线 = pd.merge(完美日K线, mg1_test, on='day')

    多周期合成K线['up'] = list(map(lambda x, y: round((float(x) / float(y) - 1) * 100, 2), 多周期合成K线['high'], MyTT.REF(多周期合成K线['close'], 1)))
    多周期合成K线['chonggao'] = list(map(lambda x, y: round((float(x) / float(y) - 1) * 100, 2), 多周期合成K线['tenhigh'], MyTT.REF(多周期合成K线['close'], 1)))
    多周期合成K线['huitoubo'] = list(map(lambda x, y: round((1 - (float(x) / float(y))) * 100, 2), 多周期合成K线['close'], 多周期合成K线['high']))
    return (多周期合成K线)


def 合成完美K线(df) -> pd.DataFrame:
    df['shiftc'] = df['close'].shift(1)
    df['up'] = list(map(lambda x, y: x if x > y else y, df['close'], df['shiftc']))
    所有分钟线 = df.copy()
    所有分钟线['day'] = pd.to_datetime(所有分钟线['day'])
    新日K = 分钟线合成日K(所有分钟线)
    # print(新日K)
    新15分钟K = 分钟线5合15(所有分钟线)
    完美K线 = 多周期K线合并(新日K, 新15分钟K)
    # print(完美K线)
    return 完美K线


def 原始分钟df格式化(原始分钟df, debug=False):
    原始分钟df.drop(columns=['amount', 'year', 'month', 'day', 'hour', 'minute'], inplace=True)
    原始分钟df.columns = ['open', 'close', 'high', 'low', 'volume', 'day']

    原始分钟df['shiftc'] = 原始分钟df['close'].shift(1)
    原始分钟df['up'] = list(map(lambda x, y: x if x > y else y, 原始分钟df['close'], 原始分钟df['shiftc']))
    所有分钟线 = 原始分钟df.copy()
    所有分钟线['day'] = pd.to_datetime(所有分钟线['day'])

    新日K = 分钟线合成日K(所有分钟线)
    新15分钟K = 分钟线5合15(所有分钟线)
    完美df = 多周期K线合并(新日K, 新15分钟K)

    完美df['volume'] = 完美df['volume'].apply(lambda x: int(x / 10000))
    # 完美df['open'] = 完美df['open'].apply(lambda x: int(x * 100))
    # 完美df['close'] = 完美df['close'].apply(lambda x: int(x * 100))
    # 完美df['high'] = 完美df['high'].apply(lambda x: int(x * 100))
    # 完美df['low'] = 完美df['low'].apply(lambda x: int(x * 100))
    完美df['day'] = 完美df['day'].apply(lambda x: int(str(x)[:4]+str(x)[5:7]+str(x)[8:10]))
    # 完美df.dropna(inplace=True)

    return 完美df


def 通达信下载原始分钟K线(api, 股票数字代码: str, 要下载的K线数量, debug=False) -> pd.DataFrame:
    """
    通达信下载原始分钟K线(tdxserverip:str, 股票数字代码:str, 开始日期:str, 结束日期, debug=False)
    """
    fun_name = sys._getframe().f_code.co_name
    t0 = datetime.now()
    if debug:
        print("函数名：", fun_name)
    市场代码 = int(股票数字代码[0].find('6')) + 1
    if debug:
        lyytools.测速(t0, "一、下载原始K线->1. tdx api connect")  # 0.05 of mainwork 0.7
    t1 = datetime.now()
    df_tdx = api.to_df(api.get_security_bars(1, 市场代码, 股票数字代码, 0, 要下载的K线数量))
    if debug:
        lyytools.测速(t1, "一、下载原始K线->2. tdx get result")  # 0.17 of mainwork 0.7
    if len(df_tdx) < 1:
        print(fun_name+" "+股票数字代码+": 空数据，请检查@"+str(api)+", to:"+str(要下载的K线数量))
    return (df_tdx)


def wmdf(api, stk_code_num, to_down_kline, debug=False) -> pd.DataFrame:
    if debug:
        print("函数名：", sys._getframe().f_code.co_name, ": try to get wmdf")
    if debug:
        t0 = datetime.now()
    try:
        df = 通达信下载原始分钟K线(api, stk_code_num, to_down_kline, debug=debug)
        if df.empty:
            raise Exception("通达信下载原始分钟K线 error: DataFrame must not be empty")
    except Exception as e:
        print("Fuction: wmdf, try to run 通达信下载原始分钟线 error。stk_code_num:", stk_code_num, "to_down_kline:", to_down_kline, "api:", api, e)
        print("wmdf error:", e)
        return None
    if debug:
        lyytools.测速(t0, "通达信下载原始K线")
    t1 = datetime.now()

    try:
        wmdf = 原始分钟df格式化(df)
    except Exception as e:
        print("error函数名：", sys._getframe().f_code.co_name, ": try to get wmdf")
        print("api=", api, " stk_code_num=", stk_code_num, " to_down_line=", to_down_kline, "try to run wmdf = 原始分钟df格式化(df) error:", e)
        return None
    if debug:
        lyytools.测速(t1, "df格式转换")

    return wmdf


def mk_api_list(svlist, debug=False) -> list:
    api_list = []
    if debug:
        print("函数名：", sys._getframe().f_code.co_name)

    for i in tqdm.tqdm(range(len(svlist))):
        try:
            serverip, tdxport = svlist[i], 7709
            if debug:
                print("mk_api_list: try to con to ", serverip)
            exec("api"+str(i)+" = TdxHq_API(multithread=False,heartbeat=False,auto_retry=True)")
            exec("api"+str(i)+".connect(serverip, tdxport)")
            api_list.append(eval("api"+str(i)))
        except Exception as e:

            print("mk_api_list error", e)
    print("mkapi: All done")
    return api_list


if __name__ == "__main__":
    import lyytools
    import lyyf_mysql
    import mongodb
    from sqlalchemy import create_engine

    def assign(list1, list2):
        """
        把服务器列表依次、循环分配到股票代码，让每个代码拥有专属服务器
        """
        dict_result = {}
        iter_list2 = iter(list2)
        for idx, val in enumerate(list1):
            try:
                dict_result[val] = next(iter_list2)
            except StopIteration:
                iter_list2 = iter(list2)
                dict_result[val] = next(iter_list2)
        return dict_result
    engine = create_engine('mysql+pymysql://cy:Yc124164@rm-7xvcw05tn97onu88s7o.mysql.rds.aliyuncs.com:3306/fpdb?charset=utf8')
    conn = engine.connect()

    # 获取股票代码表
    df = pd.read_sql_table('stock_all_codes', conn)
    stock_list = df['code'].tolist()
    server_list, _ = lyyf_mysql.get_list_from_sql("stock_tdx_server", "ip", "error_times<1")
    tdxapi_list = mk_api_list(server_list)
    sv_for_code_dic = assign(stock_list, tdxapi_list)
    db1 = mongodb.con_db("stock")
