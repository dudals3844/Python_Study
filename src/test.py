# Error

# make error
# class Bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle(Bird):
#     pass

# eagle = Eagle()
# eagle.fly()

class MyError(Exception):
    pass


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")