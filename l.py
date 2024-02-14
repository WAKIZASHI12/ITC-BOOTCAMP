# pervoe zadanie 1.1
a = 17531
b = 5821
count_a = str(a).count("3")
count_b = str(b).count("3")
if count_a > count_b:
    print("a")
elif count_a < count_b:
    print("b")
else:
    print("odinakovo")

# zadanie 1.2
number2 = 4388
rem = number2 % 7
if rem >= 4:
   resul = rem * 4
   print("ostato(rem)bolishe ili raven 4 rezilitat ymnojenia na 7")
else:
    print("ostatok(rem) menishe 4 ymnojenie yt nhtbyetsa") 
# zadanie 1.3
number3 = 4292
re = number3 % 5
if re <= 3:
   resul = re / 3
   print("ostato(re)bolishe ili raven 3 rezilitat delim na 3")
else:
    print("ostatok(re) menishe 3 ymnojenie yt nhtbyetsa")

# zadanie 1.4

number4 = 7 + 5 * (3 * (27**3))
first_step = 27**3
second_step = 3 * first_step
third_step = 5 * second_step
fourth_step = 7 + third_step
print(number4==fourth_step)

# zadanie 1.5

number5 = 183
result = number5 - 17 / 19 + 13.6 * 2 % 12
print(result)

