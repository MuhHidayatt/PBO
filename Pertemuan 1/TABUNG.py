print("Menghitung luas permukaan dan volume tabung")

# variable
jari_jari = 7
tinggi = 10

# Mengimport nilai pi
from math import pi

# rumus
luas_permukaan = 2 * pi * jari_jari * (jari_jari + tinggi)
volume = pi * (jari_jari ** 2) * tinggi

# output
print("Jari-jari :", jari_jari)
print("Tinggi :", tinggi)
print("Luas Permukaan Tabung: ", luas_permukaan)
print("Volume Tabung: ", volume)
