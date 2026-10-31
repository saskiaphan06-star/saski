nama_barang = input("Nama barang: ")
harga_barang = float(input("Harga barang: Rp"))
diskon = float(input("Diskon (%): "))

jumlah_diskon = harga_barang * diskon / 100
total_bayar = harga_barang - jumlah_diskon

print("============================")
print("     HASIL PERHITUNGAN      ")
print("============================")

print("Nama Barang:", nama_barang)
print("Harga Barang: Rp", harga_barang)
print("Diskon :", diskon, "%")
print("Jumlah Diskon: Rp", jumlah_diskon)
print("Total Bayar: Rp", total_bayar)



