#===============================================================
#Nama   : Muhammad Hilmi Musyaffa
#NIM    : J0403251132
#Kelas  : A1
#==========================================================

#=========================================================
# Latihan 4: Kombinasi Huruf
#=========================================================

def kombinasi(n, hasil=""):
    #[span_10](start_span)Base case: jika panjang string hasil sudah sama dengan n, 
    #cetak hasilnya[span_10](end_span)
 if len(hasil) == n:
  print(hasil)
 return

#Explore: Mencoba menambahkan huruf 'A' lalu mengeksplorasi kemungkinannya.

 kombinasi(n, hasil + "A")
 #[span_11](start_span)Explore: Mencoba menambahkan huruf 'B' setelah jalur 'A'
#selesai dieksplorasi[span_11](end_span).

 kombinasi(n, hasil + "B")
kombinasi(2)

#jumlah kombinasi yang dihasilkan ditentukan oleh rumus 2^n. karena setiap posisi memiliki 2 pilihan
# (A atau B), maka untuk n=2 dihasilkan 2^2 = 4 kombinasi (AA, AB, BA, BB).
#struktur ini membentuk pohon keputusan di mana setiap level mewakili satu digit huruf.