def hitung_daya(voltase, arus):
    """Mengembalikan daya listrik (Watt) =
    Voltase x arus."""
    return voltase * arus 

def kategori_konsumsi(daya):
    """Mengenbalikan status kategori berdasarkan daya (Watt)."""
    if daya < 10:
        return "Hemat (Low Power)"
    elif daya <= 50:
        return "Normal"
    else:
        return "Tinggi (High Power - Perlu Heatskin)"
    
