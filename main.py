def fun(a, b, c, d,x):
    return (a * x ** 3 + b * x ** 2 + c * x + d)


a = int(input('a coeff '))
b = int(input('b coeff '))
c = int(input('c coeff '))
d = int(input('d coeff '))
e = float(input('Погрешность '))
a_bor = int(input('a '))
b_bor = int(input('b '))

if fun(a,b,c,d,a) == 0:
    print(a)
if fun(a,b,c,d,b) == 0:
    print(b)

else:
    while (b_bor - a_bor > e):
       med = (a_bor + b_bor) / 2
       if med == 0:
          print(med)
       else:
         if fun(a, b, c, d,a_bor) * fun(a, b, c, d, med) < 0:
            b_bor = med
         else:
            a_bor = med
print(a_bor, b_bor)
print("Ответ: ", a_bor)
