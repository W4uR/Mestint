from keres import *

class kiralyno(Feladat):
    def __init__(self,ke,c):
        super().__init__(ke,c)
        self.S=c-1


    def céltesz(self, állapot):
        return állapot[self.S] == self.cél


    def rákövetkező(self, állapot):

        lépések= list()

        s=állapot[self.S] # (1,2,0,0,0,0,0,0,3)

        for i in range(1,self.S+1):
            előfeltétel = True
            for m in range(1,állapot[self.S]): #m:[1,2]
                all=állapot[m-1]
                abs1=abs(m-s)
                abs2=abs(i-állapot[m-1])
                if állapot[m-1] != i and abs(m-s) != abs(i-állapot[m-1]):
                    előfeltétel = True
                else:
                    előfeltétel = False
                    break

            if előfeltétel:
                állapot_uj=list(állapot)

                állapot_uj[s-1] =i
                állapot_uj[8]=állapot_uj[8]+1

                állapot_uj2 = tuple(állapot_uj)
                lépések.append(állapot_uj2)

        return lépések

    def __str__(self):
        str=''
        for i in self.kezdő[:self.S]:
            if i==0:
                str += 'x  '*self.S+'\n'
            else:
                str += 'x  '*(i-1) + 'Q  ' + 'x  '*(self.S-i)+'\n'


        return str



ha = kiralyno((0,0,0,0,0,0,0,0,1),9)


while ha.célteszt(ha.kezdő)==False:
    print(ha)
    rakov=ha.rákövetkező(ha.kezdő)
    if len(rakov)!= 0:
        print(rakov)
    else:
        print('Vége')
        break
    lepes=int(input('Adjon meg egy lépést: '))
    lepes=rakov[lepes-1]
    ha=kiralyno(lepes,9)
