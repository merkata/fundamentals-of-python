1. Will the following lines of code print the same thing? Explain why or why not.
x = 6
print(6)
print("6")

First line binds the value 6 (integer) to variable x;
Second prints the integer 6
Third prints the string "6"

2. Will the following lines of code print the same thing? Explain why or why not.
x = 7
print(x)
print("x")

Second line will print the content of variable x, which is 7, third line will just output "x", the string

3. What is the largest floating-point value available on your system?

```
In [1]: import sys

In [2]: sys.float_info.max
Out[2]: 1.7976931348623157e+308
```

4. What is the smallest floating-point value available on your system?

```
In [1]: import sys

In [2]: sys.float_info.min
Out[2]: 2.2250738585072014e-308
```

5. What happens if you attempt to use a variable within a program, and that variable has not been
assigned a value?

We'd get a NameError
```
In [4]: print(no_such_variable)
--------------------------------------------------------
NameError              Traceback (most recent call last)
<ipython-input-4-2ada54d5acff> in <module>()
----> 1 print(no_such_variable)

NameError: name 'no_such_variable' is not defined
```

6. What is wrong with the following statement that attempts to assign the value ten to variable x?
10 = x

You cannot assign a variable to a static value, "=" is assignment, not equality test such as in maths

7. Once a variable has been properly assigned can its value be changed?

It can, variables are mutable in Python and can point to new values

8. In Python can you assign more than one variable in a single statement?

You can
```
In [5]: a, b, c = 1, 2, 3

In [6]: print('{0} {1} {2}'.format(a, b, c))

1 2 3
```

9. Classify each of the following as either a legal or illegal Python identifier:
(a) fred
legal
(b) if
illegal - uses a reserved word
(c) 2x
illegal, cannot start with number
(d) -4
illegal - is a static value (negative integer)
(e) sum\_total
legal
(f) sumTotal
legal, though camelCase is not preferred in Python
(g) sum-total
illegal, cannot contain "-"
(h) sum total
illegal, " " is a separator, cannot be part of variable name
(i) sumtotal
legal
(j) While
legal, though confusing (lower-case while is a reserved word)
(k) x2
legal
(l) Private
legal, though confusing (lower-case private is a reserved word)
(m) public
legal
(n) $16
illegal, cannot start with a special symbol
(o) xTwo
legal, though camelCase
(p) _static
legal
(q) _4
legal
(r) ___
legal
(s) 10%
illegal, starts with digit
(t) a27834
legal
(u) wilma's
illegal, uses special char "'"

10. What can you do if a variable name you would like to use is the same as a reserved word?

Option 1: rethink why I would do that and name it something else
Option 2: put a "_" before it
Option 3: use an upper case version of it

11. How is the value 2.45×10−5expressed as a Python literal?

2.45e-05

12. How can you express the literal value 0.0000000000000000000000000449 as a much more compact Python literal?

```
In [49]: val1 = 0.0000000000000000000000000449

In [50]: val2 = 0.449e-25

In [51]: val1 == val2
Out[51]: True
```

13. How can you express the literal value 56992341200000000000000000000000000000 as a much more
compact Python literal?

```
In [157]: val3
Out[157]: 56992341200000000000000000000000000000

In [158]: val4 = 569923412*10**29

In [159]: val3 == val4
Out[159]: True
```

14. Can a Python programmer do anything to ensure that a variable’s value can never be changed after its initial assignment?

No

15. Is "i" a string literal or variable?

It's a string literal due to it being enclosed in quotes

16. What is the difference between the following two strings? 'n' and '\n'?

'n' is just the strin "n" while "\n" is a special character meaning end of line

17. Write a Python program containing exactly one print statement that produces the following output:
A
B
C
D
E
F

```
In [73]: my17_op1 = "A\nB\nC\nD\nE\nF"

In [74]: my17_op2 = """
    ...: A
    ...: B
    ...: C
    ...: D
    ...: E
    ...: F
    ...: """

In [75]: print(my17_op1)
A
B
C
D
E
F

In [76]: print(my17_op2)

A
B
C
D
E
F

```

18. Write a Python program that simply emits a beep sound when run.

print("\b")

