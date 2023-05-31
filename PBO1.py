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


# Langkah 2: Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# Langkah 3: Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke universitas_xyz
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

# Langkah 4: Membuat objek Mahasiswa dengan nama, nim, dan jurusan tertentu dan menambahkannya ke jurusan_ti
mahasiswa1 = Mahasiswa("Damianus Christopher S", "G1A022028", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa1)

# Langkah 5: Menampilkan daftar jurusan di universitas_xyz
universitas_xyz.tampilkan_daftar_jurusan()

# Langkah 6: Menampilkan daftar mahasiswa di jurusan_ti
jurusan_ti.tampilkan_daftar_mahasiswa()
