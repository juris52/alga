bruto=int(input("Cik ir Jûsu bruto mçneðalga? "))
if bruto>1666.67:
    ien=0.23
else:
    ien=0.2
gr=int(input("Vai Jums ir algas nodokïu grâmatiòa? 1- Nç; 2- Jâ: "))
if gr==2:
    cl=int(input("Cik cilvçkus Jûs apgâdâjat? " ))
    soc=bruto*0.105
    pn=bruto-soc
    if (pn-175-250*cl)>0:
        nm=pn-175-250*cl
        nd=nm*ien
        na=nm-nd+175+250*cl
    else:
        na=pn
        nd=0
else:
    soc=a*0.105
    pn=bruto-soc
    nd=pn*ien
    na=pn-nd+175+250*cl
print("Jûsu NETO alga bûs", na,"eiro")
print("No Jûsu bruto algas", soc,"eiro aizgaja sociâlajos nodokïos")
print("No Jûsu bruto algas", nd,"eiro aizgâja ienâkumu nodokïos")