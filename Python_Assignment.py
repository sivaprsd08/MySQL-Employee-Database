Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:\Users\kpe00\Desktop\Python_assignment_1.py ============
Enter your Name: Zara
Hello Zara
Hello Zara, welcome to Python programming
>>> result
'Hello Zara, welcome to Python programming'
>>> result[0]
'H'
>>> result[-1]
'g'
>>> result[:5]
'Hello'
>>> result[-11:]
'programming'
>>> result[::-1]
'gnimmargorp nohtyP ot emoclew ,araZ olleH'
>>> result[22:28]
' Pytho'
>>> result[22:29]
' Python'
>>> strM = "Python beginner tutorial"
>>> strM.upper()
'PYTHON BEGINNER TUTORIAL'
>>> strM.lower()
'python beginner tutorial'
>>> strM.capitalize()
'Python beginner tutorial'
>>> strM.count("t")
3
>>> strM.replace("Python","Machine Learning")
'Machine Learning beginner tutorial'
>>> numbers = (10, 20, 30)
>>> numbers[0]
10
>>> tup1 = (10, 20, 30)
>>> tup2 = (40, 50, 60)
>>> t_combine = tup1 + tup2
>>> t_combine
(10, 20, 30, 40, 50, 60)
>>> t_combine * 3
(10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60)
>>> t_combine[3]
40
>>> t-combine[2]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t-combine[2]
NameError: name 't' is not defined
>>> t_combine[2]
30
>>> t_combine[:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> t_combine[:3]
(10, 20, 30)
>>> t_combine[-3:]
(40, 50, 60)
>>> 