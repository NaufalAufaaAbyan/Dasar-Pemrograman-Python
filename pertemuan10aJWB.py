values = []

for i in range(1,6):  # range(1, 6) menghasilkan 1, 2, 3, 4, 5
    value = input(f"Masukkan nilai ke-{i}: ")
    values.append(value)

print("\nTampilkan Lagi Datanya")
print("---------------------------")

for i, value in enumerate(values, start=1):  # start=1 agar indeks dimulai dari 1
    print(f"Nilai ke-{i}: {value}")