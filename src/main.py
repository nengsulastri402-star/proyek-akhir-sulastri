# File utama untuk menjalankan alur program

from utilitas import cetak_header, cetak_pembatas, cetak_tabel_siswa
from analisis import validasi_nilai, evaluasi_ketuntasan, hitung_statistik
from data_io import baca_data_file, tulis_laporan_file

def main():
    """Fungsi utama pengatur alur eksekusi program."""
    cetak_header()
    
    filepath_input = "../data/nilai_contoh.txt"
    filepath_output = "../output/laporan.txt"
    kkm = 75
    
    print(f"Membaca data dari: {filepath_input} ...\n")
    baris_data = baca_data_file(filepath_input)
    
    if not baris_data:
        print("Program dihentikan: Data kosong atau file tidak ditemukan.")
        return

    data_siswa = {}
    daftar_nilai = []
    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    # Parsing & Validasi Data
    for baris in baris_data:
        parts = baris.split(",")
        if len(parts) == 3:
            nim, nama, nilai_str = parts[0].strip(), parts[1].strip(), parts[2].strip()
            
            if validasi_nilai(nilai_str):
                nilai = float(nilai_str)
                status = evaluasi_ketuntasan(nilai, kkm)
                
                data_siswa[nim] = {
                    "nama": nama,
                    "nilai": nilai,
                    "status": status
                }
                daftar_nilai.append(nilai)
                
                if status == "TUNTAS":
                    jumlah_tuntas += 1
                else:
                    jumlah_belum_tuntas += 1
            else:
                print(f"[Peringatan] Data diabaikan (nilai tidak valid): {baris}")

    if not data_siswa:
        print("Tidak ada data siswa valid untuk diproses.")
        return

    # Tampilkan Tabel Hasil Rekapitulasi
    print("\nREKAPITULASI HASIL BELAJAR SISWA:")
    cetak_tabel_siswa(data_siswa)

    # Kalkulasi Statistik Kelas
    stat = hitung_statistik(daftar_nilai)

    print("\nRINGKASAN STATISTIK KELAS:")
    print(f"- Total Siswa Valid    : {stat['total_siswa']} Orang")
    print(f"- Rata-rata Nilai Kelas: {stat['rata_rata']:.2f}")
    print(f"- Nilai Tertinggi (Max): {stat['maksimum']:.1f}")
    print(f"- Nilai Terendah (Min) : {stat['minimum']:.1f}")
    print(f"- Siswa Tuntas (>= {kkm}): {jumlah_tuntas} Orang")
    print(f"- Siswa Belum Tuntas   : {jumlah_belum_tuntas} Orang")
    cetak_pembatas()

    # Format Isi Laporan Teks
    isi_laporan = f"""==================================================
REKAPITULASI DAN ANALISIS NILAI MATEMATIKA KELAS
==================================================
Batas KKM: {kkm}

RINGKASAN STATISTIK:
- Jumlah Siswa Valid   : {stat['total_siswa']}
- Rata-rata Kelas      : {stat['rata_rata']:.2f}
- Nilai Tertinggi (Max): {stat['maksimum']:.1f}
- Nilai Terendah (Min) : {stat['minimum']:.1f}
- Tuntas               : {jumlah_tuntas} siswa
- Belum Tuntas         : {jumlah_belum_tuntas} siswa

DAFTAR DETAIL SISWA:
"""
    for nim, detail in data_siswa.items():
        isi_laporan += f"[{nim}] {detail['nama']:<15} - Nilai: {detail['nilai']:<5.1f} ({detail['status']})\n"

    # Simpan Laporan ke Folder output/
    tulis_laporan_file(filepath_output, isi_laporan)

if __name__ == "__main__":
    main()