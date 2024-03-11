def cipher_creds(func):
    def wrapper():
        login, password = func()
        cipher_login = ""
        cipher_password = ""
        for letter in login:
            if letter.isdigit():
                cipher_login += str(chr(int(letter)))
            else:
                cipher_login += str(ord(letter))

        for letter in password:
            if letter.isdigit():
                cipher_password += str(chr(int(letter)))

            else:
                cipher_password += str(ord(letter))



        return cipher_login, cipher_password

    return wrapper


@cipher_creds
def set_user_creds():
    login = input("enter your login : ")
    password = input("enter your password : ")
    return login, password


print(set_user_creds())

