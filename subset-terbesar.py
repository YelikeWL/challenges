''' 
Kotakode challenge #1
Tanggal upload            : 25 Maret 2021
Nama akun yang digunakan  : yosmich

LATAR BELAKANG
Kamu diberikan sebuah list berisi integer. Temukan subset dari elemen yang TIDAK BERSEBELAHAN 
yang jika di total, memiliki jumlah terbesar. Berikan jumlah dari subset tersebut. 
Jika semua elemen di dalam list bernilai negatif, maka total jumlah terbesar nya adalah 0.

Input  : Sebuah list berisi integer.
Output : int

CONTOH 1
Input       : [3, 7, 4, 6, 5] 
Output      : 13
Penjelasan  : Kemungkinan kombinasi subset adalah [3, 4, 5], [3, 4], [3, 6], [3, 5], [7, 6], [7, 5], dan [4, 5]. 
              Total jumlah subset terbesar adalah 13, dari subset [7, 6]

CONTOH 2
Input       : [2, 1, 5, 8, 4] 
Output      : 11
Penjelasan  : Kemungkinan kombinasi subset adalah [2, 5, 4], [2, 5], [2, 8], [2, 4], [1, 8], [1, 4], [5, 4]. 
              Total jumlah subset terbesar adalah 11, dari subset [2, 5, 4]

CONTOH 3
Input       : [3, 5, -7, 8, 10] 
Output      : 15
Penjelasan  : Kemungkinan kombinasi subset adalah [3, -7, 10], [3, -7], [3, 8], [3, 10], [5, 8], [5, 10], dan [-7, 10]. 
              Total jumlah subset terbesar adalah 15, didapatkan dari subset [5, 10]

INSTRUKSI
Buatlah fungsi subsetTerbesar beroutput sebuah integer yang merepresentasikan jumlah subset terbesar dari list yang diberikan.

'''

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

def sub_lists(inputList):       # membuat subsets dari list tanpa syarat
    base = []  
    subsets = [base]
    for i in range(len(inputList)):
        orig = subsets[:]
        new = inputList[i]
        for j in range(len(subsets)):
            subsets[j] = subsets[j] + [new]
        subsets = orig + subsets
          
    return subsets

def subsetTerbesar(inputList):
    output = 0
    subsets = sub_lists(inputList)
    for subset in subsets:      # coba satu2 per subset yang sudah tercipta
        raw = 0     # store jumlah angka yang paling besar sekarang
        index = 5   # random number kecuali -1, 0, 1
        for j in subset:        # tambahkan angka lain
            if j > 0 and (inputList.index(j) - index != 1):     # skip negatif / berdampingan
                raw += j
                index = inputList.index(j)
        if raw > output:        # lebih besar akan di save sebagai subset terbesar sementara
            output = raw
    return output

# main
while True:
    inputList = input("Masukkan list angka: ")      # masih dalam bentuk string
    inputList = stringList_ke_listInt(inputList)    # sudah jadi list di Python
    print("Jumlah terbesar dari subset yang tidak berdampingan:")
    print(subsetTerbesar(inputList))
