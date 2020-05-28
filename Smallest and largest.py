largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done": break
    try:
        num1 = int(num)
    except:
        print('Invalid Input')
        continue
    if num1 > largest:
        largest = num1
    if smallest is None:
        smallest = num1
    elif num1 < smallest:
        smallest = num1
print("Maximum", largest)
print("Minimum", smallest)
