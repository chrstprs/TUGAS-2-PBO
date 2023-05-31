# TUGAS-2-PBO
Nama : Damianus Christopher Samosir 
NPM : G1A022028

Kode di atas adalah contoh implementasi kelas Mahasiswa, Jurusan, dan Universitas. Berikut adalah penjelasan singkat untuk setiap bagian kode:

1. Kelas Mahasiswa:
   - Kelas ini memiliki atribut nama, nim, dan jurusan.
   - Method `__init__` digunakan untuk menginisialisasi objek Mahasiswa dengan nama, nim, dan jurusan.
   - Method `tampilkan_info` digunakan untuk menampilkan informasi Mahasiswa seperti nama, nim, dan nama jurusan.

2. Kelas Jurusan:
   - Kelas ini memiliki atribut nama_jurusan dan DaftarMahasiswa (daftar mahasiswa).
   - Method `__init__` digunakan untuk menginisialisasi objek Jurusan dengan nama_jurusan dan membuat daftar mahasiswa kosong.
   - Method `tambah_mahasiswa` digunakan untuk menambahkan objek Mahasiswa ke daftar mahasiswa pada Jurusan.
   - Method `tampilkan_daftar_mahasiswa` digunakan untuk menampilkan daftar mahasiswa yang terdaftar di Jurusan.

3. Kelas Universitas:
   - Kelas ini memiliki atribut nama_universitas dan DaftarJurusan (daftar jurusan).
   - Method `__init__` digunakan untuk menginisialisasi objek Universitas dengan nama_universitas dan membuat daftar jurusan kosong.
   - Method `tambah_jurusan` digunakan untuk menambahkan objek Jurusan ke daftar jurusan pada Universitas.
   - Method `tampilkan_daftar_jurusan` digunakan untuk menampilkan daftar jurusan yang terdaftar di Universitas.

Pada bagian implementasi kode di bawah definisi kelas, langkah-langkah yang dijalankan adalah sebagai berikut:

1. Langkah 2: Membuat objek Universitas dengan nama "XYZ University" menggunakan kelas Universitas.

2. Langkah 3: Membuat objek Jurusan dengan nama "Teknik Informatika" menggunakan kelas Jurusan. Kemudian objek Jurusan tersebut ditambahkan ke daftar jurusan pada objek Universitas yang sudah dibuat.

3. Langkah 4: Membuat objek Mahasiswa dengan nama "Damianus Christopher S", nim "G1A022028", dan jurusan "Teknik Informatika" menggunakan kelas Mahasiswa. Kemudian objek Mahasiswa tersebut ditambahkan ke daftar mahasiswa pada objek Jurusan yang sudah dibuat sebelumnya.

4. Langkah 5: Menampilkan daftar jurusan yang terdaftar di objek Universitas.

5. Langkah 6: Menampilkan daftar mahasiswa yang terdaftar di objek Jurusan "Teknik Informatika".

