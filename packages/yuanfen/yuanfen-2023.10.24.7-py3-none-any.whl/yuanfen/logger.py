import logging
import os
from logging.handlers import TimedRotatingFileHandler


class Logger:
    def __init__(self, name=None, level=logging.INFO):
        os.makedirs("logs", exist_ok=True)
        logger_name_fmt = " [%(name)s]" if name else ""
        log_formatter = logging.Formatter(f"%(asctime)s [%(levelname)-7s]{logger_name_fmt} %(message)s")

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(log_formatter)

        self.file_handler = TimedRotatingFileHandler(
            "logs/log",
            when="midnight",
            backupCount=365,
            encoding="utf-8",
        )
        self.file_handler.suffix = "%Y-%m-%d.log"
        self.file_handler.setFormatter(log_formatter)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.file_handler)

    def debug(self, msg):
        self.logger.debug(f"{msg}")

    def info(self, msg):
        self.logger.info(f"{msg}")

    def warn(self, msg):
        self.logger.warning(f"{msg}")

    def error(self, msg):
        self.logger.error(f"{msg}")
