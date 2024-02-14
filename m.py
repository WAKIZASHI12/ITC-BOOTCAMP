a = 2**3
b = 3**2
if a >= b:
   print('a>b')

else:
    print("b>a")

a = 45
if 0 <= a <= 21 or 57 <= a <= 100:
    print('a razreshonom')
else:
    print("a zapreshonom")


a = 40

if 40  % 2 == 0:
    print('4chet')
else:
    print("ne4het")
if 40 % 3 == 0:
    print('deli')
else:
    print("nedeli")
if 40 **2 > 1000:
   print('kfadrat bolishe 1000')
else:
    print(" kfadrat menishe 1000")

a = 14
if a <= 13 or a >= 15:
    print('a <= 13')
else:
    print("a >= 15")



a = 10 // 5
b = 10 / 5
if a == b:
    print('ravn')
else:
    print("neravn")


a = 10 // 5
b = 10 / 5
if a == b:
    print('a+b')
else:
    print("neravn")

number = -10
if number < 0:
   print('chusklo {number} otri.')
else:
    print("chusklo {number} ne otri.")



a = 10
b = 5
if a > 0 and b > 10:
    print('oba  yavlyat chislami')
else:
    print("ne")



a = 10
b = 5
if a > b:
    print('a + 2')
else:
    print("b + 2")

a = 849
if  a > 0 and a < 0:
    print('boli')
else:
    print("neshe")



age = 19
if age >= 18:
    print('sovershenoletni')
elif age <= 4:
    print("rebenok")
else:
    print("nesovershonoletni")



a =  45
b = 6
if a % b == 0:
    print('da')
else:
    print("net")


year = 20080
current_year = 2024
if year == current_year:
    print('nastypil')
elif year > current_year:
    print("bydyshie")
else:
    print("proshel")



a = 1900
b = 30
c = 89
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)





a = 17391
b = 546
c = 934
if (a % 17) < (b % 17) and (a % 17) < (c % 17):
    print('a % 17 ostatok meshe')
elif (b % 17) < (a % 17) and (b % 17) < (c % 17):
    print("b % 17 ostatok meshehe")
else:
    print("c % 17 osnanok meshe")


x = 13
a = 172
if (x ** 2) <= a:
    print(x**4)

