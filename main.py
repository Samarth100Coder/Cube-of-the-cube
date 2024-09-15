def cube(x):
    return x**3

def divi3(x):
    if x%3==0:
        return cube(x)
    else:
        return('not divisible by 3')

n=int(input('Enter a number: '))
print('value=',divi3(n))