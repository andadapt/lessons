[drag=100, drop=center, flow=col]

## Starter

How many variables are there in the code below:


```basic
TextWindow.WriteLine("What is your name?")
name = TextWindow.Read()
TextWindow.WriteLine("How old are you?")
age = TextWindow.Read()
dogAge = age * 7
```

What are the symbols in small basic for:
@ol
- Addition
- Multiplication
- Divide
@ol



---
[drag=100, drop=center, flow=col]
## Small Basic - Lesson 5 
## Selection
@ol
**ASPIRE to:**

- Demonstrate the use of selection with multiple conditions
**CHALLENGE to:**

- Demonstrate the use of selection with a single condition
@ol
---
[drag=100, drop=center, flow=col]

## What is Selection?

Selection allows you to check something and then do something depending on the result.

In programming this is done by using an IF statement.

The example to the right shows how an IF statement works.

```basic
numberToGuess = 9
TextWindow.WriteLine(“Enter a number:”)
guess = TextWindow.Read()
If guess = numberToGuess Then
  TextWindow.WriteLine(“You guessed the number”)
Else
  TextWindow.WriteLine(“You guessed wrong!”)
EndIf
```


---
[drag=100, drop=center, flow=col]
## Task

Try to complete:

Task 1 - Are You Old?

Use the code to create the program so it works like the example shown.

## Done? 
Screenshot your code and add it to your programming diary


  
REMEMBER:
If CONDITION Then
   DO IF CONDITION IS TRUE
Else
   DO IF CONDITION IS FALSE
EndIf
---  
[drag=100, drop=center, flow=col]
### Multiple Conditions

Sometimes you may want to check more than one condition in a program.
@ol
- For example:
- “If the guess isn’t the correct number,  check whether their guess is higher or lower than the number they are trying to guess to give them a clue”
- If you want to make more than one check, you can use ElseIf, look at the example to the right.
@ol

```basic
numberToGuess = 9
TextWindow.WriteLine(“Enter a number:”)
guess = TextWindow.Read()
If guess = numberToGuess Then
  TextWindow.WriteLine(“You guessed the number”)
ElseIf guess > numberToGuess Then
  TextWindow.WriteLine(“Your guess was too high!”)
Else
  TextWindow.WriteLine(“Your guess was too low!”)
EndIf
```
---
[drag=100, drop=center, flow=col]
## Task

Try to complete:

Task 2 - Are You a Teenager?

Use the code from the program you have just made to change your program so that:
- If they are over 19 it says they are old
- If they are over 12 and less than 20 it says they are a teenager
- If they are below 13 it says hey there youngster!

## Done? 
Screenshot your code and add it to your programming diary


  
REMEMBER:
If CONDITION1 Then
   DO IF CONDITION1 IS TRUE
ElseIf CONDITION2 Then
   DO IF CONDITION2 IS TRUE
Else
   DO IF BOTH CONDITIONS ARE FALSE
EndIf
  
---
[drag=100,drop=center, flow=col]

![](assets/img/year8/task2.gif)
---
[drag=100, drop=center, flow=col]

## Progress Check
  
On your mini-whiteboards answer the following questions:

What would the program display if number was:
- 35
- 20
- 14


```basic
If number > 20 Then
  number = number + 10
Else
  number = number - 10
EndIf
TextWindow.WriteLine(number)
```
---
[drag=100, drop=center, flow=col]

## Progress Check

  
On your mini-whiteboards answer the following questions:

What would the program display if number was:
- 14
- 24
- 6

```basic    
If number > 20 Then
  number = number + 10
ElseIf number > 10 Then
  number = number * 10
Else
  number = number - 5
EndIf
TextWindow.WriteLine(number)
```


---

[drag=100, drop=center, flow=col]
## Task  

Try to complete Task 3 - Planet Quiz

Use the success criteria to create a program to ask five different questions about the planets.

## Done? 
Screenshot your program and add it to your programming diary. Then try to complete extensions for the task.



---
[drag=100, drop=center, flow=col]
## Plenary

Open: Selection Plenary

Read the program and replace the comments with the Small Basic code, see the example to the right.

HINT: Look at some of the code that is already in the program to help you.
Plenary

Simon - insert picture 

SN- You could peer-assess this using Q&A with students



