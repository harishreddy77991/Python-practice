# for loop

# for i in range(1,101):
#     print (i)
#     print("------------")

# for i in ("Harish"):
#     print (i)

# li=[1,2,3,4,5]
# for i in  (li):
#     print (i)

# or

# li=[1,2,3,4,5]
# for i in range (len(li)):
#     print (li[i])

# while loop

# x=8
# while x<=10:
#     print(x)
#     x+=1

# range(starting,ending,step)

# num=int(input("Enter table :"))
# for i in range(1,11,1):
#     print(f"{num}*{i}={num*i}")



# for i in range(2,20):
#     for j in range(1,11):
#         print (f"{i}*{j}={i*j}")
#     print ("--------------")


# num=int(input("enter number:"))
# if num %2==0:
#     print("even number")
# else:
#     print("odd number")


# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, 5  + 1):  # Outer loop for rows
#     for j in range(5  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         print("*", end=" ")
#     print()

# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows ,0 ,- 1):  # Outer loop for rows
#     for j in range(5  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         print("*", end=" ")
#     print()

# def valid_password(pwd):
#     if len(pwd) < 8:
#         return False 
#     has_degital=any(c.isdigit() for c in pwd)
#     has_upper=any(c.isupper() for c in pwd)
#     return has_degital and has_upper

# print(valid_password("Hari@12"))
# print(valid_password("Haris@123"))


# def greet(name="Guest"):
#     print("Hello", name)

# greet()
# greet("Ravi")


# def calc(a, b):
#     return a+b, a-b

# sum_val, sub_val = calc(10, 5)
# print(sum_val, sub_val)


# def student(name, age):
#     print(name, age)

# student(age=22, name="Harish")



# class Human:
#     def __init__(self,n,o):
#         self.name=n
#         self.occupation=o
#     def do_work(self):
#         if self.occupation=="Cricket Player":
#             print (self.name,"Plays Cricket")
#         elif self.occupation=="Actor":
#             print (self.name,"Shootes a film")
    
#     def Speaks (self):
#         print (self.name,"How are you?")

# Hari=Human("Harish","Actor")
# Hari.do_work()
# Hari.Speaks()

# Sree=Human("Sreenu","Cricket Player")
# Sree.do_work()
# Sree.Speaks()



# class person:
#     pass
# p1=person()
# p1.Name="Harish"
# p1.age=25

# print(p1.Name)
# print(p1.age)


# class person:
#     def __init__(self,Name,Age=25):
#         self.Name=Name
#         self.age=Age
        
# p1=person("Harish")
# p2=person("Sreenu",28)

# print(p1.Name,p1.age)
# print(p2.Name,p1.age)

# cust_name="Harish"
# cust_email="harish@gmail.com"
# age=25
# cust_order=[]

# def add_order(order_details):
#     pass 

# def Calculate_total():
#     pass 

# class Customer:
#     def __init__(self):
#         pass

#     def add_order(order_details):
#      pass

# def Calculate_total():
#     pass 

# cust1=Customer("Harish","harish@gmail.com")
# cus2=Customer("sreenu","sreenu@gmail.com")
# cust3=Customer("vamsi","vamsi@gmail.com") 

# git changes
# fecvfrvrf
