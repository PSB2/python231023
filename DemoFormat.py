# DemoFormat.py

for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("-------오른쪽 정렬---------")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("-------0을 정렬---------")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(5))