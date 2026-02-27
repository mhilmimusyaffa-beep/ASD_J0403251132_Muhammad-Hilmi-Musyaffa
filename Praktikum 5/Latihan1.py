#===============================================================
#Nama   : Muhammad Hilmi Musyaffa
#NIM    : J0403251132
#Kelas  : A1
#==========================================================

#=========================================================
# Latihan 1: Rekursi Pangkat
#=========================================================

def pangkat(a, n):
 # Base case = Kondisi berhenti (span_1)
 #(start_span) jika n adalah 0, maka angka 
 # apapun dipangkatkan 0 hasilnya 1(span_1)
#(end_span).
 if n == 0:
    return 1

#(span_2)(start_span)
 # Recursive case = Memanggil dirinya sendiri dengan
 #mengurangi nilai n (eksponen)[span_2]
 #(end_span)
 #Rumus: a^n = a*a^(n-1)


 return a * pangkat(a, n - 1)
#Mencetak hasil pemangkatan 2 pangkat 4 
print(pangkat(2, 4)) # Output: 16

#1. Alur program memanggil pangkat yaitu 2 dan 4 lalu masuk
#   ke stack rekursi
# 2*pangkat(2,3) -> 2*pangkat(2,2) -> 2*pangkat(2,1) -> 2*pangkat (2,0).
#2. Base case terjadi saat n==0, yang akan mengembalikan nilai 1
#3. Recursive call berfungsi memanggil dirinya sendiri dengan parameter (a, n-1)
#   sampai mencapai base case, lalu hasilnya dikalikan saat unwinding stack.