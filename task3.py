list1 = []
for num in range(10):
    list1.append(num)
for num in list1:
    print(num+1)

string1 = input("Введите текст")
for char in string1:
    print(char) 

def hello_user():
    while True:
        user_say = input("Как дела?")   
        if user_say == "Хорошо":
            print("Отлично!")
            break
hello_user()
