# ulang = 3
# for i in range(ulang):
#     print("gantenk")


# simpan = [12, "udin petot", 14.5, True, 'A', "102"]
# for i in simpan:
#     print(i)


# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#         print()


# makanan = ["mie", "sop", "bakso"]
# minuman = ["esteh", "air putih", "es jeruk"]
# for i in makanan:
#     for j in minuman:
#         print(f"{i} & {j}")


# print("Menu Rumah Makan Informatika 24: ")
# print("---------------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
# for i in simpan:
#     print(i)


#cara menambahkan nomor cara 1st
# print("Menu Rumah Makan Informatika 24: ")
# print("--------------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
# for i, menu in enumerate(simpan,start=1):
#     print(f"{i}. {menu}")


#cara menambahkan nomor cara ke 2nd
# print("Menu Rumah Makan Informatika 24: ")
# print("--------------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
# for i in range(len(simpan)):
#     print(f"{i+1}. {simpan[i]}")


# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total perulangan: {hitung}")


# jawab = 'ya'
# hitung = 0
# while(True):
#     hitung += 1
#     jawab = input("baikan lagi tidak? ")
#     if jawab == "ya" or jawab == "iya":
#         break
# print(f"total perulangan: {hitung}")


# print("Daftar bilangan ganjil dari 1-50")
# for i in range(50):
#     if i % 2 == 0:
#         continue
#     print(i)


angka = range(10)
bawah = 0
while(angka == range(10)):
    bawah += 1
    angka = input("angka berapa? ")
print(f"total perulangan : {bawah}")