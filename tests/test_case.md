# Rancangan Test Case Proyek

| ID Test | Kategori | Input / Kondisi | Ekspektasi Hasil | Target Fungsi |
| :--- | :--- | :--- | :--- | :--- |
| **TC01** | Normal | Data nilai `[85, 70, 95]` | Rata-rata = 83.33 | `hitung_statistik()` |
| **TC02** | Batas Min | Nilai input `0` | Nilai diterima sebagai data valid | `validasi_nilai()` |
| **TC03** | Batas Max | Nilai input `100` | Nilai diterima sebagai data valid | `validasi_nilai()` |
| **TC04** | Invalid | Nilai input `105` atau `-10` | Input ditolak, munculkan peringatan | `validasi_nilai()` |
| **TC05** | Invalid Error | Membaca file yang tidak ada | Menangkap `FileNotFoundError` tanpa crash | `baca_data_file()` |
