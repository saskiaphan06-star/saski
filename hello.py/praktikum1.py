print("--- LATIHAN 1: VARIABEL DAN TIPE DATA ---")
nama_mahasiswa = "Saskia"     # String
umur = 18                     # Integer
tinggi_badan = 155            # Float 
status_aktif = True           # Boolean

# Menampilkan nilai variabel dan mengecek tipe datanya menggunakan type ()
print("Nama Mahasiswa", nama_mahasiswa, "Type", type(nama_mahasiswa))
print("Umur Mahasiswa", umur, "Type", type(umur_mahasiswa))
print("Tinggi Badan", tinggi_badan, "Type", type(tinggi_badan))
print("Status Aktif", status_aktif, "Type", type(status_aktif))

print("\n") #memberikan jarak spasi antar latihan

# ====================================

print ("--- LATIHAN 2: KONVERSI TIPE DATA ---")
angka_string = "50"
angka_integer = int(angka_string)  # Konversi string ke integer
angka_float = float(angka_string)    # Konversi string ke float

print("Angka String:", angka_string, "Type:", type(angka_string))
print("Angka Integer:", angka_integer, "Type:", type(angka_integer))
print("Angka Float:", angka_float, "Type:", type(angka_float))

print("\n")

# ==========================================    

print ("--- LATIHAN 3: OPERASI ARITMATIKA ---")
a = 15
b = 4

print("Penjumlahan (a+b) :", a + b)
print("Pengurangan (a-b) :", a - b)
print("Perkalian (a*b) :", a * b)
print("Pembagian (a/b) :", a / b)
print("Pembagian Bulat (a//b) :", a // b)
print("Sisa Bagi (a % b) :", a % b)
print("Pangkat (a ** b) :", a ** b)

