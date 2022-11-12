## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?

Python is knowns as general purpose language because can be use to for variety of development like Web application,backend, server side, Application, Automating stuff and can be used fir IOT.
Now coming to High Level Language , It is written in a a simple english statement which we humans can undersatnd but Machine  cannot, machine understand language whihc are at low level or Assebly Level. 

Q2. Why is Python called a dynamically typed language?

Python is called dynamically typed language because in python when we write any program or logic we do not need to define variable datatype, Be it string, Integer, List etc.
 # Assigning String in variable
 var1 = 'Hello'
 #Assigning Integer as Value
 var2 = 33
 #Assigning List as Value
 var3 =['i','Neuron']

Q3. List some pros and cons of Python programming language?

Pros: 
a)Easy to read/write English like syntax
b)Dynamically typed
c)Large community and many libraries

Cons.
a)Slow in executtion
b) Run time error
c)Not memory efficient

Q4. In what all domains can we use Python?

Python can be used in domain like:
a) Web Devlopment(Django)
b) Server Side(backend)
c) High Mathemetical computation stuff(Data Sceince/Analysis)
d)Automating stuff
e) Scripting

Q5. What are variable and how can we declare them?

Variable are the name given to a specific memory whihc holds/stores any value, So that user can in the program by reffering.
We can delacre any variable dynamically meaning we do not need to specify its datatype, but follow the variable naming convention.

Q6. How can we take an input from the user in Python? 

We need to use input() function to take inputs
# This we can take input but without prompt
var1 = input()
print(var1)

# This we can take input but with prompt
var1 = input('Enter the Value:')
print(var1)

Q7. What is the default datatype of the value that has been taken as an input using input() function?

By default whenver the input is taken using input() function , the default datatype is String.

Q8. What is type casting?

using Type casting  a datatype can be converted in different type.
Eg:

var1= input('Enter the Value:')
#var1 = 3 feeded from keyboard
print(type(var1)
#this will print the type class whihc will String in this case, Since the default input type is String
#not to type cast
var2 = int(var1)
print(type(var2))
#this will print type class as Integer

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

Yes, we can , we need to use split() fucntion to seprate the input as per defined seprator
#Taking input from user
num = input('Enter comma seprated value').split(',')
print(num)

Q10. What are keywords?

Keywords are the word which are predifined in a programming language, which cannot be used as variable.
eg:def,print,class,return

Q11. Can we use keywords as a variable? Support your answer with reason.

No the keywords cannot be used as variable, since keywords are predifined in language They hold some specific value.

Q12. What is indentation? What's the use of indentaion in Python?
Indentation signifies the starting of code line, Like in Python it indicates a block of code.
eg: for loop has it own loop
num = [1,2,3,4,5]
for i in num:
    print(i)


Q13. How can we throw some output in Python?

You can throw output using print() funtion and also as return if we are using fucntion in a program

Q14. What are operators in Python?

Operator are used to do some calculation on operands(variable).
eg print(a + b)
Here a,b are operand and + is operator.
Like this we have different type of operator.
Arithmentic operator: +,-,*,/
Comparison Operator: ==,!=,>,<,>=,<=
Logical operator: AND, OR, NOT
Assignment operator: =,+=,-=
Membership Operator: in, not in

Q15. What is difference between / and // operators?

/ operator is Division operator and //  operator is floor division

x = 18
y = 2
print(x / y)

Ouput will be 9.0

x = 9
y = 2
print(x // y)
Ouput will be 4, it return nearest whole value

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
# Declaring and intialising the variable with string value
string_var='iNeuron'
#Multiplying and printing the string variable that 4 times
print(string_var*4)

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

#Taking input from user
num = int(input("Please enter your number: "))
#checking if number is even or Odd
if (num%2==0):
    print(num,'is even')
else:
    print(num,'is Odd')

Q18. What are boolean operator?

AND,OR and NOT are the Boolean operator, whihc always returns True or False as final result.

Q19. What will the output of the following?
```
1 or 0 ==> 1

0 and 0 ==> 0

True and False and True ==> False

1 or 0 or 0 ==> 1
```

Q20. What are conditional statements in Python?

Conditional statements are something which allows program to hanlde or execute certain fucntion/operation based certain scenarios and this can be acheived with 
coditional statement.
in Python we have if, elif and else conditional statement

Q21. What is use of 'if', 'elif' and 'else' keywords?

The 'if', 'elif' and 'else' keywords are used to perform some desired operation on some defined scenarios
eg:
# Taking three inputs with prompts
num1= input('Enter 1st number: ')
num2= input('Enter 2nd number: ')
num3= input('Enter 3rd number: ')
# comparing if num1 is greatest of other two number 
if num1> num2:
    if num1 > num3:
        print('Greater number is num1: ',num1)
# comparing if num2 is greatest of 3rd number 
elif num2>num3:
    print('Greater number is num2: ',num2)
# Since none of the above two number are greatest and control came to else part 3rd number is greatest
else:
    print('Greater number is num3: ',num3)
	
	
Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

#Taking input age from user
age= int(input("Please enter your age: "))
#checking if user age is 18 or above
if (age>=18):
    print('I can vote')
else:
    print('I can\'t vote')

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
 # declared the list
numbers = [12, 75, 150, 180, 145, 525, 50] 
 # declared the variable and initialise it with 0
total_even_sum=0

#running for a loop to go by each element
for i in numbers:    
    if(i%2==0):#checking if element is perfectly divisible vy 2 for even number
       total_even_sum+=i
#printing the total sum of even numbers from the list
print(total_even_sum)

##Answer is total_even_sum=392


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

# Taking three inputs with prompts
num1= input('Enter 1st number: ')
num2= input('Enter 2nd number: ')
num3= input('Enter 3rd number: ')
# comparing if num1 is greatest of other two number 
if num1> num2:
    if num1 > num3:
        print('Greater number is num1: ',num1)
# comparing if num2 is greatest of 3rd number 
elif num2>num3:
    print('Greater number is num2: ',num2)
# Since none of the above two number are greatest and control came to else part 3rd numb is greatest
else:
    print('Greater number is num3: ',num3)


Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]


Program is below

numbers = [12, 75, 150, 180, 145, 525, 50]

#running for a loop to go by each element
for i in numbers:    
    if(i>500):#checking if element is greater than 500 if True the break the loop else continue
       break
    elif (i>150): #skipping the value if greater than 150
        continue 
    else:
        if(i%5==0): #checking if element is divsible by 5
            print(i)

## Answer is 75,145,150
