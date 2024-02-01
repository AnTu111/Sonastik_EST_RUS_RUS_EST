def Loe_failist(fail:str)->list:
 f=open(fail,'r',encoding="utf-8-sig")
 mas=[]
 for rida in f:
    mas.append(rida.strip('\n').upper())
 f.close()
 return mas


def lisamine(mas:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()



def connect(est:list,rus:list)->any:
    zipped=zip(est,rus)
    print(list(zipped))


def est_to_rus(est:list,rus:list)->list:
    n=str(input("Palun sisetage sona eesti keeles:-- ")).upper()
    if n in est:
        ind=est.index(n) 
        print(f"{n} -- {rus[ind]}") 
        v = int(input("Kui tunnete, et tõlkimine on ebakorrektne vajutage - 1 - "))
        if v == 1:
           cor = str(input("Sisetage korrektne tõlkimine siia: "))
           rus[ind] = cor
           lisamine(rus,"rus.txt") 
           print(est) 
           print(rus)
        else:
            print("Bye")
    else:
       print("Selline sõna on puudu, lisage palun: ")
       est,rus = elementi_lisamine(est,rus)
       lisamine(est,"est.txt")
       lisamine(rus,"rus.txt")
       

def elementi_lisamine(est:list, rus:list):
   es = input("Sõna eesti keeles: / Слово на эстонском: " )
   est.append(es)
   ru = input("Sõna vene keeles: / Слово на русском:  ")
   rus.append(ru)
   return est,rus
   

def rus_to_est(est:list,rus:list)->list:
   n = str(input("Введите слово на русском языке:-- ")).upper()
   if n in rus:
      ind = rus.index(n)
      print(f"{n} -- {est[ind]}")
      v = int(input("Если вам кажется, что слово введено не корректно нажмите - 1 - "))
      if v == 1:
         cor = str(input("Введите корректный перевод: "))
         est[ind] = cor
         lisamine(est,"est.txt")
         print(est)
         print(rus)
      else:
            print("Bye")
   else:
      print("Слово отсутсвует, добавьте: ")
      est,rus = elementi_lisamine(est,rus)
      lisamine(est,"est.txt")
      lisamine(rus,"rus.txt")
      

def mang(est:list,rus:list):
   import random
   oige = 0
   for i in range(5):
      n = random.choice(est)
      print(n)
      ind = est.index(n)
      v = input("Sisestage tolkimine: ").upper()
      if v in rus and v == rus[ind]:
         oige += oige
         print(f"Koorektne! , õige sona on {rus[ind]}")
      else:
         print("Kahjuks vastus on vale")
   
   print(f"Teie tulemus on {oige}")
   
      
   


      
      





   