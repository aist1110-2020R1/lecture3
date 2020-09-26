# for loop exercise

#1
# num = int(input('Enter the value of x: '))
# x = lambda n: 1 if not(n) else n*x(n-1)
# ans = sum([(num**n)*((-1)**n)/x(n) for n in range(11)])
# print(ans)

#2
# def is_prime(n, lookup):
#     if n==0 or n==1: return False
#     for i in lookup:
#         if not(n%i): return False
#     return True
#
# lo, up = tuple(map(int, input('Enter lower and upper: ').split()))
# lookup = []
# for i in range(max(0, lo)):
#     if is_prime(i, lookup): lookup.append(i)
# ind = len(lookup)
# for i in range(lo, up+1):
#     if is_prime(i, lookup): lookup.append(i)
# print(lookup[min(ind, len(lookup)):])

#3
# def is_prime(n, lookup):
#     if n==0 or n==1: return False
#     for i in lookup:
#         if not(n%i): return False
#     return True
#
# n = int(input('Enter n: '))
# lookup = []
# for i in range(n+1):
#     if is_prime(i, lookup):
#         lookup.append(i)
#         if lookup[len(lookup)-1] - lookup[max(0, len(lookup)-2)] == 2: print(tuple(lookup[:-3:-1][::-1]))