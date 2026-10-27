# Modul untuk membaca dan menyimpan file data
import os

def baca_data_file(filepath):
    """Membaca isi file data teks dan mengembalikan daftar baris string."""
    if not os.path.exists(filepath):
        print(f"[Error] File '{filepath}' tidak ditemukan!")
        return []
    
    lines = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                line_str = line.strip()
                if line_str and not line_str.startswith("NIM"):
                    lines.append(line_str)
    except Exception as e:
        print(f"[Error] Terjadi kesalahan saat membaca file: {e}")
        
    return lines

def tulis_laporan_file(filepath, isi_laporan):
    """Menulis hasil rekapitulasi ke file teks di folder output/."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(isi_laporan)
        print(f"\n[Sukses] Laporan berhasil disimpan ke file: {filepath}")
    except IOError as e:
        print(f"\n[Error] Gagal menyimpan file laporan: {e}")