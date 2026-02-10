print('====Membuka file dalam satu string====')
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    isi_file = file.read()
print(isi_file)
print('==== Hasil ===')
print('tipe data :', type(isi_file))

 #================================================================       
 #Praktikum 1: Konsep ADT dan file Handling
 #Latihan dasar 1: Membuka file perbaris
 #================================================================

print('====Membuka file Per Baris====')
jumlah_baris= 0
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilang karakter baris baru
        print('baris ke-', jumlah_baris)
        print('isinya :', baris)
        
 #================================================================       
 #Praktikum 1: Konsep ADT dan file Handling
 #Latihan dasar 2: Memparsing baris menjadi data satuan dan menampilkannya dalam bentuk kolo,-kolom data
 #================================================================
        
#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom-kolom data

jumlah_baris = 0 
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(',') #pecah menjadi data satuan dan simpan ke variabel
        print ('NIM :', nim, '| Nama :', nama, '| Nilai :', nilai) #Menampilkan satuan data dalam bentuk kolom
        
 #================================================================       
 #Praktikum 1: Konsep ADT dan file Handling
 #Latihan dasar 3: Membaca data dan menyimpannya ke struktur data list
 #================================================================
 
data_list = [] #inisialisasi list untuk menampung data

with open('data_mahasiswa.txt', 'r',encoding='utf-8') as file:
    for baris in file :
        baris = baris.strip() 
        nim, nama, nilai = baris.split(',') #Pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)]) #Menyimpan data ke list 
print('=== Menampilkan list ===')
print(data_list)
print('contoh record ke-1', data_list[0])
print('contoh record ke-2', data_list[1])
print('jumlah record', len(data_list))

 #================================================================       
 #Praktikum 1: Konsep ADT dan file Handling
 #Latihan dasar 4: Membaca data dan menyimpannya ke struktur data dictionary
 #================================================================
 
data_dict = {} #Inisialisasi dictionary
with open('data_mahasiswa.txt', 'r',encoding='utf-8') as file:
    for baris in file :
        baris = baris.strip() 
        nim, nama, nilai = baris.split(',') #Pecah menjadi data satuan dan simpan ke variabel
        #Simpan data dalam dictionary (key, value)
        data_dict[nim] = {
            'nama' : nama,
            'nilai' : int(nilai)
        }
print ('=== Menampilkan Data Dictionary ===')
print(data_dict)
        
 
        
        