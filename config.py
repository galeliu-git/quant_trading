import os
from dotenv import load_dotenv
import logging
import sys

load_dotenv('.env', override=True)  # 加载 .env 文件中的环境变量


# 日志配置
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(lineno)d - %(message)s')


# 日志输出到控制台
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


# 日志输出到文件
file_handler = logging.FileHandler(
    './output.log')
file_handler.setLevel(level=logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


RUN_DEV = os.getenv('RUN_DEV')
if RUN_DEV == 'development':
    logger.info("---------启动测试环境---------")
    BINANCE_HTTP_URL = "https://testnet.binancefuture.com"
    BINANCE_WS_BASE_URL = 'wss://testnet.binancefuture.com/ws-fapi/v1'
else:
    logger.info("---------启动正式环境---------")
    BINANCE_HTTP_URL = "https://fapi.binance.com"
    BINANCE_WS_BASE_URL = 'wss://ws-fapi.binance.com/ws-fapi/v1'
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')
logger.info(f"API Key 已加载: {BINANCE_API_KEY[:4]}...")  # 显示前4位确认加载成功
