print(" zad 1A ")
print(type(1 + 2))
print(type(1 + 4.5))
print(type(3 / 2))
print(type(4 / 2))
print(type(3 // 2))
print(type(-3 // 2))
print(type(11 % 2))
print(type(2 ** 10))
print(type(8 ** (1 / 3)))
#
print("zad 1B")
print(int(3.0))
print(float(3))
print(float("3"))
print(str(12.4))
print(bool(0))
#
print("zad 2")
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)
#
print("zad 3")
imie = "Jan"
wiek = 20
wzrost = 178

print(f"Nazywam się {imie} i mam {wiek} lat.")
print(f"Mój wzrost to {wzrost} cm.")
#
print("zad 4")
cena = 39.99
rabat = 0.2
cena_po_rabacie = cena * (1 - rabat)

print(f"cena początkowa: {cena} PLN")
print(f"rabat: {rabat * 100}%")
print(f"cena produktu po rabacie: {cena_po_rabacie:.2f} PLN")
#
print("zad 5")
a = float(input("podaj długość pierwszego boku prostokąta: "))
b = float(input("podaj długość drugiego boku prostokąta: "))

pole = a * b
obwod = 2 * a + 2 * b

print(f"pole prostokąta wynosi: {pole}")
print(f"obwód prostokąta wynosi: {obwod}")
#
print("zad 6")
import random

droga = random.randint(50, 500)
spalanie = float(input("podaj średnie spalanie: "))
cena = float(input("podaj cenę paliwa: "))

zuzycie = (droga * spalanie) / 100
koszt = zuzycie * cena

print("wylosowana droga:", droga)
print("zużycie paliwa:", zuzycie)
print("koszt podróży:", koszt)

input("\nEnter")
