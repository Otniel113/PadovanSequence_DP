# PadovanSequence_DP
Membandingkan kompleksitas waktu Padovan Sequence secara: 
1. Rekursif
2. Dynamic Programming (Memoization) atau dengan pendakatan Top-Down 
3. Dynamic Programming (Tabulation) atau dengan pendekatan Bottom-Up

## Penjelasan Padovan Sequence (Barisan Padovan)
![PadovanGambar](https://upload.wikimedia.org/wikipedia/commons/c/cd/Padovan_triangles_%281%29.png)

Padovan Sequence (Barisan Padovan) adalah barisan yang merupakan relasi rekurensi dengan rumus sebagai berikut:


![PadovanRumus](https://latex.codecogs.com/gif.latex?%5Cbg_white%20P_n%3D%20%5Cbegin%7Bcases%7D%201%2C%26%20%5Ctext%7Bjika%20%7D0%5Cleq%20n%5Cleq%202%5C%5C%20P_%7Bn-2%7D%20&plus;%20P_%7Bn-3%7D%2C%26%20%5Ctext%7Bjika%20%7D%20n%20%5Cgeq%203%20%5Cend%7Bcases%7D)

Sehingga menghasilkan baris seperti : 1,1,1,2,2,3,4,5,7,9,12,...

Agak mirip dengan barisan Fibonacci (Fibonacci Sequence) yang membedakan adalah relasi rekurensinya dan juga basisnya

## Kompleksitas

1. Rekursif : O(1.32471^n)
2. DP Memoization (Top-Down) : O(n)
3. DP Tabulation (Bottom-Up) : O(n)

## Algoritma

Rekursif
```python
def padovan_biasa(n):
    if (n <= 2):
        return 1
    else:
        return padovan_biasa(n-3) + padovan_biasa(n-2)
```

Dynamic Programming Memozation
```python
def inisiasiMemori(memori, n):
    for i in range(0,n):
        if (0 <= i <= 2):
            memori.append(1)
        else:
            memori.append(0)
            
def padovan_memoization(memori, n):
    if (memori[n] != 0):
        return memori[n]
    else:
        memori[n] = padovan_memoization(memori, n-3) + padovan_memoization(memori, n-2)
        return memori[n]
```

Dynamic Programming Tabulation

```python
def padovan_tabulation(n):
    memori_lokal = []
    for i in range(0,n+1):
        if (0 <= i <= 2):
            memori_lokal.append(1)
        else:
            memori_lokal.append(memori_lokal[i-3] + memori_lokal[i-2])
    return memori_lokal[n]
```

## Langkah per Langkah

Rekursif <br>
![Rekursif](https://user-images.githubusercontent.com/57952404/148190641-5ede367e-03e2-4ce2-9e3a-1abcab5ca72e.png)

Dynamic Programming Memoization<br>
![Memoization](https://user-images.githubusercontent.com/57952404/148190702-fd776832-9e43-4c9d-ae60-a95d7f25cccb.png)

Dynamic Programming Tabulation<br>
![Tabulation](https://user-images.githubusercontent.com/57952404/148190749-4638f8c8-ebf7-4d7a-8a20-bf8706ff17fb.png)

## Hasil Pengamatan

Nilai N adalah inputan user untuk mencari nilai Pandovan ke-n. Tabel berikut berisi waktu eksekusi dalam detik
| Nilai n |	30 | 40 |	50 | 60 |	70	| 1000	| 2500 |
| -- | -- | -- | -- | -- | -- | -- | -- |
| Rekursif	| 0.01	| 0.03	| 0.34	| 5.24 | 89.59	|	
| DP Memozation (Top-Down) |	0 |	0 |	0 |	0 |	0 |	0.001 |	0.005 |
| DP Tabulation (Bottom-Up) |	0 |	0 |	0 |	0 |	0 |	0.001 |	0.001 |
<br>

Atau dapat dilihat dalam grafik berikut <br>
![Padovan_Grafik_70](https://user-images.githubusercontent.com/57952404/148191562-ad1a52d1-b536-4438-a3ea-92b03390b3ad.png)
