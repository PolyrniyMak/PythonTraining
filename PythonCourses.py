a = 0
a = a + 4
if a > 0:
    print('Good')

b = "Spam " * a
print(b)


print(5//2)
print(5/2)


print(min(1.2,1.1,3))
print(abs(-25.6))
print(abs(25.6))

print(807 + 1)
print(int('807') + 1)
print(float(7))
print(int(3.33))

help(round)
print(round(2.55, 1))


def ah(a, b, c):
    d1 = abs(a-b)
    d2 = abs(b-c)
    d3 = abs(a-c)
    return min(d1, d2, d3)

print(
    ah(1, 10, 100),
    ah(1, 10, 10),
    ah(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)
