import math

# Input jari-jari lingkaran dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Hitung luas lingkaran
luas = math.pi * jari_jari ** 2

# Hitung keliling lingkaran
keliling = 2 * math.pi * jari_jari

# Tampilkan hasil
print(f"Luas lingkaran: {luas}")
print(f"Keliling lingkaran: {keliling}")