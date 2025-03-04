from config import logger, BINANCE_API_KEY, BINANCE_API_SECRET, BINANCE_WS_BASE_URL, BINANCE_HTTP_URL
import requests
import time


# get请求币安http api
def get_http_api(path, params=None):
    logger.info(f'get_http_api: {path}, {params}')
    response = requests.get(BINANCE_HTTP_URL + path, params=params)
    # logger.info(response.text)
    # logger.info(response.json())
    return response.json()

# 测试http服务器连通


def http_ping():
    json_data = get_http_api('/fapi/v1/ping')
    logger.info(json_data)
    return json_data


# 获取服务器时间
def get_server_time():
    json_data = get_http_api('/fapi/v1/time')
    logger.info(json_data)
    return json_data


# 获取交易规则和交易对
def get_exchange_info():
    json_data = get_http_api('/fapi/v1/exchangeInfo')
    logger.info(json_data)
    return json_data


# 获取近期成交
def get_recent_deal_trades(symbol, limit=500):
    params = {'symbol': symbol, 'limit': limit}
    json_data = get_http_api(path='/fapi/v1/trades', params=params)
    logger.info(json_data)
    return json_data


# 查询合约k线数据
def get_recent_deal_trades(pair, contractType='PERPETUAL', limit=500):
    '''

    '''
    params = {'symbol': symbol, 'limit': limit}
    json_data = get_http_api(path='/fapi/v1/trades', params=params)
    logger.info(json_data)
    return json_data


if __name__ == '__main__':
    # http_ping()
    # get_server_time()
    # 打印当前时间戳-毫秒
    # print(int(time.time()*1000))
    # print(get_server_time())
    # get_exchange_info()
    symbol = 'ETHUSDT'
    limit = 1000
    res = get_recent_deal_trades(symbol=symbol, limit=limit)
    print(res[0], res[-1])
