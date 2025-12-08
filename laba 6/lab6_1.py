class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    
    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль успешно поменян.")
    
    def check_password(self, password):
        return password == self.__password
    
user = UserAccount("user123", "user123@blabla.com", "123321")
# user.set_password("newpassrol")
# print(user.check_password("newpassrol"))
# print(user.check_password("parrol"))

new_parrol=input("Введите новый пароль: ")
user.set_password(new_parrol)

checkparrol = input("Введите пароль для проверки: ")
print(user.check_password(checkparrol))
