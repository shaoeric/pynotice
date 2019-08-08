from pyprompt.sound.prompt import promptOnfinish, promptOnException


@promptOnfinish()
def foo(name="foooo"):
    for i in range(10000):
        if i%1000==0:
            print(name)
    return "123"


# print("begin")
# ret = foo()
# print(ret)
# print("finish")
"""
out>>
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


@promptOnfinish()
@promptOnException()
def test(name="aaa"):
    print(name)
    return "ccc"

print("begin")
re = test()
print(re)
print("end")

"""
out>>
begin
aaa
play sound...
ccc
end
"""
