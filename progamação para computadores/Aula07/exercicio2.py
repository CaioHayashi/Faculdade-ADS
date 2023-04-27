import os
os.system('cls' if os.name == 'nt' else 'clear')

for num in range(100):
    if num <= 50:
        print(num)
    else:
        if num % 2 == 0:
            print(num)