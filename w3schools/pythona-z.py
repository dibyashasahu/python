print("\n\n**---*\t\t*---*\t\t*---**\n\n")
## Variable type show

a= 5
b= 3.5
c= 'This is dibyasha'
d=type(a)
e=type(b)
f=type(c)
print("%s is of  %s" %(a,d))
print("%s is of  %s" %(b,e))
print("%s is of  %s" %(c,f))

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("***multiline string***\n\n")

a="""I have always aimed to be a wealthy person
less in terms of money
and more in terms of heart."""

print("the multiline string is: \n", a)

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("***strings as arrays***\n\n")

a='dibyasha sahu'
print ("The fifth element is:", a[4])

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("*** string slicing***\n\n")

a= 'dibyasha sahu'
print(a[2:5])

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("***negative slicing***\n\n")

a= 'dibyasha sahu'
print(a[-11:-8])

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("***working with string***\n\n")

a= '    dibyasha sahu   '
print (a.strip())
print ("length of string after stripiing is: ",len(a))
b=(a.upper())
print(b)
c= (b.lower())
print(c)
print(a.replace(" ","."))

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("***string cncatenation***\n\n")
a='dibyasha'
b='age'
c=20
print("%s %s is %s" %( a, b, c))
#str=a+b+c
#print(str)
print("{} {} is {}". format(a,b,c))

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("***playing with strings***\n\n")
a="dibyasha sahu"
print(a.capitalize())
print(a.casefold())
print(a.center(45))
print("expandtabs",a.expandtabs(10))

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("***boolean***\n\n")
a="saroj"
print(bool(a))

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("***function***\n\n")

def my_function():
    return False
print(my_function())

def my_function1():
    g=5+3
    return g 

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("***function***\n\n")
print("my_function1:", my_function1())
print(bool(my_function1()))

print(10>8)

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("*** operator ***\n\n")
a1="saroj"
a2="dibyasha"
def compare(name1,name2):
    if len(name1)==len(name2):
        return True 
    else:
        return False 
# result=compare("dibyasha", "saroj")
# print("the result variable value is ",result)
print("Method only comarision 1: ", compare(a1,a2))
# print("Method only comarision 2: ", compare("Saroj","Dibyasha"))

class A:
    def compare(self, name1,name2):
        if len(name1)==len(name2):
            return True
        else:
            return False

obj=A()
a1= "dibyasha"
a2="saroj"
print ("method comparison:", obj.compare(a1,a2))

print("\n\n**---*\t\t*---*\t\t*---**\n\n")
print("*** class Demo ***\n\n")

class students:
    def __init__(self, name, address, marks):
        self.studentname=name
        self.studentaddress=address
        self.studentmark=marks
        
    def is_passed(self, marks):
        if marks>60:
            return True
        else:
            return False
x= students("dibyasha", "6747 ntley road",88)
y=students("saroj","8778 ghb road",6)
print("has the x student passed?", x.is_passed(x.studentmark))
print("has the y student passed?", y.is_passed(y.studentmark))





    

















