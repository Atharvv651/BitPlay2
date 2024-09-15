size = int(input("Enter the size of the array: "))

array = list()

for i in range(size):
    array.append(int(input(f"Enter Element {i+1}: ")))

xor_of_2 = array[0]
x = 0
y = 0
set_bit = 0

for i in range(1, size):
    xor_of_2 = xor_of_2 ^ array[i]
    set_bit = xor_of_2 & ~(xor_of_2 - 1)

for i in range(size):
    if array[i] & set_bit != 0:
        x = x ^ array[i]
    else:
        y = y ^ array[i]

print(f"The two odd occuring elements are {x} and {y}")