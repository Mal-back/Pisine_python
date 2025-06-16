import time
import datetime

timestamp = time.time()

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")

dt = datetime.datetime.fromtimestamp(timestamp)
print(dt.strftime("%b %d %Y"))
