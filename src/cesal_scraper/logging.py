import logging
import logging.config

import colorlog

from .settings import DEBUG


def setup_logging() -> None:
    """Setups the logging configuration for the application."""
    log_level = logging.DEBUG if DEBUG else logging.INFO
    log_file = "temp/cesal-scraper.log"

    # Define the format for file handler
    file_formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Define the format for stream handler with color
    color_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={"DEBUG": "cyan", "INFO": "green", "WARNING": "yellow", "ERROR": "red", "CRITICAL": "bold_red"},
    )

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(file_formatter)

    # Stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(color_formatter)

    # Configure the root logger
    logging.basicConfig(level=log_level, handlers=[file_handler, stream_handler])
