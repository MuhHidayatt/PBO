print("Menghitung luas permukaan dan volume prisma segitiga")

# variable
alas_segitiga = 6
tinggi_segitiga = 4
tinggi_prisma = 8

# rumus luas permukaan prisma segitiga
luas_permukaan = (alas_segitiga * tinggi_prisma) + 2 * (0.5 * alas_segitiga * tinggi_segitiga)

# rumus volume prisma segitiga
volume = 0.5 * alas_segitiga * tinggi_segitiga * tinggi_prisma

# output
print("Alas Segitiga :", alas_segitiga)
print("Tinggi Segitiga :", tinggi_segitiga)
print("Tinggi Prisma :", tinggi_prisma)
print("Luas Permukaan Prisma Segitiga: ", luas_permukaan)
print("Volume Prisma Segitiga: ", volume)
