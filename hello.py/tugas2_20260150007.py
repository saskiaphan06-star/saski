print ("===========================================")
print ("      SISTEM KASIR DAN KALKULATOR BMI      ")
print ("===========================================")


print ("--- DATA DIRI ---")

nama = input(" Nama : ")
nim = input (" NIM : ")
berat = float(input( " Berat Badan (Kg) : "))
tinggi_cm = float(input( " Tinggi Badan (Cm) : "))

# Konversi cm ke meter
tinngi_m = tinggi_cm / 100
# Menghitung BMI 
bmi = berat / (tinngi_m ** 2)

# Bagian 2 - Kasir


print (" --- DATA BARANG ---")
barang1 = input(" Barang 1 : ")
harga1 = float(input(" Harga Barang 1 : Rp "))
barang2 = input(" Barang 2 : ")
harga2 = float(input(" Harga Barang 2 : Rp "))

# Perhitungan transaksi
subtotal = harga1 + harga2
diskon = subtotal * 0.05
harga_setelah_diskon = subtotal - diskon 
pajak = harga_setelah_diskon * 0.11
total_bayar = harga_setelah_diskon + pajak

# Output
print ("=================================================")
print ("               STRUK PEMBAYARAN                  ")
print ("=================================================")


print ("Nama : Saskia")
print (" NIM : 20260150007")

print(" --- HASIL PERHITUNGAN BMI ---")
print("Berat Badan :", round(berat, 2), "Kg")
print("Tinggi Badan :", round(tinggi_cm / 100 , 2), "M")
print("BMI :", round(bmi, 2))

print(" --- DETAIL TRANSAKSI --- ")
print("Barang 1 :", barang1, "Harga :", round(harga1, 2))
print("Barang 2 :", barang2, "Harga :", round(harga2, 2))


print(" ----------------------------------------------------------------- ")
print("Subtotal : Rp", round(subtotal, 2))
print("Diskon (5%) : Rp", round(diskon, 2))
print("Harga Setelah Diskon : Rp", round(harga_setelah_diskon, 2))
print("Pajak (11%) : Rp", round(pajak, 2))
print("Total Bayar : Rp", round(total_bayar, 2))

print("=============================================================")
print("          TERIMA KASIH TELAH BERBELANJA                      ")
print("=============================================================")
















