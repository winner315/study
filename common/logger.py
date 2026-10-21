import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

# 日志文件：定位到 项目根(logger.py 的上一级) 下的 log/test.log
LOG_FILE = Path(__file__).parent.parent / "log" / "test.log"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)  # 目录不存在就自动创建


def get_logger(name="test"):
    """获取一个公共 logger：同时输出到控制台和文件，按天滚动。

    - 同一个 name 返回同一个 logger（不会重复加 handler）
    - 来源用 %(module)s + %(lineno)d 自动记录，无需手动传 name
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:  # 防止重复添加 handler
        fmt = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s"
        )

        # handler①：控制台
        console = logging.StreamHandler()
        console.setFormatter(fmt)
        logger.addHandler(console)

        # handler②：文件（每天零点切分，保留最近 7 天）
        file_handler = TimedRotatingFileHandler(
            LOG_FILE, when="midnight", backupCount=7, encoding="utf-8"
        )
        file_handler.setFormatter(fmt)
        logger.addHandler(file_handler)

    return logger
