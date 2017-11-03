1. Is the literal 4 a valid Python expression?

Yes, it's an example of a simple expression

2. Is the variable x a valid Python expression?

Yes, this also is an example of a simple expression

3. Is x + 4 a valid Python expression?

It is a valid expression, provided that x has been defined before this expression

4. What affect does the unary + operator have when applied to a numeric expression?

It adds two values together (two values) or denotes a positive number (one value)

5. Sort the following binary operators in order of high to low precedence: +, -, *, //, /, %, =.

Found in the docs - https://docs.python.org/3/reference/expressions.html, 6.16 Operator precedence

/, //, %, *
+, -
=

6. Given the following assignment:
x = 2
Indicate what each of the following Python statements would print.
(a) print("x")
outputs "x"
(b) print('x')
outputs "x"
(c) print(x)
outputs 2
(d) print("x + 1")
outputs "x + 1"
(e) print('x' + 1)
TypeError, expression fails
(f) print(x + 1)
outputs 3

```

In [1]: x = 2

In [2]: print("x")
x

In [3]: print('x')
x

In [4]: print(x)
2

In [5]: print("x + 1")
x + 1

In [6]: print('x' + 1)
--------------------------------------------------------
TypeError              Traceback (most recent call last)
<ipython-input-6-b168880bea75> in <module>()
----> 1 print('x' + 1)

TypeError: must be str, not int

In [7]: print(x + 1)
3

```

7. Given the following assignments:
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5
Evaluate each of the following Python expressions.
(a) i1 + i2
(b) i1 / i2
(c) i1 // i2
(d) i2 / i1
(e) i2 // i1
(f) i1 * i3
(g) d1 + d2
(h) d1 / d2
(i) d2 / d1
(j) d3 * d1
(k) d1 + i2
(l) i1 / d2
(m) d2 / i1
(n) i2 / d1
(o) i1/i2*d1
(p) d1*i1/i2
(q) d1/d2*i1
(r) i1*d1/d2
(s) i2/i1*d1
(t) d1*i2/i1
(u) d2/d1*i1
(v) i1*d2/d1

unittest program exercise_3_7.py present

8. What is printed by the following statement:
print(5/3)

outputs a float
```
In [8]: print(5/3)
1.6666666666666667
```

9. Given the following assignments:
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5
Evaluate each of the following Python expressions.
(a) i1 + (i2 * i3)
(b) i1 * (i2 + i3)
(c) i1 / (i2 + i3)
(d) i1 // (i2 + i3)
(e) i1 / i2 + i3
(f) i1 // i2 + i3
(g) 3 + 4 + 5 / 3
(h) 3 + 4 + 5 // 3
(i) (3 + 4 + 5) / 3
(j) (3 + 4 + 5) // 3
(k) d1 + (d2 * d3)
(l) d1 + d2 * d3
(m) d1 / d2 - d3
(n) d1 / (d2 - d3)
(o) d1 + d2 + d3 / 3
(p) (d1 + d2 + d3) / 3
(q) d1 + d2 + (d3 / 3)
(r) 3 * (d1 + d2) * (d1 - d3)

```

In [1]: i1, i2, i3 = 2, 5, -3

In [2]: d1, d2, d3 = 2.0, 5.0, -0.5

In [3]: i1 + (i2 * i3)
Out[3]: -13

In [4]: i1 * (i2 + i3)
Out[4]: 4

In [5]: i1 / (i2 + i3)
Out[5]: 1.0

In [6]: i1 // (i2 + i3)
Out[6]: 1

In [7]: i1 / i2 + i3
Out[7]: -2.6

In [8]: i1 // i2 + i3
Out[8]: -3

In [9]: 3 + 4 + 5 / 3
Out[9]: 8.666666666666666

In [10]: 3 + 4 + 5 // 3
Out[10]: 8

In [11]: (3 + 4 + 5) / 3
Out[11]: 4.0

In [12]: (3 + 4 + 5) // 3
Out[12]: 4

In [13]: d1 + (d2 * d3)
Out[13]: -0.5

In [14]: d1 + d2 * d3
Out[14]: -0.5

In [15]: d1 / d2 - d3
Out[15]: 0.9

In [16]: d1 / (d2 - d3)
Out[16]: 0.36363636363636365

In [17]: d1 + d2 + d3 / 3
Out[17]: 6.833333333333333

In [18]: (d1 + d2 +d3) / 3
Out[18]: 2.1666666666666665

In [19]: d1 + d2 + (d3 / 3)
Out[19]: 6.833333333333333

In [20]: 3 * (d1 + d2) * (d1 - d3)
Out[20]: 52.5

```

10. What symbol signifies the beginning of a comment in Python?

The pound - "#"

11. How do Python comments end?

With a new line

12. Which is better, too many comments or too few comments?

The right amount of comments, avoiding code smell through comments

13. What is the purpose of comments?

To document the source code for you and your fellow colleagues

14. Why is human readability such an important consideration?

Because programmers are (mostly) human

15. What circumstances can cause each of the following run-time errors to arise?
• NameError
print(nonexistent)
• ValueError
int('two')
• ZeroDivisionError
5 / 0
• IndentationError
def test():
print("Won't work")
• OverflowError
2231.012e12**1.510000e10
• SyntaxError
print "Hi"
• TypeError
'two' / 'three'
Hint: Try some of following activities in the interpreter or within a Python program:
• print a variable that has not been assigned
• convert the string 'two' to an integer
• add an integer to a string
• assign to a variable named end-point
• experiment adding spaces and tabs at various places in the code of an error-free Python program
• compute raise a floating-point number to a large power, as in 1.510,000.

16. Consider the following program which contains some errors. You may assume that the comments
within the program accurately describe the program’s intended behavior.
```
#Get two numbers from the user
n1 = float(input())# 1
OK
n2 = float(input())# 2
OK
#Compute sum of the two numbers
print(n1 + n2)# 3
OK
#Compute average of the two numbers
print(n1+n2/2)# 4
logic error - operator precedence
#Assign some variables
d1 = d2 = 0# 5
#Compute a quotient
print(n1/d1)# 6
run-time error - division by zero
#Compute a product
n1*n2 = d1# 7
interpreter error
#Print result
print(d1)# 8
logic error - result from step 7 is never computed
```

```
In [24]: n1 = float(input())
2

In [25]: n2 = float(input())
3

In [26]: print(n1 + n2)
5.0

In [27]: print(n1 + n2/2)
3.5

In [28]: d1 = d2 = 0

In [29]: print(n1 / d1)
--------------------------------------------------------
ZeroDivisionError      Traceback (most recent call last)
<ipython-input-29-2ecde77847a4> in <module>()
----> 1 print(n1 / d1)

ZeroDivisionError: float division by zero

In [30]: n1 * n2 = d1
  File "<ipython-input-30-392715a488c9>", line 1
    n1 * n2 = d1
                ^
SyntaxError: can't assign to operator


In [31]: print(d1)
0
```

For each line listed in the comments, indicate whether or not an interpreter error, run-time exception,
or logic error is present. Not all lines contain an error.

17. Write the shortest way to express each of the following statements.
(a) x = x + 1
x += 1
(b) x = x / 2
x /= 2
(c) x = x - 1
x -= 1
(d) x = x + y
x += y
(e) x = x - (y + 7)
x -= y + 7
(f) x = 2*x
x *= 2
(g) number\_of\_closed\_cases = number\_of\_closed\_cases + 2*ncc
number_of_closed_cases += 2 * ncc

```
In [9]: x = 1

In [10]: x += 1

In [11]: x /= 2

In [12]: x -= 1

In [13]: y = 1

In [14]: x += y

In [15]: x -= y + 7

In [16]: x *= 2

In [17]: x
Out[17]: -14.0
```

18. What is printed by the following code fragment?
x1 = 2
x2 = 2
x1 += 1
x2 -= 1
print(x1)
print(x2)
Why does the output appear as it does?

Code is short for
x1 = x1 + 1 #increment by 1
x2 = x2 - 1 #decrement by 1

19. Consider the following program that attempts to compute the circumference of a circle given the
radius entered by the user. Given a circle’s radius, r, the circle’s circumference, C is given by the
formula:
C = 2πr
r = 0
PI = 3.14159
#Formula for the area of a circle given its radius
C = 2*PI*r
#Get the radius from the user
r = float(input("Please enter the circle's radius: "))
#Print the circumference
print("Circumference is", C)
(a) The program does not produce the intended result. Why?

It computes the value with r=0 before we get to the input from the user

(b) How can it be repaired so that it works correctly?

We need to calculate the value of C with an r from the user, so the calculation must be after user input

20. Write a Python program that ...
tbd
21. Write a Python program that ...
tbd
