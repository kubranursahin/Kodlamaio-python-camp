myList = ["Laptop", "Phone", "TV"]
print(myList)
myList.append("Mouse")
print(myList)
number = int(input("Faktoriyel : "))
factorial = 1
if number<0:
    print("Girilen sayı negatif!")
elif number == 0:
    print("Sonuç = 1")
else:
    for i in range(1, number+1):
        factorial = factorial*i
    print("Sonuç : ", factorial)