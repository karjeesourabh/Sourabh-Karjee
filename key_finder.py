import random


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def prime_finder():
    test_number = random.randrange(10, 100)
    for i in range(2, test_number):
        if i % test_number == 0:
            return prime_finder()
        return test_number


p = prime_finder()
q = prime_finder()
n = p * q
phi = (p-1) * (q-1)


pub_keys = []
for i in range(2, phi):
    if gcd(i, n) == 1 and gcd(i, phi) == 1:
        pub_keys.append(i)
    if len(pub_keys) >= 100:
        break
e = random.choice(pub_keys)
del pub_keys

pri_keys = []
i = 2
while len(pri_keys) < 5:
    if (i * e) % phi == 1:
        pri_keys.append(i)
    i += 1
d = random.choice(pri_keys)
del pri_keys


print("Walla.. Here is your Keys:")
print(f"Public Key: ({e},{n}) and Private Key: ({d},{n})")
