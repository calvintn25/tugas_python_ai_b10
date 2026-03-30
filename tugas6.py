import numpy as np
import pandas as pd
import os
 
np.random.seed(42)  # set seed agar output konsisten

nilai = np.array([78,85,92,67,88,73,90,95, 87, 70])
rata_rata = np.mean(nilai)
median = np.median(nilai)
standard_deviasi = np.std(nilai)
min = np.min(nilai)
max = np.max(nilai)

#Buat DataFrame dengan kolom minimal: nama, nim, nilai.
nilai_subset = nilai[:5]
data = {
    "nama": ["Calvin", "Jolin", "Doni", "Bayu", "Budi"],
    "nim": ["2331206", "2331207", "2412001", "2232035", "2331208"],
    "nilai": nilai_subset # ambil 5 nilai pertama untuk dimasukkan ke DataFrame
}

df = pd.DataFrame(data)
df["status"] = np.where(df["nilai"] >= 70, "LULUS", "TIDAK LULUS")

print(df.head())

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def average(self) -> float:
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float: #Persentase lulus
        total = len(self.df)
        if total == 0:
            return 0.0
        lulus = (self.df["nilai"] >= threshold).sum()
        return (float(lulus) / total) * 100.0

    def save_summary(self, path: str) -> None:
        total = len(self.df)
        lulus = (self.df["nilai"] >= 70).sum()
        tidak_lulus = total - int(lulus)

        lines = [
            "=== Ringkasan GradeBook ===",
            f"Jumlah data: {total}",
            f"Rata-rata nilai: {self.average()}",
            f"Persentase lulus (>=70): {self.pass_rate()}%",
            f"Jumlah lulus: {int(lulus)}",
            f"Jumlah tidak lulus: {tidak_lulus}",
            "",
        ]

        with open(path, "a", encoding="utf-8") as file:
            if os.path.exists(path) and os.path.getsize(path) > 0:
                file.write("\n")
            file.write("\n".join(lines))

    def __str__(self) -> str:
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average():.2f})"


if __name__ == "__main__":
    print("=== NUMPY ===")
    print("Nilai:", nilai)
    print("Rata-rata:" , rata_rata)
    print("Median:", median)
    print("Standard Deviasi:", standard_deviasi)
    print("Nilai Minimum:", min)
    print("Nilai Maximum:", max)

    print("\n=== PANDAS ===")
    df = pd.DataFrame(data)
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    grade_book = GradeBook(df)
    print(grade_book)
    print(f"Average: {grade_book.average():.2f}")
    print(f"Pass rate: {grade_book.pass_rate():.2f}%")
    grade_book.save_summary("ringkasan_tugas6.txt")
    print("Ringkasan GradeBook ditulis ke ringkasan_tugas6.txt")