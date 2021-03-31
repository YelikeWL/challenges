'''
Kotakode challenge #2
Tanggal upload            : 24 Maret 2021
Nama akun yang digunakan  : yosmich

LATAR BELAKANG
Diberikan 2 input: input pertama adalah sebuah list berisi integer dan input kedua adalah sebuah integer, x.
Tugas kamu adalah untuk menemukan semua kemungkinan kombinasi pasangan dari list tersebut 
yang dimana total jumlah dari setiap pasangan nya harus sama dengan x.

Input   : 
1. Sebuah list berisi integer (Minimum element di input list adalah 2. Input list tidak harus sorted).
2. Sebuah integer.

Output  :
Sebuah two dimensional list berisi pasangan-pasangan integer.

CONTOH 1
Input       : [1, 2, 4, 6, 9], 15
Output      : [[6, 9]]
Penjelasan  : Hanya bilangan 6 dan 9 yang jika ditambahkan akan menghasilkan 15. Maka dari itu, output nya adalah [6, 9].

CONTOH 2
Input       : [1, 2, 3, 4, 5], 7
Output      : [[2, 5], [3, 4]]
Penjelasan  : Untuk menghasilkan 7, ada dua kemungkinan: yaitu 2+5 dan juga 3+4. Maka dari itu, output nya adalah [2, 5],[3, 4]

INSTRUKSI
Menggunakan fungsi cariPasangan(list a, int x) dimana a adalah sebuah list berisi integer dan x adalah sebuah integer, 
temukan semua pasangan dari list a dimana jumlah dari dua bilangan tersebut adalah integer x.

'''

def cariPasangan(inputList, inputInt):
    pasangan = []
    reverseList = inputList[::-1]
    listLen = len(inputList)
    for i in range(listLen):
        j = inputInt - inputList[i]   
        # bisa juga pakai iterasi untuk j, tapi makan waktu jika list besar
        if j in inputList and (listLen - reverseList.index(j) - 1) != i):   # cek index dari belakang
            if [j, inputList[i]] not in pasangan:
                pasangan.append([inputList[i], j])
    return pasangan

def stringList_ke_listInt(inputList):   # ubah inputList berupa string, jadi list int Python
    data = []
    pivot = 1
    raw = 0
    while pivot < (len(inputList)):
        try:
            raw = int(inputList[pivot]) + raw * 10
        except:
            if raw != 0:
                data.append(raw)
                raw = 0
        pivot += 1
    return data

# main
while True:
    try:    # cek format input yang diberikan
        inputList = input("Masukkan list angka (minimal 2), seperti [1, 3, 5]: \n")      # masih dalam bentuk string
        inputInt = int(input("Masukkan angka target penjumlahan (x): \n"))
        inputList = stringList_ke_listInt(inputList)
        valid = True
    except:
        print("Format input Anda masih salah. Harap coba lagi.")
        valid = False
        
    if valid:
        print("Pasangan yang memenuhi data:")
        print(cariPasangan(inputList, inputInt))
