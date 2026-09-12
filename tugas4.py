# ============================================================
# Tugas 4 - List, Tuple, Set, Dictionary & Structures
# ============================================================

# ============================================================
# 1. LIST – AKSES & MANIPULASI
# ============================================================
print("=" * 55)
print("1. LIST – AKSES & MANIPULASI")
print("=" * 55)

data = ["Python", 42, "JavaScript", 3.14, True, "Kotlin", 99]
print(f"List awal       : {data}")
print(f"Elemen pertama  : {data[0]}")
print(f"Elemen terakhir : {data[-1]}")

# Slicing [start:stop:step]
print(f"Slicing [1:6:2] : {data[1:6:2]}")
print(f"Slicing [::2]   : {data[::2]}")
print(f"Slicing [1:4]   : {data[1:4]}")

# append()
data.append("Dart")
print(f"\nSetelah append('Dart')    : {data}")

# insert()
data.insert(2, "TypeScript")
print(f"Setelah insert(2, 'TS')   : {data}")

# extend()
data.extend([100, 200])
print(f"Setelah extend([100,200]) : {data}")

# pop()
item_pop = data.pop()
print(f"\nSetelah pop()  (hapus '{item_pop}'): {data}")

# remove()
data.remove(True)
print(f"Setelah remove(True)      : {data}")

# ============================================================
# 2. TUPLE – IMMUTABILITY & UNPACKING
# ============================================================
print("\n" + "=" * 55)
print("2. TUPLE – IMMUTABILITY & UNPACKING")
print("=" * 55)

profil = ("Andi", 21, "Bandung", "Informatika", "IPK: 3.85")
print(f"Tuple           : {profil}")
print(f"Panjang (len)   : {len(profil)}")
print(f"Indeks ke-0     : {profil[0]}")
print(f"Indeks ke-2     : {profil[2]}")

# Unpacking dengan *rest
nama, umur, *rest = profil
print(f"\nUnpacking:")
print(f"  nama  = {nama}")
print(f"  umur  = {umur}")
print(f"  *rest = {rest}")

# Tuple immutable – tidak bisa diubah
try:
    profil[0] = "Budi"
except TypeError as e:
    print(f"\nPercobaan ubah tuple -> ERROR: {e}")

# ============================================================
# 3. SET – KEUNIKAN & OPERASI HIMPUNAN
# ============================================================
print("\n" + "=" * 55)
print("3. SET – KEUNIKAN & OPERASI HIMPUNAN")
print("=" * 55)

# Duplikat otomatis dihilangkan
set_a = {1, 2, 3, 4, 5, 3, 2, 1}   # ada duplikat
set_b = {3, 4, 5, 6, 7, 8}

print(f"set_a (input ada duplikat): {{1,2,3,4,5,3,2,1}} -> {set_a}")
print(f"set_b                     : {set_b}")

print(f"\nUnion (|)              : {set_a | set_b}")
print(f"Intersection (&)       : {set_a & set_b}")
print(f"Difference a-b (-)     : {set_a - set_b}")
print(f"Difference b-a (-)     : {set_b - set_a}")
print(f"Symmetric diff (^)     : {set_a ^ set_b}")

# ============================================================
# 4. DICTIONARY – KEY/VALUE DASAR
# ============================================================
print("\n" + "=" * 55)
print("4. DICTIONARY – KEY/VALUE DASAR")
print("=" * 55)

mahasiswa = {
    "nama"    : "Rizky Pratama",
    "nim"     : "2024001",
    "angkatan": 2024,
    "kota"    : "Surabaya"
}
print(f"Dict awal: {mahasiswa}")

# Tambah key baru
mahasiswa["jurusan"] = "Teknik Informatika"
print(f"\nSetelah tambah 'jurusan' : {mahasiswa}")

# Ubah nilai
mahasiswa["kota"] = "Yogyakarta"
print(f"Setelah ubah 'kota'      : {mahasiswa}")

# Hapus key
del mahasiswa["angkatan"]
print(f"Setelah hapus 'angkatan' : {mahasiswa}")

print(f"\nkeys()   : {list(mahasiswa.keys())}")
print(f"values() : {list(mahasiswa.values())}")
print(f"items()  : {list(mahasiswa.items())}")

print("\nIterasi key: value")
for key, value in mahasiswa.items():
    print(f"  {key}: {value}")

# ============================================================
# 5. NESTED STRUCTURES
# ============================================================
print("\n" + "=" * 55)
print("5. NESTED STRUCTURES")
print("=" * 55)

daftar_buku = [
    {"judul": "Laskar Pelangi",        "penulis": "Andrea Hirata",  "tahun": 2005},
    {"judul": "Bumi Manusia",          "penulis": "Pramoedya A.T.", "tahun": 1980},
    {"judul": "Perahu Kertas",         "penulis": "Dee Lestari",    "tahun": 2009},
    {"judul": "Negeri 5 Menara",       "penulis": "A. Fuadi",       "tahun": 2009},
    {"judul": "Pulang",                "penulis": "Tere Liye",      "tahun": 2015},
    {"judul": "Filosofi Kopi",         "penulis": "Dee Lestari",    "tahun": 2006},
]

print("Semua judul buku:")
for buku in daftar_buku:
    print(f"  - {buku['judul']} ({buku['tahun']})")

# Filter buku terbit >= 2009 dengan list comprehension
tahun_filter = 2009
buku_baru = [b["judul"] for b in daftar_buku if b["tahun"] >= tahun_filter]
print(f"\nBuku terbit >= {tahun_filter} (list comprehension):")
for judul in buku_baru:
    print(f"  - {judul}")

# ============================================================
# 6. COMPREHENSION & UTILITAS
# ============================================================
print("\n" + "=" * 55)
print("6. COMPREHENSION & UTILITAS")
print("=" * 55)

angka_1_20 = list(range(1, 21))

# List comprehension – bilangan genap
list_genap = [x for x in angka_1_20 if x % 2 == 0]
print(f"List genap (1-20)    : {list_genap}")

# List comprehension – kuadrat
list_kuadrat = [x ** 2 for x in angka_1_20]
print(f"List kuadrat (1-20)  : {list_kuadrat}")

# Dict comprehension – genap/ganjil 1–10
dict_genap_ganjil = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print(f"\nDict genap/ganjil    : {dict_genap_ganjil}")

# Set comprehension – huruf unik lowercase dari kalimat
kalimat = "Belajar Python Itu Menyenangkan"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print(f"\nKalimat              : '{kalimat}'")
print(f"Huruf unik lowercase : {huruf_unik}")

# ============================================================
# 7. KEANGGOTAAN & PENCARIAN SEDERHANA
# ============================================================
print("\n" + "=" * 55)
print("7. KEANGGOTAAN & PENCARIAN SEDERHANA")
print("=" * 55)

bahasa = ["Python", "JavaScript", "Kotlin", "Dart", "TypeScript"]
set_bahasa = {"Python", "Go", "Rust", "Java"}

# Cek keanggotaan dengan 'in'
cari = "Python"
print(f"'{cari}' in list bahasa     : {cari in bahasa}")
print(f"'{cari}' in set_bahasa      : {cari in set_bahasa}")

cari2 = "Ruby"
print(f"'{cari2}' in list bahasa    : {cari2 in bahasa}")

# index() untuk posisi
if cari in bahasa:
    print(f"Posisi '{cari}' di list   : index {bahasa.index(cari)}")

# Pencarian dalam dictionary
kata_kunci = "nama"
print(f"\n'{kata_kunci}' in mahasiswa (dict) : {kata_kunci in mahasiswa}")
kata_kunci2 = "angkatan"
print(f"'{kata_kunci2}' in mahasiswa (dict) : {kata_kunci2 in mahasiswa}")

print("\n" + "=" * 55)
print("Program selesai!")
print("=" * 55)
