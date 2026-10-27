# PROPOSAL PROYEK AKHIR ALGORITMA DAN PEMROGRAMAN
**Judul Proyek:** Program Rekapitulasi dan Analisis Nilai Matematika   

**Nama:**  Sulastri

**Kelas:** B

**Nim:** 2225250152

**Prodi:** Pendidikan Matematika

---

## 1. Pernyataan Masalah & Latar Belakang
Guru matematika sering mengalokasikan waktu yang lama untuk melakukan rekapitulasi nilai siswa, menghitung nilai rata-rata kelas, mencari nilai tertinggi/terendah, serta menentukan ketuntasan belajar siswa berdasarkan KKM secara manual. Proses ini rawan terjadi kesalahan input dan perhitungan. Diperlukan program berbasis terminal (console) yang efisien, otomatis, serta mampu menyimpan hasil rekap secara rapi dalam bentuk file teks.

## 2. Pengguna Utama dan Tujuan
- **Pengguna Utama:** Guru/Pengajar Mata Pelajaran Matematika.
- **Tujuan Proyek:** Mengotomatiskan proses membaca data nilai, memvalidasi rentang input nilai, mengkalkulasi statistik kelas, mengukur status ketuntasan siswa, dan menghasilkan file laporan ringkas.

## 3. Ruang Lingkup & Kebutuhan Fungsional
### Fitur Wajib (Core Features):
1. **F01 (Membaca Data):** Membaca data siswa (NIM, Nama, Nilai) dari file `.txt`.
2. **F02 (Validasi Input):** Memastikan nilai berada pada rentang $0 \le \text{Nilai} \le 100$.
3. **F03 (Kalkulasi Statistik):** Menghitung nilai rata-rata, minimum, dan maksimum kelas.
4. **F04 (Status Ketuntasan):** Menentukan status "TUNTAS" atau "BELUM TUNTAS" berdasarkan batas KKM (misal KKM = 75).
5. **F05 (Ekspor Laporan):** Menyimpan ringkasan rekapitulasi ke file teks di folder `output/laporan.txt`.

### Kebutuhan Nonfungsional:
- Program berbasis Console/Terminal Python.
- Memiliki sistem penanganan kesalahan (*error handling*) jika file data tidak ditemukan.
- Kode ditulis secara modular menggunakan fungsi terpisah.

---

## 4. Spesifikasi Input, Proses, dan Output (IPO)
| Komponen | Deskripsi Detail |
| :--- | :--- |
| **Input** | File teks `data/nilai_contoh.txt` berisi daftar siswa dan nilainya. |
| **Proses** | 1. Pembacaan dan parsing isi file teks.<br>2. Validasi kelayakan nilai (0–100).<br>3. Perhitungan $\text{Rata-rata} = \frac{\sum \text{Nilai}}{n}$, nilai Min, dan Nilai Max.<br>4. Evaluasi kondisi $Nilai \ge KKM$.<br>5. Format penulisan string laporan. |
| **Output** | 1. Ringkasan statistik di terminal.<br>2. File laporan ringkas `output/laporan.txt`. |

---

## 5. Pseudocode Alur Program Utama
```text
MULAI
    PANGGUL fungsi baca_data("data/nilai_contoh.txt")
    JIKA file tidak ditemukan:
        TAMPILKAN "Error: File data tidak ditemukan!"
        SELESAI

    UNTUK SETIAP data_siswa DALAM baris_data:
        LAKUKAN fungsi validasi_nilai(nilai)
        JIKA valid ADALAH BENAR:
            SIMPAN ke dalam dictionary data_valid
        JIKA TIDAK:
            CATAT "Peringatan: Data nilai tidak valid ditemukan"

    JIKA data_valid KOSONG:
        TAMPILKAN "Tidak ada data valid untuk diproses."
        SELESAI

    HITUNG rata_rata = hitung_rata_rata(data_valid)
    HITUNG nilai_min = hitung_min(data_valid)
    HITUNG nilai_max = hitung_max(data_valid)

    EVALUASI ketuntasan tiap siswa berdasarkan KKM (75)

    TAMPILKAN hasil rekapitulasi pada Terminal
    PANGGIL fungsi simpan_laporan(rekapitulasi, "output/laporan.txt")
SELESAI


