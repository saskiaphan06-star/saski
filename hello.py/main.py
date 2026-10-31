# Mengimpor modul buatan sendiri 
import modul_skoring

print("=======================================")
print(" SISTEM INPUT NILAI AKHIR AI           ")
print("=======================================")

# 1. PROSES INPUT
nama_mk = "Pemograman Dasar AI"
in_tugas = float(input("Masukan Nilai Tugas Mandiri (0-100) : "))
in_ucp1 = float(input("Masukan Nilai UCP 1          (0-100) : "))
in_ucp2 = float(input("Masukan Nilai UCP 2          (0-100) :"))

# 2. PROSES PEMANGGILAN FUNGSI MODUL
nilai_akhir = modul_skoring.hitung_nilai_akhir(in_tugas, in_ucp1, in_ucp2)
grade_akhir = modul_skoring.tentukan_grade(nilai_akhir)

# 3. PROSES OUTPUT
print("\n====================================================")
print(f"RANGKUMAN NILAI: {nama_mk}")
print("======================================================")
print(f"Nilai Akhir (Kalkulasi) : {nilai_akhir:.2f}")
print(f"Grade Mutu              : {grade_akhir}")
print("=======================================================")
