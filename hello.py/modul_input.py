def minta_input_nilai(nama_komponen):
    """
    Fungsi ini akan terus mengulang (while) meminta input
    sampai user memasukkan ANGKA yang VALID (0 - 100)
    """
    while True:
        try:
            # Mencoba menerima input dan mengubahnya ke desimal (float)
            teks_input = input(f"Masukkan nilai {nama_komponen} (0 - 100):")
            nilai = float(teks_input)

            # Debugging Logika: Mencegah nilai minus atau lebih dari 100
            if nilai < 0 or nilai > 100:
                print("[Warning] Nilai tidak masuk akal Harap masukan rentang 0 hingga 100.")
                continue # Mengulang loop kembali ke atas 

            # Jika semua aman, kembalikan nilai dan hentikab loop
            return nilai

        except ValueError:
            # Menangkap eror jika user memasukkan huruf (misal: "delapan puluh")
            print("[ERROR SYSTEM] Tipe data salah! Anda memasukkan teks, harap masukkan Angka. \n")
            
