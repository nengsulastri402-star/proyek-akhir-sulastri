# Modul pembantu untuk format tampilan terminal

def cetak_header():
    """Menampilkan header aplikasi di terminal."""
    print("=" * 60)
    print(" PROGRAM REKAPITULASI & ANALISIS NILAI MATEMATIKA KELAS ")
    print("=" * 60)

def cetak_pembatas():
    """Menampilkan garis pembatas."""
    print("-" * 60)

def cetak_tabel_siswa(data_siswa):
    """Menampilkan tabel daftar siswa beserta status ketuntasannya."""
    print(f"{'NIM':<8} | {'Nama':<15} | {'Nilai':<6} | {'Status':<12}")
    cetak_pembatas()
    for nim, detail in data_siswa.items():
        print(f"{nim:<8} | {detail['nama']:<15} | {detail['nilai']:<6.1f} | {detail['status']:<12}")
    cetak_pembatas()