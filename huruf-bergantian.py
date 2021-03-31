'''
Kotakode challenge #1
Tanggal upload            : 23 Maret 2021
Nama akun yang digunakan  : yosmich

LATAR BELAKANG
Kamu diberikan string yang hanya memiliki dua huruf, P dan C. 
Ubah string tersebut untuk menjadi sebuah string dimana tidak boleh ada huruf yang sama bersebelahan. 
Lalu hitung jumlah huruf yang harus dihapus untuk memenuhi kebutuhan itu.

Input   : string yang hanya memiliki huruf P dan C.
Output  : int

CONTOH 1
Input       : "PCPCCPC"
Output      : 1
Penjelasan  : Hasil 1 didapatkan karena hanya perlu menghapus huruf C di indeks ke-4 (1-based indexing).

CONTOH 2
Input       : "PPCPPC"
Output      : 2
Penjelasan  : Hasil 2 didapatkan karena harus menghapus huruf P di indeks ke-1 dan ke-4 (1-based indexing) agar menghasilkan huruf bergantian.

CONTOH 3
Input       : "PCPPCPPP"
Output      : 3
Penjelasan  : Hasil 3 didapatkan karena bisa menghapus huruf P di indeks ke-4, indeks ke-7 dan indeks ke-8 (1-based indexing).

INSTRUKSI
Buatlah sebuah fungsi hurufBergantian yang menerima sebuah string input. 
Output nya adalah sebuah int dimana nilai dari int tersebut adalah jumlah minimum huruf yang dihapus.

'''

def hurufBergantian(inputString):  # tidak terbatas'P' dan 'C' saja
    length = len(inputString)
    if length < 2:
        return 0
    if inputString[0] == inputString[1]:
        return 1 + hurufBergantian(inputString[1:length])
    else:
        return 0 + hurufBergantian(inputString[1:length])

# main
while True:
    inputString = input("Tulis sebuah string dengan huruf P dan C saja: ")

    # cek apakah kata dengan 'P' dan 'C' saja
    valid = True
    for i in inputString:
        if not(i == 'P' or i == 'C'):
            valid = False
            print("String Anda mengandung huruf lain selain 'P' dan 'C'.")
            break
    if valid:
        print("Jumlah huruf minimum yang harus Anda hapus:")
        print(hurufBergantian(inputString))
