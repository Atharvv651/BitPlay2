length = int(input("Enter Array Size: "))

array = []
for i in range(length):
    array.append(int(input(f"Enter Element Number {i+1}: ")))

odd = 0
for element in array:
    odd = odd ^ element

print(f"The Odd Occuring is {odd}")