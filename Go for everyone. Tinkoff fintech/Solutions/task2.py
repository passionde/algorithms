n, k = int(input()), int(input())
print((k - n % k) * (n // k)**2 + (n % k) * (n // k + 1)**2, (n - (k - 1))**2 + k - 1)