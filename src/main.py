# File utama untuk menjalankan alur program

from analisis import hitung_statistik, validasi_nilai
from data_io import baca_data_file, tulis_laporan_file
from utilitas import cetak_header, cetak_pembatas


def main():
    """Fungsi utama program."""
    cetak_header()
    print("Persiapan alur program selesai.")
    cetak_pembatas()


if __name__ == "__main__":
    main()