import logging
import asyncio
from datetime import datetime
from services.file_handler import FilesHandler

asyncio.run(FilesHandler.create_directory("logs"))
# logging.basicConfig(filename='example.log',
#                     level=logging.INFO)

handler = logging.StreamHandler()
reader_handler = logging.FileHandler(f"logs/{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log", mode="w")
reader_formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(name)s %(message)s |'
    '%(filename)s:%(funcName)s:%(lineno)s | - %(name)s - | %(message)s'
)

logger = logging.getLogger()
logger.addHandler(handler)
logger.addHandler(reader_handler)

logger.setLevel(logging.DEBUG)
# for name in {"httpcore.connection", "httpx", "httpcore.http11"}:
#     temp_logger = logging.getLogger(name)
#     temp_logger.setLevel(logging.WARNING)

