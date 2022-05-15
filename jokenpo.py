from time import sleep

for cx in range(11, 0, -1):
    sleep(1)
    print(cx-1)
sleep(1)
print('\033[31mBUM! BUMBUM! BUM!\033[m')