print("=======================================================================")
print("    SISTEM KALKULASI BIAYA PENGIRIMAN PAKET EKSPEDISI AI-EXSPRESSS     ")
print("=======================================================================")

print(" --- DATA PENGIRIMAN --- ")
nama_pengirim = input(" Nama Pengirim : ")
alamat_pengirim = input(" Alamat Pengirim : ")
berat_paket = float(input(" Berat Paket (Kg) : "))
jarak_pengiriman = float(input(" Jarak Pengiriman (Km) : "))
jenis_pengiriman = input(" Jenis Pengiriman (Reguler / Kilat) : ")

# Logika Tarif Jarak (if-elif-else)
if jarak_pengiriman <= 50:
    tarif_per_kg = 5000
elif 50 <= jarak_pengiriman <= 100:
    tarif_per_kg = 10000
else: #jika jarak > 100 km 
    tarif_per_kg = 15000


 # Logika Perhituhan Aritmatika 
biaya_dasar = berat_paket * tarif_per_kg

# Logika Jenis Layanan (if-else)
if jenis_pengiriman.lower() == "kilat": 
    biaya_tambahan = 0.20 * biaya_dasar # surcharge 20%
else:
    biaya_tambahan + 0                  # layanan reguler atau input lainnya

# TOtal Akhir dan Cetak Struk
total_biaya = biaya_dasar + biaya_tambahan

# Format struk pengiriman yang rapih
print("\n" + "="*40)
print("     STRUK BIAYA PENGIRIMAN       ")
print("="*40)
print(" Nama Pengirim : ", nama_pengirim)
print(" Berat Paket : ", berat_paket, "Kg")
print(" Jarak Pengiriman : ", jarak_pengiriman, "Km")
print(" Jenis Pengiriman : ", jenis_pengiriman)
print("="*40)
print(" Tarif per Kg : Rp", tarif_per_kg)
print(" Biaya Dasar : Rp", biaya_dasar)
print(" Biaya Tambahan : Rp", biaya_tambahan)
print("="*40)
print(" Total Biaya : Rp", total_biaya)
print("="*40)
print(" Terima kasih telah menggunakan layanan AI-Express!")


