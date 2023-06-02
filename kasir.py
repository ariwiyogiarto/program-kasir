db_barang = ["Buku","Pena","Pensil", "Tipe-x"]
harga = [2500, 3000, 4500, 5000]

total = 0
member = None
while True:
	barang = input("Masukkan Nama Barang : ")
	jumlah = int(input("Jumlah Beli : "))
	if member == None:
		member = input("Apakah Termasuk Member ? ")
	ulang = input("Apakah Mau Input Lagi ?")
	no = db_barang.index(barang)
	total += harga[no] * jumlah
	if ulang == "n":
		break

print(total)
if member == "y":
	diskon1 = total * (50 / 100)
	print(diskon1)
	if total > 100000:
		diskon2 = total * 25 / 100
		total -= diskon1 + diskon2
	else:
		total -= diskon1
else:
	if total > 100000:
		diskon2 = total * 25 / 100
		total -= diskon2
	else:
		total = total
	
	

hasil = f"=================\nTotal Belanja Rp.{total}\n=================="
f1 = open("hasil_belanja.min",'w')
f1.write(hasil)
f1.close()

print(hasil)
		