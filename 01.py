# from utils import *
import utils

if __name__ == "__main__":
    print('###############################')
    num = int(input('enter a number: '))
    result = utils.check(num)
    print(f"Number: {num} is {result}.")
    
    print('###############################')
    test = utils.calculate(5,4)
    # unpacking tuple
    sum,diff,mul,div = test
    # check result
    print(test)
    print(type(test))
    # check unpacked values
    print(sum, diff)

