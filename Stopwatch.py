#This is a stopwatch python program.

import time
Time = int(input("Enter the time in seconds: "))

for x in range(Time, 0, -1):
    second = x % 60
    minute = x // 60
    print(f"{minute:02}:{second:02}")
    time.sleep(1)

print("Time is up!")