print("--- List - Akses & manipulasi data ---")
print("Slicing data")
data = ["Calvin", 21, "UIB", "Laki-laki", "Programmer", "cokelat"]
print("data awal : ", data)
print("slicing data :", data[1:6:2])

print("\n")
print("append data")
data.append("Makan")
print(data)

print("\n")
print("insert data")
data.insert(2, "Tanjungpinang")
print(data)

print("\n")
print("extend data")
data.extend([2005, "Indonesia"])
print(data)

print("\n")
print("pop data")
data.pop()
print(data)

print("\n")
print("remove data")
data.remove("cokelat")
print(data)

print("\n")
print("--- Tuple - immutability & unpacking ---")
# buat tuple dengan lebih dari sama dengan 5 elemen
data_tuple = ("Calvin", 21, "UIB", "Laki-laki", "Programmer")
print("len tuple : ", len(data_tuple))
print("akses elemen tuple ke-2 : ", data_tuple[1])
print("akses elemen tuple terkahir: ", data_tuple[4])

print("\n")
print("unpacking tuple >= 3 variabel + rest")
name, age, university, *rest = data_tuple
print("name : ", name)
print("age : ", age)
print("university : ", university)
print("rest : ", rest)

print("\n")
print("--- Set – keunikan & operasi himpunan ---")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}\

print("set_a : ", set_a)    
print("set_b : ", set_b)
#union
print("union set_a dan set_b : ", set_a | set_b)

#intersection
print("intersection set_a dan set_b : ", set_a & set_b)

#difference
print("difference set_a dan set_b : ", set_a - set_b)

#symmetric difference
print("symmetric difference set_a dan set_b : ", set_a ^ set_b)

print("\n")
print("--- Dictionary - key-value dasar ---")
mhs = {
    "nama": "Calvin",
    "nim": 2331206,
    "angkatan": "23",
    "kota": "Batam"
}
print("mhs : ", mhs)

print("\n")
print("tambah key")
mhs["jurusan"] = "Teknik Informatika"
print("mhs : ", mhs)

print("ubah nilai key")
mhs["kota"] = "Tanjungpinang"
print("mhs : ", mhs)

print("hapus key")
del mhs["nim"]
print("mhs : ", mhs)

print("\n")
print((mhs.keys()))
print(mhs.values())
print(mhs.items())

print("\nIterasi key: value:")
for k, v in mhs.items():
    print(f"{k}: {v}")

print("\n")
print("--- Nested Structure ---")
buku = [
    {
    "judul": "Harry Potter", 
    "penulis": "J.K. Rowling", 
    "tahun": 1997
    },
    {"judul": "The Lord of the Rings",
    "penulis": "J.R.R. Tolkien",
    "tahun": 1954
    },
    {"judul": "To Kill a Mockingbird",
    "penulis": "Harper Lee",
    "tahun": 1960
    },
    {"judul": "atomic habits",
    "penulis": "James Clear",
    "tahun": 2018
    }
]

#menampilkan semua judul buku
print("Judul buku:")
for b in buku:
    print(b["judul"])

#Filter buku terbit ≥ tahun tertentu menggunakan list comprehension.
tahun_tertentu = 1990
filter_buku = [b for b in buku if b["tahun"] >= tahun_tertentu]
print(f"\nBuku terbit setelah {tahun_tertentu}:")
for b in filter_buku:
    print(b["judul"])


print("\n ---Comprehension & utilitas---")
angka = list(range (1, 21))
print("angka : ", angka)

# list angka genap
genap = [x for x in angka if x % 2 == 0]
print("angka genap : ", genap)

#lisat angka kuadrat
kuadrat = [x**2 for x in angka]
print("angka kuadrat : ", kuadrat)

mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("mapping : ", mapping)

print("\nset comprehension")
kalimat = "Belajar Python itu seru"

huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("huruf unik : ", huruf_unik)

print("\n--- keanggotaan & pencarian sederhana ---")
list= [1, 2, 3, 4, 5, 2]
item=3

ada = item in list
print(f"Apakah {item} ada dalam list? {ada}")

if item in list:
    index = list.index(item)
    print(f"{item} ditemukan di indeks {index}")
else:
    print(f"{item} tidak ditemukan di data")


