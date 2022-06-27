#Loop Method
for i in range(1, 101): #Loops through a number range between 1 and 100
    if i % 3 == 0 and i % 5 == 0: #Finds numbers that are divisibe by 3 and 5 with no remainder 
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz') #Finds numbers that are divisibe by 3 with no remainder 
    elif i % 5 == 0:
        print('Buzz') #Finds numbers that are divisibe by 5 with no remainder 
    else: #What ever is left
        print(i)

#List Comprehension Method 
listMethod = ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else ('Fizz' if i % 3 == 0 else ('Buzz' if i % 5 == 0 else i)) for i in range(1, 101) if i % 3 == 0 or i % 5 == 0 ] #Nested if statements to get around the requirement

for i in listMethod:
    print(i)