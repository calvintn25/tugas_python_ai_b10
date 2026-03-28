print("--- Deklarasi Variabel dan Tipe Data --- ")
#Variabel String
a = "Hello World"

#Variabel Integer
b = 10

#Variabel Float
c = 3.14

#Variable Boolean
d = True
#variable List
e = [1, 2, 3, 4, 5]

#Print variable
print(a)
print(b)
print(c)
print(d)
print(e)

print("\n")
print("---Manipulasi String---")
f = "Python Programming"
print(f.upper()) #Mengubah menjadi huruf besar
print(f.lower()) #Mengubah menjadi huruf kecil
print(len(f)) #Menghitung panjang string

print("\n")
print("---Operasi Matematika---")
a = 20
b = 5

print(a + b) #Penjumlahan
print(a - b) #Pengurangan
print(a * b) #Perkalian
print(a / b) #Pembagian
print(a//b) #Pembagian dengan pembulatan ke bawah
print(a % b) #Sisa pembagian

print("\n")
print("---List dan Akses Elemen---")
Buah = ["apel", "jeruk", "pisang", "mangga", "durian"]

# tampilkan salah satu elemen
print(Buah[0]) #akses elemen pertama
print(Buah[2]) #akses elemen ketiga

#Menambahkan elemen ke dalam list
Buah.append("semangka")
print(Buah)

#menghapus elemen dari list
Buah.pop(1)
print(Buah)

print("\n")
print("---Penggunaan Input dari User---")
nama = input("Masukkan nama Anda: ")
umur = input("Masukkan umur Anda: ")
print("Halo, nama saya " + nama + "! " + "dan saya berumur " + umur + " tahun.")