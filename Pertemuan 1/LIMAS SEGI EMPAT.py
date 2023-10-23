print("Menghitung luas permukaan dan volume limas segi empat")

# variable
sisi_alas = 5
tinggi_limas = 8
tinggi_segitiga = 6

# rumus
luas_permukaan = (sisi_alas ** 2) + 2 * sisi_alas * (tinggi_limas + tinggi_segitiga)
volume = (sisi_alas ** 2 * tinggi_limas) / 3

# output
print("Sisi Alas :", sisi_alas)
print("Tinggi Limas :", tinggi_limas)
print("Tinggi Segitiga :", tinggi_segitiga)
print("Luas Permukaan Limas Segi Empat: ", luas_permukaan)
print("Volume Limas Segi Empat: ", volume)
