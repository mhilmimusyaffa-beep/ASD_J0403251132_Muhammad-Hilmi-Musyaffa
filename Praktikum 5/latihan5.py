#===============================================================
#Nama   : Muhammad Hilmi Musyaffa
#NIM    : J0403251132
#Kelas  : A1
#==========================================================

#=========================================================
# Latihan 5: Generator Pin
#=========================================================

def buat_pin(panjang, hasil=""):
# [span_13](start_span)Base case: Jika panjang PIN yang diinginkan tercapai
# [span_13](end_span).
 if len(hasil) == panjang:
  print("PIN:", hasil)
 return
# [span_14](start_span)Loop untuk mencoba setiap angka (0, 1, 2)
# pada posisi saat ini[span_14](end_span).

 for angka in ["0", "1", "2"]:
     # Teknik backtracking: Membangun PIN secara bertahap.
 buat_pin(panjang, hasil + angka)
buat_pin(3)

#Untuk mencegah angka yang sama muncul berulang dalam satu PIN sehingga setiap digit bersifat unik, 
#kita dapat menambahkan pengecekan kondisi sebelum melakukan pemanggilan rekursi, 
#yaitu dengan menggunakan if angka not in hasil:. Kondisi ini memastikan bahwa angka yang akan ditambahkan 
#ke dalam variabel hasil belum pernah digunakan sebelumnya pada kombinasi yang sedang dibentuk. 
#Jika angka tersebut sudah ada di dalam hasil, maka angka itu akan dilewati dan tidak diproses lebih lanjut. 
#Dengan cara ini, setiap kombinasi PIN yang dihasilkan tidak akan mengandung pengulangan digit dalam satu susunan, 
# sehingga metode backtracking hanya mengeksplorasi kemungkinan yang valid saja.