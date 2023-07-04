def check(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'

def calculate(a,b):
    # returns tuple, here we pack values to tuple
    return a+b,a-b,a*b,a/b