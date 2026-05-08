# PRAKTIKUM 2 - Adjacency List menggunakan Dictionary
# ================================================================
# Bentuk graph (undirected):
#   A -- B
#   |    |
#   C -- D
#
# Edge: A-B, A-C, B-D, C-D
 
print("\n" + "=" * 50)
print("PRAKTIKUM 2 - Adjacency List")
print("=" * 50)
 
# Dictionary: setiap key adalah node, value adalah list tetangganya
graph2 = {
    'A': ['B', 'C'],  # A terhubung ke B dan C
    'B': ['A', 'D'],  # B terhubung ke A dan D
    'C': ['A', 'D'],  # C terhubung ke A dan D
    'D': ['B', 'C'],  # D terhubung ke B dan C
}
 
# Tampilkan adjacency list: node: tetangga1 tetangga2
print("\nAdjacency List Representation:")
for node, tetangga in graph2.items():
    print(f"{node}: ", end="")   # cetak nama node diikuti titik dua
    for t in tetangga:
        print(t, end=" ")        # cetak setiap tetangga dipisah spasi
    print()                      # pindah baris setelah semua tetangga dicetak