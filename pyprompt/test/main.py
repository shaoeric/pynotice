from pyprompt.sound.prompt import promptOnfinish


@promptOnfinish()
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
play audio
123
finish
"""