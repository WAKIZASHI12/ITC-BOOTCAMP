result = []
for i in range(1000):
    if i % 3 == 0 or  i % 5 == 0:
         result.append(i)

counter = 0
for x in result:
    counter = counter + x
print(counter)
