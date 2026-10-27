# Modul untuk validasi nilai dan perhitungan statistik

def validasi_nilai(nilai):
    """Memvalidasi apakah nilai numerik dan berada pada rentang 0-100."""
    try:
        val = float(nilai)
        return 0 <= val <= 100
    except (ValueError, TypeError):
        return False

def evaluasi_ketuntasan(nilai, kkm=75):
    """Menentukan status ketuntasan siswa berdasarkan batas KKM."""
    return "TUNTAS" if nilai >= kkm else "BELUM TUNTAS"

def hitung_statistik(daftar_nilai):
    """Menhitung ringkasan statistik dari daftar nilai numerik."""
    if not daftar_nilai:
        return {
            "rata_rata": 0,
            "minimum": 0,
            "maksimum": 0,
            "total_siswa": 0
        }
    
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    nilai_min = min(daftar_nilai)
    nilai_max = max(daftar_nilai)
    
    return {
        "rata_rata": rata_rata,
        "minimum": nilai_min,
        "maksimum": nilai_max,
        "total_siswa": len(daftar_nilai)
    }