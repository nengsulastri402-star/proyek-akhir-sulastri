# Modul untuk membaca dan menyimpan file data


def baca_data_file(filepath):
    """Membaca data nilai dari file teks."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File {filepath} tidak ditemukan.")
        return []


def tulis_laporan_file(filepath, content):
    """Menulis hasil laporan rekapitulasi ke file teks."""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Laporan berhasil disimpan di {filepath}")
    except IOError as e:
        print(f"Gagal menyimpan file: {e}")