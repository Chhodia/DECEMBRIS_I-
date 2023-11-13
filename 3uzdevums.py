number = (input("number: "))
if number == 0:
    print('skaitlis ir 0')
elif number < 0:
    print("skaitlis ir negatīvs")
elif number % 2 == 0:
    print(number, " ir pāru")
elif number % 2 != 0:
    print(number, " ir nepāru")
else:
    print("ludzu ievadiet SKAITLI!")