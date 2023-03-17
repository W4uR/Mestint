from keres import *
from random import randint
class Korsók(Feladat):
    def __init__(self, ke,c):
        self.kezdő= ke
        self.cél=c
        self.K1=8
        self.K2=5
        self.K3=3

    def célteszt(self, állapot):
        return állapot[0]==self.cél or állapot[1]==self.cél

    def rákövetkező(self, állapot):
        k1, k2,k3 =állapot
        lépések=list()

        if k1>0 and k2<self.K2:
            m=min([k1,self.K2-k2])
            lépések.append(("k1-ből k2-be",(k1-m,k2+m,k3)))

        if k1 > 0 and k3 < self.K3:
            m = min([k1, self.K3 - k3])
            lépések.append(("k1-ből k3-ba",(k1-m, k2 , k3+m)))

        if k2 > 0 and k3 < self.K3:
            m = min([k2, self.K3 - k3])
            lépések.append(("k2-ből k3-ba",(k1, k2-m, k3 + m)))

        if k2 > 0 and k1 < self.K1:
            m = min([k2, self.K1 - k1])
            lépések.append(("k2-ből k1-be",(k1+m, k2 - m, k3)))

        if k3 > 0 and k1 < self.K1:
            m = min([k3, self.K1 - k1])
            lépések.append(("k3-ből k1-be",(k1+m, k2, k3-m)))

        if k3 > 0 and k2 < self.K2:
            m = min([k3, self.K2 - k2])
            lépések.append(("k3-ből k2-be",(k1, k2+m, k3 - m)))

        return lépések

    def érték(self, csúcs):
        állapot=csúcs.állapot
        v=min(abs(állapot[0]-4),abs(állapot[1]-4))

        return v

    def __str__(self):
        return 'Kancsó:' + str(self.kezdő)



korso=Korsók((8,0,0),4)

a=best_first(korso,korso.érték)
print(a.út())
# print(a.megoldás())

a=szélességi_fakeresés(korso)
print(a.út())

a=szélességi_gráfkeresés(korso)
print(a.út())

a=mélységi_gráfkeresés(korso)
print(a.út())

a=a_csillag(korso,korso.érték)
print(a.út())

# a=mélységi_fakeresés(korso)
# print(a.út())

# print(korso)
# print(korso.rákövetkező(korso.kezdő))
#
# while korso.célteszt(korso.kezdő)==False:
#     # print(korso)
#     print(korso.rákövetkező(korso.kezdő))
#     # i=int(input("Valassza ki a lépést: "))-1
#     i=randint(0,len(korso.rákövetkező(korso.kezdő))-1)
#     lepes=korso.rákövetkező(korso.kezdő)[i][1]
#     korso=Korsók(lepes,4)
#     print(korso)


# if __name__ == "__main__":
#    korso=Korsók((8,0,0),4)
#    print(korso)
#    print('Szélességi keresés')
#    a = szélességi_fakeresés(korso)
#    print(a)
#
#    utam = a.út()
#    utam.reverse()
#    print(utam)


