a = 4
b = 6.72
c = "AuJeedJad.com"

print(a)
print(b)
print (c)
print (a+b)




a,b,c = 2 , 4 , 6
x = y = z = 12
print ("a = " , a)
print ("b = " , b)
print ("c = " , c)
print ("x = " , x)
print ("y = " , y)
print ("z = " , z)




a = 7
b = 3
c = a + b
d = a / b

print ('a = %d' % a)
print ('b = %d' % b)
print ('c = %d' % c)
print ('d = %f' % d)




speed = 36.42
pi = 27 / 7
height = 2.31E5
length = 1.3E-3

print ('speed = %f' % speed)
print ('pi = %f' % pi)
print ('height = %f' % height)
print ('length = %f' % length)
print ('pi = %f' % pi)





name = "Surachai'JeedJad"
country = "Thai'land\"JeedJads"
language = 'Python'
interest = 'Ram\'21'

print ("Surachai'JeedJad")
print ("Thai'land\"JeedJads")
print ('Py\'thon')
print ('Ram\'21')




surachai1 = "What's your name?"
surachai2 = 'I\'m Surachai\"Srisawang\".'
surachai3 = "He said \"I would learn Python first\"."
surachai4 = 'His teach replied "Oh well!"'
print (surachai1)
print (surachai2)
print (surachai3)
print (surachai4)




site = 'aujeedjad' + '.co' + '.th'
tutorial = "Python" "Language" "\"Ram21\""
print(site)
print(tutorial)
print ('aujeedjad' + '.co' + '.th')
print ("Python" " Language" " \'Ram21\'")





numbers = [1, 2, 4, 6, 8, 19]
names = ["Mateo", "Danny", "James", "Thomas", "Luke"]
mixed = [-2, 5, 84.2, "Mountain", "Python"]

print(numbers)
print(names)
print(mixed)

for n in numbers:
    print(n)
print()

for n in names:
    print(n)
print()

for n in mixed:
    print(n)
print()





languages = ["C", "C++", "Java", "Python", "PHP"]

print("Index at 0 = ", languages[4])
print("Index at 3 = ", languages[3])
languages[0] = "Scalar"
print("Index at 0 = ", languages[0])





import sys

a = 8
b = 13.4
c = "Python"
d = [1, 2, 3, 4]

print('Size of a = ', sys.getsizeof(a))
print('Type of a = ', type(a))

print('Size of b = ', sys.getsizeof(b))
print('Type of b = ', type(b))

print('Size of c = ', sys.getsizeof(c))
print('Type of c = ', type(c))

print('Size of d = ', sys.getsizeof(d))
print('Type of d = ', type(d))

del a
del b, c, d

if 'a' in locals():
    print("a is exist")
else:
    print("a is not exist")
