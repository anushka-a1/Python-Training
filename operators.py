Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
str([23,22])
'[23, 22]'
l=[10,20,30]
a=l
a
[10, 20, 30]
a[1]=200
a
[10, 200, 30]
l
[10, 200, 30]
a=l.copy()
a
[10, 200, 30]
l
[10, 200, 30]
a[1]=20
a
[10, 20, 30]
l
[10, 200, 30]
n=[10,20,30,[2,3,4]]
b=n.copy()
b[1]=9
b
[10, 9, 30, [2, 3, 4]]
n
[10, 20, 30, [2, 3, 4]]
m=[10,20,30,[2,[6,7,8],3,4]]
o=m.copy()
o[3][1][1]=4
o
[10, 20, 30, [2, [6, 4, 8], 3, 4]]
m
[10, 20, 30, [2, [6, 4, 8], 3, 4]]
g=copy.deepcopy(0)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    g=copy.deepcopy(0)
NameError: name 'copy' is not defined. Did you forget to import 'copy'?
g=copy.deepcopy(o)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    g=copy.deepcopy(o)
NameError: name 'copy' is not defined. Did you forget to import 'copy'?
g=copy.deepcopy(m)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    g=copy.deepcopy(m)
NameError: name 'copy' is not defined. Did you forget to import 'copy'?
import copy
g=copy.deepcopy(o)
g[3][1][2]=9
g
[10, 20, 30, [2, [6, 4, 9], 3, 4]]
o
[10, 20, 30, [2, [6, 4, 8], 3, 4]]
10+20
30
30+0.79
30.79
30//6
5
30**2
900
(3+4j)+9
(12+4j)
(3+6j)//4
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    (3+6j)//4
TypeError: unsupported operand type(s) for //: 'complex' and 'int'
(1,2,3,4)+(5,6,7)
(1, 2, 3, 4, 5, 6, 7)
(3+6j)//(6+7j)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    (3+6j)//(6+7j)
TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
t=(1,2)
l=[1,2]
t+l
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t+l
TypeError: can only concatenate tuple (not "list") to tuple
10 and 40
40
10 or 40
10
'' or 0
0
'' and 0
''
[] and ()
[]
{} and ()
{}
'' or {}
{}
0 and False
0
0 or False
False
set
<class 'set'>
set()
set()
int
<class 'int'>
int()
0
dict()
{}
float()
0.0
complex()
0j
a=10
a+=100
a
110
a*=6
a
660
a/=4
a
165.0
a//3
55.0
a=10-9j
a*=9
a
(90-81j)
a//8
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a//8
TypeError: unsupported operand type(s) for //: 'complex' and 'int'
a/2
(45-40.5j)
a-7
(83-81j)
a+8
(98-81j)
a*9
(810-729j)
a=8.5
a//6
1.0
a/2
4.25
10==20
False
10<=20
True
True==False
False
[1,2,3]==[2,3,4]
False
{1,2,3,4}+=9
SyntaxError: 'set display' is an illegal expression for augmented assignment
'anushka' =='anushka'
True
'anushka'+='a'
SyntaxError: 'literal' is an illegal expression for augmented assignment
4!=8
True
True!=False
True
~4
-5
~True
-2

[10,29]>=[8,29]
True
10>20
False
20.9>=5.6
True
(5+6j)<=7
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    (5+6j)<=7
TypeError: '<=' not supported between instances of 'complex' and 'int'
(5+6j)<=True
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    (5+6j)<=True
TypeError: '<=' not supported between instances of 'complex' and 'bool'
False>=True
False
False>=0
True
3>=9
False
0.5<8
True
3.4566>=8.7
False
3.4566>=8.7
False
str([23,22])
'[23, 22]'
True>False
True
>>> ord('a')
97
>>> ord('*')
42
>>> '23'>'42'
False
>>> 'hi'>'hello'
True
>>> False> 'True'
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    False> 'True'
TypeError: '>' not supported between instances of 'bool' and 'str'
>>> [10,20]<[30]
True
>>> 1+0j==1
True
>>> {10,20,30}=={20,30,10}
True
>>> 'a' in 'apple'
True
>>> 'b' not in 'apple'
True
>>> 'b' in 'dance'
False
