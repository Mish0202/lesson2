def find_person(name):
  
    while True:
        for name in names:
     
            if name == 'Valera':
                print("Valera is found")
                names.pop()

  names = ['Vasya', 'Masha', 'Petya', "Valera", 'Sasha', 'Dasha']
  print(find_person(names))
