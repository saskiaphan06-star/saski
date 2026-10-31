print("\n=====================================")
print("         BAGIAN 2: WHILE LOOP          ")
print("=======================================")

print("a. Menghitung menggunakan while (dengan jeda):")
hitung = 1
while hitung <= 3:
    print("Hitungan while ke-", hitung)
    hitung = hitung + 1

    print("\nb. Progam interaktif dengan user:")
    kata_kunci = ""

    while kata_kunci != "berhenti":
        kata_kunci = input("Ketik kata 'berhenti' untuk keluar dari progam:")

if kata_kunci != "berhenti":
    print("-> Memeriksa input...")
    print("-> Anda mengetik:", kata_kunci, "- Progam masaih berulang!\n")

    print("\nMemproses jalan keluar...")
    print("Selamat! Anda berhasil keluar dari perulangan while.")
