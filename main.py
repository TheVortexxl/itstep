print("Hello")




















# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print("I am alive!")
#
# first_student = Student()
#
#
# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print(self)
#
# first_student = Student()
#
#
# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print("I am alive!")
#
# first_student = Student()
# Student.__init__(first_student)



# class Student:
#     def __init__(self):
#         self.height = 160
#
# nick = Student()
# print(nick.height)



# class Student:
#     def __init__(self, height=160):
#         self.height = height
#
# nick = Student()
# kate = Student(height=170)
# Chiril = Student(height=2033)
# print(nick.height)
# print(kate.height)
# print(Chiril.height)






# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
#
# nick = Student()
# kate = Student(height=170)
# chiri = Student()
# print(nick.amount_of_students)
# print(Student.amount_of_students)





# class Student:
#     height = 160
#
#     def __init__(self):
#         print(self.height)
#         self.height += 10
#
#
# nick = Student()
# kate = Student()

# class Student:
#     def __init__(self):
#         self.height = 170
#     height = 160
#     def printer(self):
#         print(self.height)
#
# nick = Student()
# nick.printer()



# x = 10
# class Locker:
#     print(x)
#     def func_1(self):
#         # x=20
#         print(x)
#         def func_2():
#             # x=30
#             print(x)
#         func_2()
# some_object = Locker()
# some_object.func_1()




# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height+=height
#
#
# nick = Student()
# kate = Student(height=170)
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)
# print(Student.amount_of_students)
# jora = Student()
# print(Student.amount_of_students)




# class Student:
#     def __init__(self, name=None):
#         self.name = name
#
#     def __str__(self):
#         return f"I am a student. My name is {self.name}."
#
# nick = Student(name = "Nick")
# print(nick)


# class Student:
#     def __init__(self, name=None):
#         self.name = name
#
#     def __str__(self):
#         if self.name:
#             return f"I am a student. My name is {self.name}."
#         else:
#             return "I am a student. I don't have a name."
#
# # Creating a toy student named "Alice"
# alice = Student(name="Alice")
# print(alice)  # Output: "I am a student. My name is Alice."
#
# # Creating another toy student without giving them a name
# unknown_student = Student()
# print(unknown_student)  # Output: "I am a student. I don't have a name."

# #EXTRA
# class Student:
#     def __init__(self, name=None):
#         self.name = name
#
#     def del(self):
#         print("Training is over. I am now an expert!")
#
# nick = Student()






# import random
#
# import random
#
# class Student:
#
#     # Metoda constructor pentru a inițializa atributele studentului când este creat un student nou
#     def __init__(self, name):
#         self.name = name  # Atribuirea numelui dat când se creează un student nou
#         self.gladness = 50  # Nivelul inițial al fericirii
#         self.progress = 0  # Progresul inițial
#         self.alive = True  # Studentul este viu când este creat
#
#     # Metodă pentru a studia, care crește progresul și scade fericirea
#     def to_study(self):
#         print("Este timpul să învăț")  # Anunțând că este timpul să învețe
#         self.progress += 0.12  # Facerea de progres prin studiu
#         self.gladness -= 5  # Simțindu-se mai puțin fericit din cauza învățării
#
#     # Metodă pentru a dormi, care crește fericirea
#     def to_sleep(self):
#         print("Voi dormi")  # Spunând că este timpul să doarmă
#         self.gladness += 3  # Simțindu-se mai fericit după somn
# # Metodă pentru a se relaxa, care crește fericirea, dar scade progresul
#     def to_chill(self):
#         print("Timp de odihnă")  # Anunțând timpul de odihnă
#         self.gladness += 5  # Simțindu-se mai fericit în timp ce se relaxează
#         self.progress -= 0.1  # Progresul scade puțin pentru că se relaxează prea mult
#
#     # Metodă pentru a verifica dacă studentul este încă în viață pe baza anumitor condiții
#     def is_alive(self):
#         if self.progress < -0.5:  # Dacă progresul scade prea mult
#             print("DEAD…")  # Este mort pentru că merge foarte prost
#             self.alive = False  # Nu mai este în viață
#         elif self.gladness <= 0:  # Dacă fericirea scade prea mult
#             print("Depresie…")  # Este deprimat și nu poate merge mai departe
#             self.alive = False  # Nu mai este în viață
#         elif self.progress > 5:  # Dacă progresul devine prea mare
#             print("O morurit de fericire…")  # Studientul a murit de fericire
#             self.alive = False  # Nu mai este în viață
#
#     # Metodă pentru a afișa starea studentului la sfârșitul zilei
#     def end_of_day(self):
#         print(f"Fericire = {self.gladness}")  # Afișarea nivelului de fericire al studentului
#         print(f"Progres = {round(self.progress, 2)}")  # Afișarea nivelului de progres al studentului
#
#     # Metodă pentru a simula o zi în viața studentului
#     def live(self, day):
#         day = " Ziua " + str(day) + " din viața lui " + self.name + " "  # Descrierea zilei pentru student
#         print(f"{day:=^50}")  # Afișarea zilei cu decorări în jur
#         live_cube = random.randint(1, 3)  # Aruncarea unui zar aleatoriu pentru a simula diferite activități
#         if live_cube == 1:
#             self.to_study()  # Dacă numărul aleatoriu este 1, studentul învață
#         elif live_cube == 2:
#             self.to_sleep()  # Dacă numărul aleatoriu este 2, studentul doarme
#         elif live_cube == 3:
#             self.to_chill()  # Dacă numărul aleatoriu este 3, studentul se relaxează
#         self.end_of_day()  # Afișarea stării studentului la sfârșitul zilei
#         self.is_alive()  # Verificarea dacă studentul este încă în viață
#
# # Crearea unui student nou numit "Nick"
# nick = Student(name="Vlad")
#
# # Simularea unui an (365 de zile) în viața studentului
# for day in range(365):
#     if nick.alive == False:  # Dacă studentul nu mai este în viață, opriți simularea
#         break
#     nick.live(day)  # Simularea fiecărei zile din viața studentului