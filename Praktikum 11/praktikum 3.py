# PRAKTIKUM 3 - Konversi Adjacency Matrix ke Adjacency List
# ================================================================
# Matrix yang diberikan (4 node, undirected):
#   Node 0 terhubung ke 1 dan 2
#   Node 1 terhubung ke 0 dan 2
#   Node 2 terhubung ke 0, 1, dan 3
#   Node 3 terhubung ke 2
 
print("\n" + "=" * 50)
print("PRAKTIKUM 3 - Konversi Matrix ke Adjacency List")
print("=" * 50)
 
# Adjacency matrix yang akan dikonversi (sudah diberikan di soal)
matrix3 = [
    [0, 1, 1, 0],  # node 0: terhubung ke 1, 2
    [1, 0, 1, 0],  # node 1: terhubung ke 0, 2
    [1, 1, 0, 1],  # node 2: terhubung ke 0, 1, 3
    [0, 0, 1, 0],  # node 3: terhubung ke 2
]
 
# Tampilkan matrix asal sebelum dikonversi
print("\nAdjacency Matrix asal:")
print("   ", end="")
for col in range(4):
    print(f" {col}", end="")
print()
for i, baris in enumerate(matrix3):
    print(f" {i} |", end="")
    for val in baris:
        print(f" {val}", end="")
    print()
 
# Fungsi konversi matrix ke adjacency list
def matrix_ke_list(matrix):
    V = len(matrix)                    # jumlah node = panjang matrix
    adj = {i: [] for i in range(V)}   # buat dictionary kosong untuk tiap node
 
    for i in range(V):        # loop baris (node asal)
        for j in range(V):    # loop kolom (node tujuan)
            if matrix[i][j] == 1:     # jika ada edge (nilai = 1)
                adj[i].append(j)      # tambahkan j sebagai tetangga i
 
    return adj
 
# Jalankan konversi
adj3 = matrix_ke_list(matrix3)
 
# Tampilkan hasil adjacency list
print("\nHasil Konversi -> Adjacency List:")
for node, tetangga in adj3.items():
    print(f"  Node {node} --> {tetangga}")
    # Contoh: Node 2 --> [0, 1, 3] artinya node 2 terhubung ke 0, 1, dan 3
 