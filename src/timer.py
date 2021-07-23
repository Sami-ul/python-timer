from time import time

timer_length = input(
    "How many minutes and seconds, enter as minutes seconds, enter 0 if no time in that section, do not use commas: ").split()

timer_length = list(map(float, timer_length))


def conv_seconds(minutes) -> float:
    return minutes * 60


total_seconds = conv_seconds(timer_length[0]) + timer_length[1]

input("Press enter to start: ")

time1 = time()
while time() - time1 < total_seconds:
    print(round(time() - time1, 2), end="\r")

print("\nDone")
