import time

# Inisiasi Memori untuk membantu Memoization
def inisiasiMemori(memori, n):
    #Inisiasi memori berupa list di mana nilai ke-0,1,2 diisi 1 sebagai basis dan sisanya 0
    for i in range(0,n):
        if (0 <= i <= 2):
            memori.append(1)
        else:
            memori.append(0)

# Padovan secara Rekursif
def padovan_biasa(n):
    if (n <= 2):
        return 1
    else:
        return padovan_biasa(n-3) + padovan_biasa(n-2)

# Padovan dengan Dynamic Programming Memoization (Top-Down)
def padovan_memoization(memori, n): #Dengan bantuan memori berupa list
    if (memori[n] != 0):
        return memori[n]
    else:
        memori[n] = padovan_memoization(memori, n-3) + padovan_memoization(memori, n-2)
        return memori[n]

# Padovan dengan Dynamic Programming Tabulation (Bottom-Up)
def padovan_tabulation(n):
    memori_lokal = []   #Inisiasi memori
    for i in range(0,n+1):
        if (0 <= i <= 2):               
            memori_lokal.append(1)  #Basis
        else:
            memori_lokal.append(memori_lokal[i-3] + memori_lokal[i-2])
    return memori_lokal[n]

#===============MAIN PROGRAM========
bil = int(input("Masukkan bilangan Padovan ke-berapa yang ingin dicari: "))
while (bil < 3):            # Menjamin agar nilai yang diinput lebih besar atau sama dengan 3
    bil = int(input("\nMasukkan bilangan yang lebih besar atau sama dengan 3: "))

# Menghitung waktu eksekusi Rekursif
start = time.time()
hasil = padovan_biasa(bil)
end = time.time()
print("\nWaktu eksekusi Padovan biasa (dengan rekursif) adalah ", (end-start), " detik")
print("Hasil bilangan Padovan adalah ", hasil)

# Menghitung waktu eksekusi Memoization
memori = []
inisiasiMemori(memori, bil+1)

start = time.time()
hasil = padovan_memoization(memori, bil)
end = time.time()
print("\nWaktu eksekusi Padovan dengan DP Memoization adalah ", (end-start), " detik")
print("Hasil bilangan Padovan adalah ", hasil)

# Menghitung waktu eksekusi Tabulation
start = time.time()
hasil = padovan_tabulation(bil)
end = time.time()
print("\nWaktu eksekusi Padovan dengan DP Tabulation adalah ", (end-start), " detik")
print("Hasil bilangan Padovan adalah ", hasil)