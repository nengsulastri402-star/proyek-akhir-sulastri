# Laporan Hasil Pengujian Proyek (Test Case Execution)

| ID Test | Kategori | Input / Kondisi | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC01** | Normal | Data nilai `[85, 70, 95]` | Rata-rata = 83.33 | Rata-rata = 83.33 | **PASS** |
| **TC02** | Batas Min | Nilai input `0` | Nilai diterima sebagai data valid | Nilai diterima (0.0) | **PASS** |
| **TC03** | Batas Max | Nilai input `100` | Nilai diterima sebagai data valid | Nilai diterima (100.0) | **PASS** |
| **TC04** | Invalid | Nilai input `105` atau `-10` | Input ditolak/diabaikan | Pesan peringatan muncul, data diabaikan | **PASS** |
| **TC05** | Invalid | Input string non-angka `"abc"` | Input ditolak | `validasi_nilai()` mengembalikan `False` | **PASS** |
| **TC06** | File Error | Membaca file tidak ada | Menangkap error tanpa crash | Menampilkan `[Error] File tidak ditemukan!` | **PASS** |