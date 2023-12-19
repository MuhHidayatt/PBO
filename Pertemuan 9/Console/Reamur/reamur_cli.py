print("Konversi Suhu Reamur")

# Entry
suhu = input("Maukkan Suhu Dalam Reamur:")

# Rumus 
C = (4/5 * float(suhu))
F = (9/4 * float(suhu)) + 32
K = (5/4 * float(suhu)+273)

# Output
print(suhu + " Reamur Sama Dengan:")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")