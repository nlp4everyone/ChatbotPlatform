import time

from enum import Enum
class AlertType(Enum):
    LOWER = 0,
    UPPER = 1,
    BOTH = 2

def check_price_after_period(url:str,lower_threshold=0.7,upper_threshold=0.8,interval_in_seconds = 60):
    while True:

        # Check after second
        time.sleep(interval_in_seconds)