## 介绍
##### README:  [English](https://github.com/shaoeric/pynotice/blob/master/README.md) | [中文](https://github.com/shaoeric/pynotice/blob/master/README-cn.md)

pynotice可以在你的函数执行结束或者异常后播放音频或者发送邮件通知你
#### 功能
___
- 使用默认或者自定义的wav文件路径
- 发送带有图片或者txt附件的电子邮件
- python装饰器编写你的代码
- 无需配置SMTP服务器，当然也可以通过函数的参数配置

#### 安装
___
只支持python3 
```
pip install pynotice
```
国内源不知道什么时候更新，可以在仓库的release里下载whl再安装
#### 使用方法
___
##### -音频- 【废弃】
##### 函数运行结束通过音频通知
```python
from pynotice.sound.notice import noticeOnFinish

@noticeOnFinish()
def foo(name="foooo"):  # 你所要通知的函数
    return name
   
ret = foo()
print(ret)
```
##### 函数异常时通过音频通知
```python
from pynotice.sound.notice import noticeOnException, noticeOnFinish

@noticeOnFinish()
@noticeOnException()
def foo(name="aaa"):
    return name
```

##### -电子邮件-

首先，请先确保您已经开启电子邮箱的SMTP功能，不同的电子邮箱开启方法不同。 [gmail SMTP authorization](https://www.digitalocean.com/community/tutorials/how-to-use-google-s-smtp-server) | [qq email SMTP authorization](https://jingyan.baidu.com/article/6079ad0eb14aaa28fe86db5a.html)

##### 函数结束后通过邮件通知
```python
from pynotice.mail import noticeOnFinish
import numpy as np

sender = "xxx@gmail.com"
code = "xxxxxxxxxxxxxxxx"  # SMTP 授权码 
receiver = "xxx@foxmail.com"  # list or str

# 您也可以指定一个附件
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

#### 程序异常时通过邮箱通知
```python
from pynotice.mail import noticeOnException, noticeOnFinish

sender = "xxx@gmail.com"
code = "xxxxxxxxxxxxxxxx"  # SMTP 授权码 
receiver = "xxx@foxmail.com"  # list or str

@noticeOnFinish(sender, code, receiver,attachments=[])
@noticeOnException(sender, code, receiver)
def foo(name="aaa"):
    return "ccc"
   
re = foo()
```

#### 导入模块
| 模块名 | 描述 |
| -----  | ----------- |
| [filetype](https://pypi.org/project/filetype/) | 获取文件的格式 |
| [simpleaudio](https://pypi.org/project/simpleaudio/1.0.2/) | 播放wav音频 | 
| [zmail](https://pypi.org/project/zmail/) | 发送email |

#### 资源
模块中的两个wav音频是从[这里](http://www.aigei.com/sound/class/)下载的。本来想用ipad自己做的，但是自己做的实在不太合适...
