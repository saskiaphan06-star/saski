import modul_evaluasai

def input_angka_valid(promt, min_val, max_val):
    """Meminta input angka (float) yang valid dalam rentang min_val - max_val."""

    while True:
        try:
            nilai = float(input(promt))
            if nilai < min_val or nilai > max_val:
                print(f"Warning: Angka harus di antar {min_val} dan {max_val}. Coba Lagi.")
                continue
            return nilai
        except ValueError:
            print("Error: Input harus berupa angka, bukan huruf atau teks. Coba Lagi.")

def proses_kelayakan ():
    """Meminta data, menghitung, dan menampilkan hasil kelayakan."""
print("\n--- Input Data Calon Asisten ---")
nama = input("Nama : ")
nim = input("NIM : ")
hadir = input_angka_valid("Jumlah kehadiran (0-14): ", 0,14)
tugas = input_angka_valid("Nilai Tugas (0-100): ", 0,100)
ucp1 = input_angka_valid("Nilai UCP 1 (0-100): ", 0,100)
ucp2 = input_angka_valid("Nilai UCP 2 (0-100): ", 0,100)

persentase = modul_evaluasai.hitung_persentase_presensi(hadir)
nilai_akhir = modul_evaluasai.hitung_nilai_akhir(tugas, ucp1, ucp2)
status = modul_evaluasai.cek_kelayakan_aslab(persentase, nilai_akhir)

print("\n" + "=" * 45)
print(" HASIL EVALUASI ASISTEN LABORATORIUM ")
print("=" * 45)
print(f"Nama : {nama}")
print(f"NIM : {nim}")
print(f"Kehadiran : {int(hadir)}/14 ({persentase:.2f}%)")
print(f"Nilai Akhir : {nilai_akhir:.2f}")
print(f"Status : {status}")
print("=" * 45)

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Hitung Kelayakan")
        print("2. Keluar")
        try:
            pilihan = int(input("Pilih menu (1/2): "))
        except ValueError:
            print("Error: Pilihan menu harus berupa angka 1 atay 2.")
            continue

        if pilihan == 1:
            proses_kelayakan()
        elif pilihan == 2:
            print("Terima Kasih. Progam Selesai.")
            break
        else:
            print("Warning: Pilihan tidak tersedia. Pilih 1 atau 2.")

            if __name__ == "__main__":
                main()







