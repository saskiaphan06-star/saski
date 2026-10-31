import modul_konversi

print("============================================")
print(" KALKULATOR KONSUMSI DAYA PERANGKAT EDGE AI ")
print("============================================")

nama = input("Masukan Nama Perangkat AI : ")
Voltase = float(input("Masukan Voltase (Volt) :"))
arus = float(input("Masukan Arus (Ampere) :"))

daya = modul_konversi.hitung_daya(Voltase, arus)
kategori = modul_konversi.kategori_konsumsi(daya)

print("                                                ")
print("================================================")
print(" HASIL ANALISIS DAYA AI ")
print("================================================")
print(f"Nama Perangkat : {nama}")
print(f"Daya Terhitung : {daya:.2f} watt")
print(f"Kategori Daya  : {kategori}")
print("================================================")