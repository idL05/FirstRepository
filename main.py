list = []
def add_info(num):
    list.append(num)
    print(list)

while True:
    num = int(input("Enter value: "))
    add_info(num)