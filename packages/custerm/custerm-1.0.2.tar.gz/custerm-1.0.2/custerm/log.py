import logging
from dataclasses import dataclass, field

@dataclass
class LoggerConfig:
    log_level: int = logging.DEBUG
    log_file: str = "my_library.log"

@dataclass
class LogLevel:
    DEBUG: int = logging.DEBUG
    INFO: int = logging.INFO
    WARNING: int = logging.WARNING
    ERROR: int = logging.ERROR
    SUCCESS: int = 25  

class CustomLogger:
    def __init__(self, config: LoggerConfig):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(config.log_level)

        file_handler = logging.FileHandler(config.log_file)
        file_handler.setLevel(config.log_level)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    @classmethod
    def create_logger(cls, config: LoggerConfig):
        return cls(config)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_success(self, message):
        self.logger.log(LogLevel.SUCCESS, message)

    def log(self, message, level=logging.INFO):
        if isinstance(level, int):
            self.logger.log(level, message)
        else:
            self.logger.warning(f"Invalid log level '{level}' - Logging as INFO")
            self.logger.info(message)

    @staticmethod
    def set_log_level(level):
        if level in LogLevel.__dict__.values():
            logging.getLogger(__name__).setLevel(level)
        else:
            logging.getLogger(__name__).warning("Invalid log level. Using default level (DEBUG).")

    @property
    def available_log_levels(self):
        return LogLevel.__dict__
