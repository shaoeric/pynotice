## Introduction
##### README: [English](https://github.com/shaoeric/pynotice/blob/master/README.md)|[&#x4E2D;&#x6587;](https://github.com/shaoeric/pynotice/blob/master/README-cn.md)
pynotice is a python3 module that can play a sound or send an email to inform you when your function finishes or goes wrong. 

#### Features
___
- Use default or custom wav file
- Send email with an attachment of pictures or txt files
- python decorator
- No need specifying smtp server address, of course you can do it

#### Installation
___
only for python3 
```
pip install pynotice
```

#### Usage
___
##### -Sound-
##### inform you by playing sound when your function finishes
```python
from pynotice.sound.notice import noticeOnFinish

@noticeOnFinish()
def foo(name="foooo"):  # your function
    return name
   
ret = foo()
print(ret)
```
##### inform you by playing sound when your function goes wrong
```python
from pynotice.sound.notice import noticeOnException, noticeOnFinish

@noticeOnFinish()
@noticeOnException()
def foo(name="aaa"):
    return name
```

##### -Email-

Firstly, please confirm you have opened SMTP functions in your email. And the method depends on your email server (For @163.com and @gmail.com you need to set your app private password) [gmail SMTP authorization](https://www.digitalocean.com/community/tutorials/how-to-use-google-s-smtp-server) | [qq email SMTP authorization](https://jingyan.baidu.com/article/6079ad0eb14aaa28fe86db5a.html)

##### inform you of your function result by sending an email when your function finishes
```python
from pynotice.mail.notice import noticeOnFinish
import numpy as np

sender = "xxx@gmail.com"
code = "xxxxxxxxxxxxxxxx"  # SMTP authorization code 
receiver = "xxx@foxmail.com"  # list or str

# you can also send an attachments
@noticeOnFinish(sender, code, receiver, attachments=['demo.txt']) 
def foo(name="aaa"):
    x = np.array([[1, 2, 3], [2, 3, 4]])
    for i in range(100):
        if i%20==0:
            print(i)
    np.savetxt("demo.txt", x)
    return x, [1,23,5,4], name

ret = foo()
print(ret)
```

#### inform you of the Exception by an email when the function throws exceptions
```python
from pynotice.mail.notice import noticeOnException, noticeOnFinish

sender = "xxx@qq.com"
code = "xxxxxxxxxxxxxxxx"  # SMTP authorization code 
receiver = "xxx@foxmail.com"  # list or str

@noticeOnFinish(sender, code, receiver,attachments=[])
@noticeOnException(sender, code, receiver)
def foo(name="aaa"):
    return "ccc"
   
re = foo()
```

#### Include
| module | description |
| -----  | ----------- |
| [filetype](https://pypi.org/project/filetype/) | get the file format |
| [simpleaudio](https://pypi.org/project/simpleaudio/1.0.2/) | play the wav audio | 
| [zmail](https://pypi.org/project/zmail/) | send emails simply |


#### Resource
Two wav sounds in module are downloaded from [here](http://www.aigei.com/sound/class/). I have thought I can diy with my ipad, but I'm a green hand in that so ...