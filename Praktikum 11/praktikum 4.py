print("PRAKTIKUM 4 - Studi Kasus: Media Sosial")
print("=" * 50)
 
# ── Adjacency List ───────────────────────────────────────────────
# Dictionary: key = nama user, value = list user yang di-follow
graph4 = {
    "Arya" : ["Bella", "Ciko", "Evan"],  # Arya follow Bella, Ciko, Evan
    "Bella": ["Ciko", "Dita"],           # Bella follow Ciko dan Dita
    "Ciko" : ["Fani"],                   # Ciko follow Fani
    "Dita" : ["Arya", "Evan"],           # Dita follow Arya dan Evan
    "Evan" : ["Fani"],                   # Evan follow Fani
    "Fani" : ["Bella"],                  # Fani follow Bella
}
 
# Tampilkan siapa follow siapa
print("\n--- Adjacency List (siapa follow siapa) ---")
for user, following in graph4.items():
    if following:
        print(f"  {user:6s} --> {', '.join(following)}")
    else:
        print(f"  {user:6s} --> (tidak follow siapapun)")
 
# ── Adjacency Matrix ─────────────────────────────────────────────
# Matriks 6x6: baris = user yang follow, kolom = user yang di-follow
# Nilai 1 = ada relasi follow, 0 = tidak ada relasi
 
nodes4 = ["Arya", "Bella", "Ciko", "Dita", "Evan", "Fani"]
n = len(nodes4)
 
# Pemetaan nama -> indeks angka agar bisa mengisi matriks
idx = {name: i for i, name in enumerate(nodes4)}
 
# Inisialisasi matriks 6x6 dengan semua nilai 0
mat4 = [[0] * n for _ in range(n)]
 
# Isi matriks: jika user u follow user v, set mat4[idx[u]][idx[v]] = 1
for u, neighbors in graph4.items():
    for v in neighbors:
        mat4[idx[u]][idx[v]] = 1  # directed: TIDAK dibalik (satu arah)
 
# Tampilkan matriks dengan header nama kolom
print("\n--- Adjacency Matrix (directed follow) ---")
header = [name[:3] for name in nodes4]  # singkat nama jadi 3 huruf untuk header
print("       " + "  ".join(f"{h:3s}" for h in header))
print("       " + "---" * (n * 2 - 1))
for i, row in enumerate(mat4):
    print(f"  {nodes4[i]:6s}|  " + "   ".join(str(v) for v in row))
 
# Penjelasan setiap baris matriks
print("\nPenjelasan baris matrix:")
for i, user in enumerate(nodes4):
    terhubung = [nodes4[j] for j in range(n) if mat4[i][j] == 1]
    if terhubung:
        print(f"  Baris {user:6s}: {user} follow {', '.join(terhubung)}")
    else:
        print(f"  Baris {user:6s}: tidak follow siapapun (semua nilai 0)")