from pynotice.app_notifier.notice import noticeOnFinish


@noticeOnFinish()
def foo(name="foooo"):  # your function
    return name


ret = foo()
print(ret)
