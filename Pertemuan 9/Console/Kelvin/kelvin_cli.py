print("Konversi Suhu Kelvin")

# Entry
suhu = input("Maukkan Suhu Dalam Kelvin:")

# Rumus 
C = (float(suhu) - 273)
F = (9/5 * (float(suhu) - 273) +32)
R = (4/5 * (float(suhu) - 273))

# Output
print(suhu + " Kelvin Sama Dengan")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")