size = int(input("Input number: "))

for string in range(size, 0, -1):
    for triangle in range(string, 0, -1):
        print(triangle, end=" ")
    print("\n")