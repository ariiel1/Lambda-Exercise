from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
#tbh I googled this part I don't really get it

nlength = int(input("Length: "))
if nlength <=0:
    print("Error")
else:
     print(fib(nlength))