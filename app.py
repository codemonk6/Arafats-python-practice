age = 20
name = "fred"
amount = 1000
product = "shoe"
sentence = "Linux is my operating system"
sentence2 = "My operating system is Windows"
sentence3 = "I go to school everyday"


if sentence.startswith("Linux"):
    print("supported")
else:
    print("not supported")


if sentence2.endswith("Windows"):
    print("file supported")
else: 
    print("file not supported")

if "school" in sentence3:
    print("Student")
else:
    print('working class')

sentence4 = "Holla there"

#slice
print(sentence4[:5])

sentence5 = "Hello world"
print(sentence5[5:])

# lists
fruits = ['apple', 'mango', 'tomato']


# pushing
fruits.append('onion')
fruits.pop()

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    # even fruit
    if i % 2 == 0:
        print(fruit)


if age > 18:
    print("allowed to drive")
else:
    print("restricted")

# user input
