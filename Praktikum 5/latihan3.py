#===============================================================
#Nama   : Muhammad Hilmi Musyaffa
#NIM    : J0403251132
#Kelas  : A1
#==========================================================

#=========================================================
# Latihan 3: Mencari Nilai Maksimum
#=========================================================

def cari_maks(data, index=0):
    #[span_7](start_span)base case: jika index berada di elemen terakhir, 
    #kembalikan elemen tersebut[span_7](end_span).
 # Base case
 if index == len(data) - 1:
  return data[index]

#[span_8](start_span)Recursive case:
# Mencari nilai maksimum di sisa list(index +)
# 1)[span_8](end_span).

 maks_sisa = cari_maks(data, index + 1)
 #Membandingkan elemen saat ini dengan nilai maksimum yang ditemukan dari sisa list.
 if data[index] > maks_sisa:
  return data[index]
 else:
  return maks_sisa
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

#Alur Program berfungsi menelusuri list dari depan ke belakang sampai index terakhir (base case).
#Perbandingan: Setelah mencapai akhir list, fungsi kembali ke atas (backtrack) sambil 
#membandingkan angka di index saat ini dengan angka terbesar yang ditemukan di "sisa" list.
#Base Case: Terjadi saat index == len(data) - 1, memastikan rekursi tidak 'out of bounds'.