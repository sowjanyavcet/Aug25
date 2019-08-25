mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
for x in mylist:
    print(x)
    
numbers=[]
strings=[]
names=['sa','bd','cs']
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_names=names[1]
print(numbers)
print(strings)
print("The second name on the names list is %s"%second_names) 


number=1+2*3/4.0
print(number)


remainder=11%3
print(remainder)

squared=7**2
cubed=2**3
print(squared)
print(cubed)

helloworld="hello"+""+"world"
print(helloworld)

lotsofhellos="hello"*10
print(lotsofhellos)

even_numbers=[2,4,6,8]
odd_numbers=[1,3,5,7]
add_numbers=odd_numbers+even_numbers
print(add_numbers)

print([1,2,3]*3)


#string
name="John"
print("%s"%name)

name="john"
age=35
print("%s is %d years old,"%(name,age))

name="john Deo"
print("Hello"+""+name+""+ "your current balance is $53.44")


data=("John","Doe",53.44)
format_string="Hello %s%s Your current balance is $%s."
print(format_string % data)
