"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5] 
"""

input= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flat_list = []
for sublist in input:
    if type(sublist)==list:
        for item in sublist:
            if type(item)==list:
                for i in item:
                    if type(i)==list:
                        for j in i:
                            flat_list.append(j)
                    else:
                        flat_list.append(i)
            else:
                flat_list.append(item)
    else:
        flat_list.append(sublist)

print("Verilen girdi :" , input)
print("Istenen cikti  :" , flat_list)


"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""


def reverseListe(liste):
   liste=liste[::-1]
   rListe=[]
   for item in liste :
       if type(item) == list:
           item=item[::-1] 
           rListe.append(item) 
   return rListe

input=[[1, 2], [3, 4], [5, 6, 7]]

print("input: ", input)
print("output: ", reverseListe(input))

