vn=[]

for a in range(0,10,1):
    vn.append(input(f"Masukkan nilai ke-{a} : "))

print()
print("Tampilkan Lagi Datanya")
print("---------------------------")

for a in range(0,10,1):
    print(f"Nilai ke-{a} : {vn[a]}")