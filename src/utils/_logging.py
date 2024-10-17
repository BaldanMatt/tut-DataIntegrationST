import logging

class ColoredFormatter(logging.Formatter):
    # ANSI escape codes for coloring
    COLORS = {
        'DEBUG': '\033[94m',   # Blue
        'INFO': '\033[92m',    # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'CRITICAL': '\033[41m'  # Red background
    }
    RESET = '\033[0m'  # Reset to default color

    # You can customize the log message format here
    DEFAULT_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, fmt=None, datefmt=None, style=None):
        # Call the base class constructor with the format string
        super().__init__(fmt=fmt or self.DEFAULT_FORMAT, datefmt=datefmt or self.DATE_FORMAT, style=style)

    def format(self, record):
        # Get the color code based on the log level
        color = self.COLORS.get(record.levelname, self.RESET)
        record.levelname = f"{color}{record.levelname}{self.RESET}"
        return super().format(record)


def factory(fmt=None, datefmt=None, style=None):
    # Create the ColoredFormatter with the provided fmt and datefmt
    return ColoredFormatter(fmt, datefmt, style)