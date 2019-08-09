from pynotice.sound.notice import noticeOnFinish as spof, noticeOnException as spoe
from pynotice.mail.notice import noticeOnFinish as mpof, noticeOnException as mpoe
import numpy as np


# sound prompt
@spof()
def foo(name="foooo"):
    for i in range(10000):
        if i%1000==0:
            print(name)
    return "123"


print("begin")
ret = foo()
print(ret)
print("finish")
"""
out <<
begin
foooo
foooo
foooo
foooo
foooo
foooo
foooo
foooo
foooo
foooo
play audio.....
123
finish
"""

@spof()
@spoe()
def test(name="aaa"):
    print(name)
    return "ccc"

# print("begin")
# re = test()
# print(re)
# print("end")

"""
out <<
begin
aaa
play sound...
ccc
end
"""


# email prompt
sender = "xxx@qq.com"
code = "xxxxxxxxxxxxxxxx"
receiver = "xxx@foxmail.com"  # list or str

@mpof(sender, code, receiver, attachments=['demo.txt'])
def test(name="aaa"):
    x = np.array([[1, 2, 3], [2, 3, 4]])
    for i in range(100):
        if i%20==0:
            print(i)
    np.savetxt("demo.txt", x)
    return x, [1,23,5,4], name

# print("begin")
# ret = test()
# print(ret)
# print("end")
"""
out <<
begin
server config success
0
20
40
60
80
sending email...
(array([[1, 2, 3],
       [2, 3, 4]]), [1, 23, 5, 4], 'aaa')
end
"""


@mpoe(sender, code, receiver)
def test(name="aaa"):
    for i in range(100):
        if i%20 == 0:
            print(i)
    x = np.array([[1,23,4]])
    np.savetxt('test.txt', x)
    y = np.loadtxt('notExist.txt')
    return y

# print("begin")
# result = demo()
# print(result)
# print("end")

"""
begin
server config success
0
20
40
60
80
sending email...
Traceback (most recent call last):
...  ...
    raise IOError("%s not found." % path)
OSError: notExist.txt not found.
"""
