import sys


def READ(s):
    return s


def EVAL(s):
    return s


def PRINT(s):
    return s


def rep(s):
    return PRINT(EVAL(READ(s)))


while True:
    try:
        line = input("user> ")
        print(rep(line))
    except EOFError:
        sys.exit()
