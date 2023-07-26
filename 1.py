#first program
def goods(a,b,c):
       a,b,c=20,30,40
       x=input("Enter the product to buy:")
       y=input("enter the quantity:")
       if(x==a):
              print("product is allocated, and the price of the product is",x*y)
        
#second program
student={
        "name":"Piyush",
        "age":20,
        "major":"Computer Science"
    }
print("Name:",student["name"])
print("age:",student["age"])
print("Major:",student["major"])
student["age"]=21
print("Updated dictionary:",student)
#third program
fruit=[ 'apple','banana','orange','mango']
fruit.append('grape')
print(fruit)
fruit.remove('banana')
print(fruit)
print(len(fruit))
#fourth program
import numpy as np
arr=np.array([1,2,3,4,5])
squared=arr**2
print(squared)
mean=np.mean(arr)
print(mean)
arr2=np.random

with open("data.txt","r")as file:
    data=file.read()
processed_data=data.upper()
with open("processed_data.txt","w")as file:
    file.write(processed_data)
print("file processing completed.")