import os

from utils.helpers import str_to_bool

BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = str_to_bool(os.getenv("HEADLESS", True))
SLOW_MO = os.getenv("SLOW_MO", 0)
