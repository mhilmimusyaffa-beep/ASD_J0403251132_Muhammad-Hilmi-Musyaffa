print("PRAKTIKUM 1 - Adjacency Matrix")
print("=" * 50)
 
# Fungsi untuk membuat adjacency matrix
def buat_matrix(V, edges):
    # Buat matriks V x V, semua sel diisi 0 (belum ada edge)
    mat = [[0 for _ in range(V)] for _ in range(V)]
 
    # Loop setiap edge [u, v] yang diberikan
    for u, v in edges:
        mat[u][v] = 1  # tandai ada edge dari u ke v
        mat[v][u] = 1  # karena undirected, tandai juga arah baliknya
 
    return mat  # kembalikan matriks yang sudah terisi
 
# Jumlah vertex (node) = 4, yaitu node 0, 1, 2, 3
V1 = 4
 
# Daftar edge yang menghubungkan antar node
edges1 = [[0, 1], [0, 2], [1, 2], [2, 3]]
 
# Buat matriks menggunakan fungsi di atas
mat1 = buat_matrix(V1, edges1)
 
# Tampilkan header kolom (0, 1, 2, 3)
print("\nAdjacency Matrix (node 0-3):")
print("   ", end="")
for col in range(V1):
    print(f" {col}", end="")
print()
print("   " + "--" * V1)  # garis pemisah
 
# Tampilkan isi matriks baris per baris
for i in range(V1):
    print(f" {i} |", end="")  # label baris (nomor node)
    for j in range(V1):
        print(f" {mat1[i][j]}", end="")  # 1 jika ada edge, 0 jika tidak
    print()
 
# Penjelasan arti setiap baris matriks
print()
print("Penjelasan setiap baris:")
penjelasan = {
    0: "Node 0 terhubung ke node 1 dan 2  -> baris 0 bernilai 1 di kolom 1 dan 2",
    1: "Node 1 terhubung ke node 0 dan 2  -> baris 1 bernilai 1 di kolom 0 dan 2",
    2: "Node 2 terhubung ke node 0, 1, 3  -> baris 2 bernilai 1 di kolom 0, 1, dan 3",
    3: "Node 3 terhubung ke node 2 saja   -> baris 3 bernilai 1 di kolom 2",
}
for node, ket in penjelasan.items():
    print(f"  Baris {node}: {ket}")


