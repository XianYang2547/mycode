__all__ = ['max1','Person']


def max1(a, b):
    return a + b


def min1(c, d):
    return c - d


class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print('登录成功啦')
