# TUGAS-2-PBO
Nama : Damianus Christopher Samosir 
NPM : G1A022028

Kode di atas adalah contoh implementasi dari konsep pemrograman berorientasi objek (OOP) yang menggunakan tiga kelas, yaitu `Mahasiswa`, `Jurusan`, dan `Universitas`. Kode tersebut membentuk sebuah struktur data yang merepresentasikan mahasiswa-mahasiswa yang terdaftar di berbagai jurusan di sebuah universitas.

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        # Menampilkan informasi nama, nim, dan nama jurusan mahasiswa
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)
        
- Kelas `Mahasiswa` merepresentasikan objek mahasiswa dengan atribut `nama`, `nim`, dan `jurusan`. Pada metode `__init__`, atribut-atribut tersebut diinisialisasi dengan nilai-nilai yang diberikan saat objek dibuat. Kelas ini juga memiliki metode `tampilkan_info()` yang digunakan untuk menampilkan informasi nama, nim, dan nama jurusan mahasiswa.

class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        # Menambahkan mahasiswa ke daftar mahasiswa jurusan
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        # Menampilkan daftar mahasiswa yang terdaftar di jurusan
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama:", mahasiswa.nama)
            print("NIM:", mahasiswa.nim)
            print()
            
- Kelas `Jurusan` merepresentasikan objek jurusan dengan atribut `NamaJurusan` dan `DaftarMahasiswa`. Pada metode `__init__`, atribut-atribut tersebut diinisialisasi dengan nilai-nilai awal. `DaftarMahasiswa` diinisialisasi sebagai sebuah list kosong yang akan menampung objek-objek `Mahasiswa`. Kelas ini memiliki metode `tambah_mahasiswa(mahasiswa)` yang digunakan untuk menambahkan objek `Mahasiswa` ke dalam daftar mahasiswa jurusan. Selain itu, kelas ini memiliki metode `tampilkan_daftar_mahasiswa()` yang menampilkan daftar mahasiswa yang terdaftar di jurusan.

class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        # Menambahkan jurusan ke daftar jurusan universitas
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        # Menampilkan daftar jurusan yang terdaftar di universitas
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)
        print()

- Kelas `Universitas` merepresentasikan objek universitas dengan atribut `NamaUniversitas` dan `DaftarJurusan`. Pada metode `__init__`, atribut-atribut tersebut diinisialisasi dengan nilai-nilai awal. `DaftarJurusan` diinisialisasi sebagai sebuah list kosong yang akan menampung objek-objek `Jurusan`. Kelas ini memiliki metode `tambah_jurusan(jurusan)` yang digunakan untuk menambahkan objek `Jurusan` ke dalam daftar jurusan universitas. Selain itu, kelas ini memiliki metode `tampilkan_daftar_jurusan()` yang menampilkan daftar jurusan yang terdaftar di universitas.

Langkah-langkah yang dilakukan dalam kode tersebut adalah sebagai berikut:
1. Membuat objek `Universitas` dengan nama "XYZ University" menggunakan kode `universitas_xyz = Universitas("XYZ University")
2. Membuat objek `Jurusan` dengan nama "Teknik Informatika" menggunakan kode `jurusan_ti = Jurusan("Teknik Informatika")`.
3. Menambahkan objek `Jurusan` yang telah dibuat ke dalam objek `Universitas` menggunakan kode `universitas_xyz.tambah_jurusan(jurusan_ti)`.
4. Membuat objek `Mahasiswa` dengan nama "Damianus Christopher S", nim "G1A022028", dan jurusan yang telah dibuat (`jurusan_ti`) menggunakan kode `mahasiswa1 = Mahasiswa("Damianus Christopher S", "G1A022028", jurusan_ti)`.
5. Menambahkan objek `Mahasiswa` yang telah dibuat ke dalam objek `Jurusan` menggunakan kode `jurusan_ti.tambah_mahasiswa(mahasiswa1)`.
6. Menampilkan daftar jurusan yang terdaftar di objek `Universitas` menggunakan kode `universitas_xyz.tampilkan_daftar_jurusan()`.
7. Menampilkan daftar mahasiswa yang terdaftar di objek `Jurusan` menggunakan kode `jurusan_ti.tampilkan_daftar_mahasiswa()`.
