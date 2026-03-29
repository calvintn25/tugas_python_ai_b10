print("--- Function and class ---")
def greet(nama: str) -> str: #menerima parameter nama dengan tipe data string dan mengembalikan string
    return f"Halo, {nama}!"
    
print(greet("Calvin Tan"))

print("\nfloat:")
def tambah(a: float, b: float = 0.0) -> float: #menerima dua parameter a dan b dengan tipe data float, b memiliki nilai default 0.0, dan mengembalikan float
    return a + b

print(tambah(5.2, 3.5)) 

print("\n--- Rata-rata ---")
def rata_rata(angka: list[float]) -> float: #menerima parameter angka dengan tipe data list yang berisi float dan mengembalikan float
    if not angka: 
        return 0.0
    return round(sum(angka) / len(angka), 2)

print(rata_rata([])) #list kosong, return 0.0   
print(rata_rata([1.5, 2.5, 3.0, 4.0]))

print("\n--- Class ---")
class Student: #mendefinisikan class Mahasiswa
    def __init__(self, nama: str, nim: str, nilai: list[float] | None = None): 
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float) -> None:
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        #memakai fungsi rata rata yang sudah dibuat sebelumnya untuk menghitung rata-rata nilai mahasiswa
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"

    def __str__(self) -> str:
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )

siswa1 = Student("Calvin", "2331206", [40.0, 85.0])    
siswa2 = Student("Jolin", "2331207", [90.0, 95.0])
print(siswa1)
print(siswa2)

print("\n")
if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(tambah(5, 7))
    print(tambah(10))
    print(rata_rata([80, 90, 100]))
    print(rata_rata([]))

    print("\n=== CLASS STUDENT ===")
    siswa1 = Student("Doni", "2412001")
    siswa1.tambah_nilai(80.0)
    siswa1.tambah_nilai(85.0)

    siswa2 = Student("Bayu", "2232035")
    siswa2.tambah_nilai(60.0)
    siswa2.tambah_nilai(65.0)
    siswa2.tambah_nilai(70.0)

    print(siswa1)
    print(f"Rata-rata {siswa1.nama}: {siswa1.rata_nilai()}")
    print(f"Status {siswa1.nama}: {siswa1.status()}")

    print(siswa2)
    print(f"Rata-rata {siswa2.nama}: {siswa2.rata_nilai()}")
    print(f"Status {siswa2.nama}: {siswa2.status()}")
