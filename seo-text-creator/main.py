from data import get_sentences
from random import randrange

makale_sayisi=20
makale_cumle_sayisi=200

data=get_sentences()

print("Cümle Sayısı: " ,len(data))
print("Önerilen: " ,makale_sayisi*makale_cumle_sayisi/4)

for i in range(makale_sayisi):
    len_data=len(data)
    if len_data<makale_cumle_sayisi:
        print("\n\ndata.txt işlenemeyecek kadar küçük")
        break
    outfile="data/{}.txt".format(i)
    outtext=""
    used=[]
    while len(used)<makale_cumle_sayisi:
        index=randrange(0,len_data)
        if index not in used:
            used.append(index)
            outtext+= data[index] + " "

    with open(outfile,'w',encoding="utf-8") as f:
        f.write(outtext)
    
##bu gardaşım
