# ==============================================================================================
# Praktikum 2: Konsep ADT dari File Handling (STUDI KASUS)
# ==============================================================================================

# =========================
# Latihan 1: Load Data
# =========================

nama_file = 'data_mahasiswa.txt'

def baca_data(nama_file):
    data_dict = {}
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            if baris == "":
                continue
            nim, nama, nilai = baris.split(',')
            data_dict[nim] = {
                'nama': nama,
                'nilai': int(nilai)
            }
    return data_dict


# =========================
# Latihan 2: Tampilkan Data
# =========================

def tampilkan_data(data_dict):
    print('\n=== DAFTAR MAHASISWA ===')
    print(f"{'NIM':<10} | {'Nama':<15} | {'Nilai':>5}")
    print('-' * 35)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]['nama']
        nilai = data_dict[nim]['nilai']
        print(f"{nim:<10} | {nama:<15} | {nilai:>5}")

    print('-' * 35)


# =========================
# Latihan 3: Cari Data
# =========================

def cari_data(data_dict):
    nim_cari = input('Masukkan NIM mahasiswa yang ingin dicari: ').strip()

    if nim_cari in data_dict:
        data = data_dict[nim_cari]
        print('\n===== DATA MAHASISWA DITEMUKAN =====')
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {data['nama']}")
        print(f"Nilai : {data['nilai']}")
    else:
        print('Data tidak ditemukan. Pastikan NIM benar.')


# =========================
# Latihan 4: Update Data
# =========================

def ubah_data(data_dict):
    nim = input("Masukkan NIM Mahasiswa yang akan diupdate: ").strip()

    if nim not in data_dict:
        print('NIM tidak ditemukan. Proses update dibatalkan.')
        return

    try:
        nilai_baru = int(input('Masukkan nilai baru (0-100): '))
    except ValueError:
        print('Nilai harus berupa angka.')
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print('Nilai harus antara 0–100.')
        return

    nilai_lama = data_dict[nim]['nilai']
    data_dict[nim]['nilai'] = nilai_baru

    print(f'Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.')


# =========================
# Latihan 5: Simpan Data
# =========================

def simpan_data(nama_file, data_dict):
    with open(nama_file, 'w', encoding='utf-8') as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")

    print('\nData berhasil disimpan ke file:', nama_file)


# =========================
# Menu Interaktif
# =========================

def main():
    buka_data = baca_data(nama_file)

    while True:
        print('\n=== MENU DATA MAHASISWA ===')
        print('1. Tampilkan Data Mahasiswa')
        print('2. Cari Data Berdasarkan NIM')
        print('3. Ubah Nilai Mahasiswa')
        print('4. Simpan Data ke File')
        print('0. Keluar')

        pilihan = input('Pilih menu: ').strip()

        if pilihan == '1':
            tampilkan_data(buka_data)
        elif pilihan == '2':
            cari_data(buka_data)
        elif pilihan == '3':
            ubah_data(buka_data)
        elif pilihan == '4':
            simpan_data(nama_file, buka_data)
        elif pilihan == '0':
            print('Program selesai.')
            break
        else:
            print('Pilihan tidak valid. Coba lagi.')


# =========================
# Jalankan Program
# =========================

main()
