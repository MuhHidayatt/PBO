print("Menghitung luas permukaan dan volume limas segitiga")

# variable
alas = 10
tinggi_limas = 8
tinggi_segitiga = 10

# rumus
luas_permukaan = (alas * tinggi_limas) / 2 + 3 * (0.5 * alas * tinggi_segitiga)
volume = (alas ** 2 * tinggi_segitiga) / 6

# Output
print("Alas :", alas)
print("Tinggi Limas :", tinggi_limas)
print("Tinggi Segitiga :", tinggi_segitiga)
print("Luas Permukaan Limas Segitiga: ", luas_permukaan)
print("Volume Limas Segitiga: ", volume)
