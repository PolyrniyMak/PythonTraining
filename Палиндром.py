a = input()
b = len(a)
for i in range(b//2):
    if a[i] != a[-1-i]:
        print("Строка не является палиндромом")
        quit()
print("Это палиндром!!!")