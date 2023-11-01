print('##  Program Python Belah Ketupat Bintang  ##')
print('============================================')
print()
 
lebar_belah_ketupat = int(input('Input lebar belah ketupat: '))
print()
 
for i in range(lebar_belah_ketupat):
  for j in range(lebar_belah_ketupat-i):
    print(' ',end='')
     
  for k in range(i+1):
    print('* ',end='')
  print()

for i in range(1,lebar_belah_ketupat):
  for j in range(i+1):
    print(' ',end='')
     
  for k in range(lebar_belah_ketupat-i):
    print('* ',end='')
  print()

  a = input("Masukkan nilai a: ")
b = input("Masukkan nilai b: ")
print("Variable a =", a)
print("Variable b =", b)
print("Hasil penggabungan ({}) dan ({}) = {}".format(a, b, a + b))

# Konversi nilai variable
a = int(a)
b = int(b)
print("Hasil penjumlahan ({}) + ({}) = {}".format(a, b, a + b))
print("Hasil pembagian ({}) / ({}) = {}".format(a, b, a / b))