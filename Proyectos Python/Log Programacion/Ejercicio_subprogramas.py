import misfunciones as mf

a = int(input("Entre valor de a "))
b = int(input("Entre valor de b "))
if mf.esPrimo(a):
    print(a, "es primo")
else:
    print(a, "NO es primo")
if mf.esPrimo(b):
    print(b, "es primo")
else:
    print(b, "NO es primo")
mcd =mf.mcd(a, b)
print("El máximo común divisor de", a, "y", b, "es", mcd)
mcm = mf.mcm(a, b)
print("El mínimo común múltiplo de", a, "y", b, "es", mcm)
da= mf.pdigito(a)
print(da)
db=mf.pdigito(b)
print(db)
