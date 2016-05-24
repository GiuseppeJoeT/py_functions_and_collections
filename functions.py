# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one_arg(arg1):
    print "arg1: %r" % arg1


def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
