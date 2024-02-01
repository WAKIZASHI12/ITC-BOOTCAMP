language = input("ведите язык(python, java, javascript): ")
age = int(input("ведите возраст: "))
experince = int(input("ведите опыт работы (в годах): "))
salar = int(input("ведите зарплатные ожидание: "))
if (language.lower() in ['python',' java', 'javascript'] and 18 <= age <= 65 and experince >= 3 and salar <= 60000):
    print("кандидат подходит: ")
else:
    print("кандитат не подходит: ")
