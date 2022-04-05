from math import*
def reiz(a,b):
    reiz=a*b
    return reiz
o=1
p=1
while p==1:
    ska=int(input("Cik cilvēku algas Jūs vēlaties aprēķināt? "))
    if ska>0
        for i in range (0,ska+1):
            bruto=int(input("Cik ir Jūsu bruto mēnešalga? "))
            if bruto>1666.67:
                ien=0.23
            else:
                ien=0.2
            gr=int(input("Vai Jums ir algas nodokļu grāmatiņa? 1- Nē; 2- Jā: "))
            while o==1:
                if gr==2:
                    cl=int(input("Cik cilvēkus Jūs apgādājat? " ))
                    soc=reiz(bruto,0.105)
                    pn=bruto-soc
                    if (pn-175-250*cl)>0:
                        nm=pn-175-250*cl
                        nd=nm*ien
                        na=nm-nd+175+250*cl
                    else:
                        na=pn
                        nd=0
                    o=0
                elif gr=1:
                    soc=bruto*0.105
                    pn=bruto-soc
                    nd=reiz(pn,ien)
                    na=pn-nd
                    o=0
                else:
                    print("Lūdzu ievadiet 1 vai 2")
            print("Jūsu neto alga būs", na,"eiro")
            print("No Jūsu bruto algas", soc,"eiro aizgāja sociālajos nodokļos")
            print("No Jūsu bruto algas", nd,"eiro aizgāja ienākumu nodokļos")
        p=0    
    elif ska<0:
        print("Lūdzu ievadiet nenegatīvu skaitli")
    else:
        print("Visu labu!")
