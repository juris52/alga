bruto=int(input("Cik ir J�su bruto m�ne�alga? "))
if bruto>1666.67:
    ien=0.23
else:
    ien=0.2
gr=int(input("Vai Jums ir algas nodok�u gr�mati�a? 1- N�; 2- J�: "))
if gr==2:
    cl=int(input("Cik cilv�kus J�s apg�d�jat? " ))
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
print("J�su NETO alga b�s", na,"eiro")
print("No J�su bruto algas", soc,"eiro aizgaja soci�lajos nodok�os")
print("No J�su bruto algas", nd,"eiro aizg�ja ien�kumu nodok�os")