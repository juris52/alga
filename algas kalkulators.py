from math import*
def reiz(a,b):
    reiz=a*b
    return reiz
ska=int(input("Cik cilvēku algas Jūs vēlaties aprēķināt? "))
for i in range (0,ska+1):
    bruto=int(input("Cik ir Jūsu bruto mēnešalga? "))
    if bruto>1666.67:
        ien=0.23
    else:
        ien=0.2
    gr=int(input("Vai Jums ir algas nodokļu grāmatiņa? 1- Nē; 2- Jā: "))
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
    else:
        soc=bruto*0.105
        pn=bruto-soc
        nd=pn*ien
        na=pn-nd
    print("Jūsu neto alga būs", na,"eiro")
    print("No Jūsu bruto algas", soc,"eiro aizgāja sociālajos nodokļos")
    print("No Jūsu bruto algas", nd,"eiro aizgāja ienākumu nodokļos")
