# # String

# name = 'arafat'
# print(name)

# #string concatnation

# city = 'Kampala'
# country = 'Uganda'
# location = city + ', ' + country

# print(location)

# print('<============================>')

# #temperature converter

# fahrenheit = 32
# celsius = (fahrenheit - 32) * 5/9
# kelvin = (fahrenheit + 459.67) * 5/9

# print(celsius)
# print(kelvin)

# print('<============================>')


# #Grade Calculator

# student_score = 40
# max_score = 60
# percent = (student_score / max_score) * 100

# print(percent)

# print('<============================>')

# # Boolen

# age = 7

# if age <= 7:
#     print('You are getting a child discount')

# if age >= 65:
#     print('You are getting a senior discount')

# print('<============================>')

# # Boolean andvance

# temp = 120

# if temp <= 31:
#     print('It is freezing out side')
# elif temp >= 110:
#     print('It is way to hot outside')
# else:
#     print('Go for it. It is pretty nice')

# print('<============================>')

# #locical OR(|) and AND(&)

# is_vegan_one = True
# is_vegan_two = False 

# if is_vegan_one and is_vegan_two:
#     print('Offer only vegan dishes')
# elif is_vegan_one or is_vegan_two:
#     print('Offer at least some vegan options')
# else:
#     print('Offer anything on the menu')
    
# print('<============================>')

# # Arrays

# cars = ['Toyota', 'Subaru', 'Nissan', 'Kia']

# for car in cars:
#     print(car)

# x,y,z = 'Orange', 'Banana', 'Cherry'
# print(x)
# print(y)
# print(z)

# """
# Hello this is 
# a multi line
# comment
# """

# x = "awesome"

# def myfunc():
#     x = 'fantastic'
#     print('Python is ' + x)

# myfunc()

# print('Python is ' + x)

# x = 1j
# print(type(x))

# a = 'Hello, World'
# print(a[1])

# print(a[2:5])
# print(a[-5:-2])
# print(a.split())
# print(a.upper())
# print(a.lower())
# print(a.replace('H', 'Y'))

# f = open('sample.txt', 'r')
# # print(f.read(100))
# # print(f.readline())
# # for x in f: 
# #     print(x)
# f.close()

# Appending content to a file

f = open('demotext1.txt', 'a')
f.write('Now the file has more content!')
f.close()

# Open and read the file after the appending
f = open('demotext1.txt', 'r')
print(f.read())

# Overwriting the content of the text files

f = open('demotext1.txt', 'w')
f.write('Woops! I have deleted the content')
f.close()

# Open and read the file after the appending
f = open('demotext1.txt', 'r')
print(f.read())

# creating a new file

# f = open('mytext.txt', 'x')

# creating a file if it doesnt exist

f = open('mytext.txt', 'w')

import os
import shutil

path = r"C:\Users\Dev Arafat\Pictures"
os.chdir(path)
# print(path)
files = os.listdir()
print(files)


filepath = r"C:\Users\Dev Arafat\Desktop\file"
os.chdir(filepath)
# print(filepath)
images = os.listdir()
print(images)
# os.mkdir(filepath + "\\" + "file2")
# for image in os.listdir():
#     shutil.move(image, filepath + "\\" + "file2")

flpath = r"C:\Users\Dev Arafat\Desktop\file\file2"
os.chdir(flpath)
print(flpath)
fl = os.listdir()
print(fl)