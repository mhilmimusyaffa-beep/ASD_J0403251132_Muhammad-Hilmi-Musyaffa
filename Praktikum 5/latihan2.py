#===============================================================
#Nama   : Muhammad Hilmi Musyaffa
#NIM    : J0403251132
#Kelas  : A1
#==========================================================

#=========================================================
# Latihan 2: Tracing Rekursi
#=========================================================

def countdown(n):
    #[span_4](start_span)base case: jika n sudah mencapai 0, cetak "selesai" dan 
    #hentikan rekursi[span_4](end_span).
 if n == 0:
   print("Selesai")
 return

#Fase Masuk : Dicetak sebelum pemanggilan rekursif berikutnya.
 print("Masuk:", n)
 countdown(n - 1)
 
 #[span_5](start_span)Fase keluar:
 # Dicetak setelah pemanggilan rekursif diatas selesai (saat kembali dari stack)
 # [span_5](end_span)
 print("Keluar:", n)
countdown(3)

#Output keluar muncul dari angka terkecil (1,2,3) karena prisnip kerja stack (LIFO-Last In First Out).
#Ketika countdown(0) mencapai base case, fungsi tersebut selesai dan kontrol kembali ke 
#pemanggil sebeleumnya yaitu countdown(1).
#Baris print(keluar) baru dieksekusi saat fungsi sedang keluar atau selesai dari tumpukan memori.
