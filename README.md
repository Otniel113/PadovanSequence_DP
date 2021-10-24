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

