m=0
n=1
k=int(input(': '))
# fib=0
# i=1
# while i<k:
#     fib=m+n
#     m=n
#     n=fib
#     i+=1

# print(fib) 


def fibonacci(k):
    if k in (1, 2):
        return 1
    return fibonacci(k - 1) + fibonacci(k - 2)
 
print(fibonacci(k))