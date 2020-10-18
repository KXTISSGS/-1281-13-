tags = ["ОВ", "СС", "С", "ДСП", "НС"]       #Уровни доступа

class User:                                 
    def __init__(self, name, TagLvl):
        self.name = name
        self.tagLvl = TagLvl

class File:
    def __init__(self, name, TagLvl):
        self.name = name
        self.tagLvl = TagLvl

    def __str__(self):
        return self.name
def read(user, file):
    if tags.index(user.tagLvl) >= tags.index(file.tagLvl):
        print("Операция прошла успешно")
    else:
        print("Отказ в выполнении операции. Недостаточно прав.")

def write(user, file):
    if tags.index(user.tagLvl) <= tags.index(file.tagLvl):
        print("Операция прошла успешно")
    else:
        print("Отказ в выполнении операции. Недостаточно прав.")
def availableFiles(user):                                   #доступные файлы
    availableFile = [fileObject for fileObject in Object if tags.index(fileObject.tagLvl) <= tags.index(user.tagLvl)]
    availableFile = ", ".join([str(item) for item in availableFile])
    return availableFile
def requeste(user, file):                       #
    if tags.index(user.tagLvl) >= tags.index(file.tagLvl):
        print("Операция прошла успешно")
    else:
        print("Отказ в выполнении операции. Недостаточно прав.")

object1 = File("object1", "ОВ")
object2 = File("object2", "СС")
object3 = File("object3", "НС")
object4 = File("object4", "ДСП")
object5 = File("object5", "С")

Object = [object1, object2, object3, object4, object5]

ken = User("Кен", "ОВ")
felix = User("Феликс", "СС")
phoenix = User("Феникс", "С")
maxim = User("Максим", "ДСП")
claude = User("Клод", "НС")
sanji = User("Санджи", "ДСП")
luffi = User("Луффи", "СС")
users = [ken, felix, phoenix, maxim, claude, sanji, luffi]


while True:
    loginExit = False
    curUser: User
    while True:

        userName = input("User ")
        for user in users:
            if userName == user.name:
                curUser = user
                loginExit = True
        if loginExit:
            break
        print("Ошибка аутентификации.")
    availableFile=availableFiles(curUser)
    print(f"Аутентификация прошла успена. \nДоступные файлы {availableFile}")
    while True:
        command = input("Жду ваших указаний > ")
        if command=="read":
            inFile = int(input("Над каким объектом производится операция? "))
            if inFile <= len(Object):
                read(curUser,Object[inFile-1])
        elif command=="write":
            inFile = int(input("Над каким объектом производится операция? "))
            if inFile <= len(Object):
                write(curUser,Object[inFile-1])
        elif command=="requeste":
            inFile = int(input("Над каким объектом производится операция? "))
            if inFile <= len(Object):
                requeste(curUser,Object[inFile-1])
        elif command == "grant" and curUser.tagLvl=="ОВ":
            number = input("Чему вы хотите присвоить право? 1 - субъекту, 2 - объекту. ")
            if number =="1":

                     userNum = input("Какому пользователю вы хотите поменять право?\n" + "\n".join([f"{i} - {str(user.name)}" for i, user in enumerate(users, start=1)]) + "\n")
                     ext = False
                     if int(userNum)>0 and int(userNum) <= len(Object):
                         NewTag=input("Введите новый уровень доступа ")
                         for tag in tags:
                             if NewTag == tag:
                                 users[int(userNum)].tagLvl=NewTag
                                 print("Операция прошла успешно ")
                                 ext=True


                     if ext==False:
                         print("Ошибка ввода")

            elif number == "2":

                userNum = input("Какому объекту вы хотите поменять право?\n" + "\n".join(
                    [f"{i} - {str(object.name)}" for i, object in enumerate(Object, start=1)]) + "\n")
                ext = False
                if int(userNum) > 0 and int(userNum) <= len(Object):
                    NewTag = input("Введите новый уровень доступа ")
                    for tag in tags:
                        if NewTag == tag:
                            users[int(userNum)].tagLvl = NewTag
                            print("Операция прошла успешно ")
                            ext = True

                if ext == False:
                    print("Ошибка ввода")
        elif command == "quit":
            print(f"Работа пользователя {curUser.name} завершена. До свидания!")
            break









