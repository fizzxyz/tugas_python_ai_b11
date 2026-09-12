# ============================================================
# Tugas 5 - Function & Class
# ============================================================


# ============================================================
# FUNCTIONS
# ============================================================

def greet(nama: str) -> str:
    """Mengembalikan teks sapaan."""
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b


def rata_rata(angka: list) -> float:
    """
    Mengembalikan rata-rata dari list angka.
    Jika list kosong, kembalikan 0.0.
    """
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


# ============================================================
# CLASS
# ============================================================

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama  = nama
        self.nim   = nim
        self.nilai = []

    def tambah_nilai(self, skor: float):
        """Menambah satu nilai ke list nilai."""
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """Mengembalikan rata-rata nilai menggunakan fungsi rata_rata()."""
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """Mengembalikan 'LULUS' jika rata-rata >= threshold, selain itu 'TIDAK LULUS'."""
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )


# ============================================================
# DEMO
# ============================================================

if __name__ == "__main__":

    # ----------------------------------------------------------
    print("=" * 45)
    print("=== FUNCTIONS ===")
    print("=" * 45)

    # greet()
    print(greet("Arifian"))

    # tambah()
    print(f"tambah(5, 7)  = {tambah(5, 7)}")
    print(f"tambah(10)    = {tambah(10)}")

    # rata_rata()
    print(f"rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"rata_rata([])            = {rata_rata([])}")

    # ----------------------------------------------------------
    print("\n" + "=" * 45)
    print("=== CLASS STUDENT ===")
    print("=" * 45)

    # Mahasiswa 1
    mhs1 = Student("Budi Santoso", "A001")
    mhs1.tambah_nilai(85)
    mhs1.tambah_nilai(90)
    mhs1.tambah_nilai(78)
    mhs1.tambah_nilai(92)
    print(f"\nMahasiswa 1  : {mhs1}")
    print(f"  Rata-rata  : {mhs1.rata_nilai()}")
    print(f"  Status     : {mhs1.status()}")

    # Mahasiswa 2
    mhs2 = Student("Sari Dewi", "A002")
    mhs2.tambah_nilai(55)
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(65)
    print(f"\nMahasiswa 2  : {mhs2}")
    print(f"  Rata-rata  : {mhs2.rata_nilai()}")
    print(f"  Status     : {mhs2.status()}")

    print("\n" + "=" * 45)
    print("Program selesai!")
    print("=" * 45)
