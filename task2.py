def compare_str(str1, str2):
    if type(str1) != str or type(str2) != str:
        return 0
    if str1 == str2:
        return 1
    if len(str1)>len(str2):
            return 2
    if str1 != str2 and str2 == "learn":
        return 3
for _ in range (5):
    input1, input2 = input("Введите 1ю строку"), input("Введите 2ю строку")
    print(compare_str(input1, input2))
