# ============================================================
# Tugas 3 - Dasar Pemrograman Python
# ============================================================

# ============================================================
# 1. DEKLARASI VARIABEL DAN TIPE DATA
# ============================================================
nama_kota   = "Bandung"          # string
jumlah_hari = 7                  # integer
nilai_pi    = 3.14159            # float
is_pelajar  = True               # boolean
mata_pelajaran = [               # list
    "Matematika",
    "Fisika",
    "Kimia",
    "Biologi",
    "Bahasa Indonesia"
]

print("=" * 50)
print("1. VARIABEL DAN TIPE DATA")
print("=" * 50)
print(f"Nama kota    : {nama_kota}  -> tipe: {type(nama_kota)}")
print(f"Jumlah hari  : {jumlah_hari}     -> tipe: {type(jumlah_hari)}")
print(f"Nilai pi     : {nilai_pi} -> tipe: {type(nilai_pi)}")
print(f"Is pelajar   : {is_pelajar}  -> tipe: {type(is_pelajar)}")
print(f"Mata pelajaran: {mata_pelajaran} -> tipe: {type(mata_pelajaran)}")

# ============================================================
# 2. MANIPULASI STRING
# ============================================================
print("\n" + "=" * 50)
print("2. MANIPULASI STRING")
print("=" * 50)

sapaan = "Halo"
nama_depan = "Andi"
nama_belakang = "Pratama"

# Menggabungkan string (concatenation)
nama_lengkap = nama_depan + " " + nama_belakang
print(f"Nama lengkap  : {nama_lengkap}")

# Menghitung panjang string
print(f"Panjang nama  : {len(nama_lengkap)} karakter")

# Mengubah ke huruf besar dan kecil
print(f"Huruf besar   : {nama_lengkap.upper()}")
print(f"Huruf kecil   : {nama_lengkap.lower()}")

# Menggabungkan sapaan dengan nama
kalimat = sapaan + ", " + nama_lengkap + "! Selamat datang di kota " + nama_kota + "."
print(f"Kalimat       : {kalimat}")

# ============================================================
# 3. OPERASI MATEMATIKA SEDERHANA
# ============================================================
print("\n" + "=" * 50)
print("3. OPERASI MATEMATIKA SEDERHANA")
print("=" * 50)

a = 20
b = 6

print(f"a = {a}, b = {b}")
print(f"Penjumlahan    (a + b)  = {a + b}")
print(f"Pengurangan    (a - b)  = {a - b}")
print(f"Perkalian      (a * b)  = {a * b}")
print(f"Pembagian      (a / b)  = {a / b:.4f}")
print(f"Pembagian bulat(a // b) = {a // b}")
print(f"Modulus/Sisa   (a % b)  = {a % b}")

# ============================================================
# 4. LIST DAN AKSES ELEMEN
# ============================================================
print("\n" + "=" * 50)
print("4. LIST DAN AKSES ELEMEN")
print("=" * 50)

buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Semangka"]
print(f"List awal       : {buah}")

# Akses elemen tertentu
print(f"Elemen pertama  : {buah[0]}")
print(f"Elemen terakhir : {buah[-1]}")
print(f"Elemen ke-3     : {buah[2]}")

# Tambah item baru
buah.append("Anggur")
print(f"Setelah append  : {buah}")

# Hapus item
buah.remove("Jeruk")
print(f"Setelah remove  : {buah}")

# Hapus item dengan pop (elemen terakhir)
item_dihapus = buah.pop()
print(f"Item di-pop     : {item_dihapus}")
print(f"List akhir      : {buah}")

# ============================================================
# 5. INPUT DARI USER
# ============================================================
print("\n" + "=" * 50)
print("5. INPUT DARI USER")
print("=" * 50)

nama_user = input("Masukkan nama Anda : ")
umur_user = input("Masukkan umur Anda : ")

print(f"\nHalo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
print("Senang bertemu dengan Anda!")
print("=" * 50)
