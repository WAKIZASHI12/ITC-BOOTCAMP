path_a = input("Введите путь до картинки которую меняете: ")
path_b = input("Введите путь до картинки на которую меняете: ")

if os.path.exists(path_a):
    if os.path.isfile(path_a):
        if os.path.exists(path_b):
            if os.path.isfile(path_b):
                with open(path_a, "w") as file:
                    file.write(path_b)
        else:
            print("Картинка на которую необходимо изменть не найдена!")
else:
    print("Картинка которую необходимо измениь не найдена!")
