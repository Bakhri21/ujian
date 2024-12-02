def tambahBukuBaru():
  global namaBuku
  namaBuku=input("Masukan Judul Buku : ")
  
  global namaPenulis
  namaPenulis=input("Masukan Penulis : ")
  return namaBuku, namaPenulis

def main():
  while True:
    
    buku = [namaBuku, namaPenulis]
    
    totalBuku = []
    totalBuku += [buku]
    print(f"Halo saya Rayhan nurahman dari kelas 1IA16 dan NPM saya 51424177")
    
    for j in range(1):
      print(f"Jumlah Total Buku Saat Ini : {len(totalBuku)}")

    print(f"="*30)
    print(f"Selamat Datang di Sistem Pendataan Perpustakaan")
    print(f"1. Tambah Buku Baru")
    print(f"2. Cek Daftar Buku")
    print(f"3. Hapus Buku")
    print(f"4. Hitung jumlah Buku")
    print(f"5. Exit")
    print(f"="*30)
    
    inputUser = int(input("Masukan Pilihan Menu (1-5): "))
    
    if(inputUser == 1):
      tambahBukuBaru()
      
    elif(inputUser == 2):
      for x in totalBuku:
        print(f"Total Buku : {x}")
      
    elif(inputUser == 3):
      print("Pilihan Tidak Tersedia")
      
    elif(inputUser == 4):
      print("Pilihan Tidak Tersedia")
      
    elif(inputUser == 5):
      print("Pilihan Tidak Tersedia")
      
    else:
      print("Pilihan Tidak Tersedia")

main()