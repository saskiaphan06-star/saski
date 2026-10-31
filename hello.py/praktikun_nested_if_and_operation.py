# ----------------------------------------------------------------------------------
print("\n--- LATIHAN 4: NESTED IF & OPERATOR LOGILA ---")
print("[!] Simulasi Penentuan Predikat Kelulusan Cumlaude")

ipk = float(input("Masukkan IPK total Anda (0.0 - 4.0"))
masa_studi = int(input("Masa Studi Anda (dalam semester)"))

# Menggunakan operator 'and' ( kedua syarat harus True)
if ipk >= 3.51 and masa_studi <= 8:
    print("-> Syarat dasar Cumlaude terpenuhi.")

    # Nested IF (Pengecekan lanjut di dalam blok True)
    nilai_d == input("Apakah Anda memiliki nilai D? (ya/tidak): ")
    if nilai_d == "tidak":
        print("STATUS AKHIR: LULUS DENGAN PUJIAN (CUMLAUDE)!")
    else:
        print("STATUS AKHIR: LULUS SANGAT MEMUASKAN (Gagal cumlaude karena nilai D)")

else:
    print("STATUS AKHIR: LULUS BIASA (Tidak memenuhi standar IPK/Masa Studi)")

print("\n" "="*50)


