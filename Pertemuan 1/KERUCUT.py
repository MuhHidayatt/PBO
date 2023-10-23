print("Menghitung luas permukaan dan volume kerucut")

# variable
jari_jari = 7
tinggi = 8
garis_pelukis = 12

# Mengimport nilai pi
from math import pi

# rumus
luas_permukaan = pi * jari_jari * (jari_jari + garis_pelukis)
volume = (1/3) * pi * (jari_jari ** 2) * tinggi

# output
print("Jari-jari :", jari_jari)
print("tinggi :", tinggi)
print("garis_pelukis :", garis_pelukis)
print("Luas Permukaan Kerucut: ", luas_permukaan)
print("Volume Kerucut: ", volume)
