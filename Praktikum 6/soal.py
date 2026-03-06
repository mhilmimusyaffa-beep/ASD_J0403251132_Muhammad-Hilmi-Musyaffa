def bubbleSortDescending(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i] < data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

# data nilai tes
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# simpan data asli untuk mengetahui nomor kandidat
data_asli = data.copy()

# urutkan nilai dari tertinggi ke terendah
bubbleSortDescending(data)

print("Data nilai setelah diurutkan (descending):")
print(data)

# ambil 5 nilai tertinggi
lima_tertinggi = data[:5]

print("\nLima skor tertinggi:")
print(lima_tertinggi)

print("\nKandidat yang lolos:")

for nilai in lima_tertinggi:
    kandidat = data_asli.index(nilai) + 1
    print("Kandidat ke-", kandidat, "dengan nilai", nilai)
#penjelasan:
#Data nilai diurutkan secara descending menggunakan algoritma sorting untuk 
#mendapatkan nilai tertinggi. 
#Hasilnya, lima nilai tertinggi adalah 98, 89, 76, 68, dan 57. 
#Nilai tersebut dimiliki oleh kandidat ke-7, ke-4, ke-2, ke-9, dan ke-6, 
#sehingga kelima kandidat tersebut dinyatakan lolos seleksi.
