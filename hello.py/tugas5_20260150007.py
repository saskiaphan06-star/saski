print("================================================")
print("             Sistem Keamanan Login              ")
print("================================================")

# Bagian 1: Login
sandi_benar = "AI2026"
percobaan = 0

while percobaan < 3:
    password = input("Masukan Password: ")
    if password == sandi_benar:
        print("Akses Diberikan! ")
        break
    percobaan +=1
else:
    print("Sistem Terkunci! ")
    exit()

print("\n                                              ")
print("================================================")
print("             Analisis Suhu Server               ")
print("================================================")

total = 0
tertinggi = 0

for hari in range(1, 6):
    suhu = float(input(f"Suhu hari ke-{hari}: "))
    total += suhu
    if hari == 1 or suhu > tertinggi:
        tertinggi = suhu

print("Total Suhu:" , total)
print("Rata-rata Suhu:" , total / 5)
print("Suhu Tertinggi:" , tertinggi)

