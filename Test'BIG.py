nums = [23 , 17 , 52 , 78 , 62 , 70]
max = nums[0]
for n in nums:
    if n > max:
        max = n

min = nums[0]
for n in nums:
    if n < min:
        min = n

print ("max value = ", max)
print (type(max))
print ("min value = ", min)
print (type(min))


a = 37
b = 27
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a // b)
print (a % b)
print (4**6)
print (a ** b)