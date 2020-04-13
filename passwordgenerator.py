import string,random
import csv


def generatePassword(num):
    password = ''
    for n in range(num):
        x = random.randint(0,94)
        password += string.printable[x]
    return password


print('Enter name of Site')
name_of_site = input()
passwordsreturn = generatePassword(15)

print (passwordsreturn)

with open('passwords.csv', 'a', encoding='utf-8') as file:
    thewriter = csv.writer(file)

    thewriter.writerow([name_of_site, passwordsreturn])