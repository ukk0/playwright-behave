import os

HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
