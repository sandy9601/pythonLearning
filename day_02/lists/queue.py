# FIFO first in first out 

from collections import deque

places = deque(["ap","tg","ts","del"])
places.append("ker")
print(places.popleft())


