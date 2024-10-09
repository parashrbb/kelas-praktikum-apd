# daftar_buku = {
# # key      #vallue
# "Buku1" : "Harry Potter",
# "Buku2" : "Twillight",
# "Buku3" : "Twillight"
# }

# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# # print(daftar_buku)


# Biodata = {
#    "Nama" : "Aldy Ramadhan Syahputra",
#    "NIM" : 2109106079,
#    "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#    "Mahasiswa_Aktif" :True,
#    "Social Media" : {
#       "Instagram" : "@aldyrmdhns_",
#       "Discord" : "Izanami#6848",
#       "Email" : "iniemail@gmail.com"
#    }
# }

# print(Biodata["KRS"][1])
# print(Biodata["Social Media"]["Email"])

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"NIM Saya adalah {Biodata['NIM']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(Biodata["Mahasiswa_Aktif"])

# print(f"nama saya adalah {Biodata.get('Nama')}")
# print(f"NIM Saya adalah {Biodata.get('NIM')}")

# games = dict(Sekiro = "Action", Pokemon = "Adventure", 
# Valorant = {"nama" : {123 : "informatika"}})
# print(games["Valorant"]['nama'])


# Games = {
#     "Game1" : "PUBG Mobile",
#     "Game2" : "Mobile Lagends",
#     "Game3" : {
#         "nama"  : "COC",
#         "genre" : "Strategy"
#     }
# }

# print((Games.get('Game3')).get('genre'))


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")

# #menggunakan items
# for mapel, nilai in Nilai.items():
#     print(f"Nilai {mapel} anda adalah {nilai}")


# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# #Menambahkan
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", 
#              "Upin Ipin" : "Kids", 
#              "COOL FILMS" : "COOL GENRE"})
# #Mengganti
# Film["The Conjuring"] = "serem"
# #DEL(item yang akan dihapus akan betul-betul terhapus dan tidak akan ada lagi sisanya.)
# del Film["Avenger Endgame"]
# #POP(Menyimpan di stock)
# simpan = Film.pop('Hours')
# #Clear (menghapus)
# Film.clear()

# #Setelah Ditambah
# print(Film)

# #Cara mengetahui Jumlah data Dictionary
# print("Jumlah Data = ", len(Film))

# movies = Film.copy()
# print(movies)


# key = "apel", "jeruk", "mangga"
# value = 
# buah = dict.fromkeys(key, value)
# print(buah)


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)


# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }

# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
# print("")


# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }

# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for kiri, kanan in value.items():
#         print  (kiri, " : ", kanan)
#     print("")


# data = {
#     "Nama" : "Muhammad Farras Arhab Ince",
#     "Umur" : 18,
#     "NIM" : 2409106092,
#     "Jurusan" : "Informatika",
#     "Angkatan" : 2024
# }

# data["Hobi"] = input("Masukkan Hobi Anda = ")
# print(data)

# data = {
#     "Matematika" : 90, 
#     "Fisika" : 80,
#     "Biologi" :  80,
#     "Kimia" : 70
# }

# total = 0
# for i in data.values():
#     total += i
# print(f"total nilai anda adalah {total}")
# print(f"Rata Rata nilai anda adalah {total/4}")