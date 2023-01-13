import sys


def input():
    return sys.stdin.readline()[:-1]


N = input()

zero_count = 0
for i in reversed(N):
    if i == "0":
        zero_count += 1
    else:
        break

kaibun_before = "0" * zero_count + N
kaibun_after = "".join(list(reversed(kaibun_before)))

if kaibun_before == kaibun_after:
    print("Yes")
else:
    print("No")
