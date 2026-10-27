# Modul untuk validasi nilai dan perhitungan statistik

def validasi_nilai(nilai):
    """Memvalidasi apakah nilai berada pada rentang 0-100."""
    return 0 <= nilai <= 100


def hitung_statistik(daftar_nilai):
    """Menghitung statistik dasar dari daftar nilai."""
    if not daftar_nilai:
        return None
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    return {
        "rata_rata": rata_rata,
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai)
    }