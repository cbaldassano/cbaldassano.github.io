limit = 1000
a = [True] * limit                          # Initialize the primality list
a[0] = a[1] = False

for (i, isprime) in enumerate(a):
    if isprime:
        print(i)
        for n in range(2*i, limit, i):     # Mark factors non-prime
            a[n] = False
