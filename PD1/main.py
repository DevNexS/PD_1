import fileinput

#2. Aprēķināt vidējo administratora vecumu, visvecāko un visjaunāko administratoru.
datne = open("admin.txt")
age = 0
lines = 0
for rinda in datne:
    dati = rinda.split()
    age += int(dati[3])
    lines += 1
    mid_age = age/lines
    print("Middle age = ", mid_age)
datne.close()

#3. Izdrukāt cik apvienotajā datnē administratoru, cik viesu.
lines = 0
with fileinput.FileInput(files=("admin.txt", "viesis.txt")) as users:
    for line in users:
        lines += 1
print("Lines:", lines)

#Administratoru skaits
admin = open("admin.txt")
admin_lines = 0
for line in admin:
    admin_lines += 1
print("Admin lines:", admin_lines)

#Viesu skaits
users = open("viesis.txt")
user_lines = 0
for line in users:
    user_lines += 1
print("User lines:", user_lines)


