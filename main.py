#wypisać jakie są typy danych w python

#Funkcje wspomagajace sprawdzanie typow obiektów
liczbaint = 11
print(type(liczbaint)) #wyciagniecie klasy obiektu
print(type(liczbaint).__name__) #zwraca typowo nazwę typu obiektu
print(isinstance(liczbaint, int)) #porownuje czy zmienne jest podanego typu

#ZMIENNE
#1 INTEGER 
#liczby całkowite dodatnie i ujemne
liczba1 = 2
liczba2 = 77
liczba3 = -42
print(type(liczba1), type(liczba2), type(liczba3))
print(isinstance(liczba1, int))

#2 FLOAT liczby zmiennoprzecinkowe (separator to kropka)
licz_float = 3.4
licz_float1 = -7.44
print(type(licz_float1))
print(type(licz_float))

#3 STRING - wartosc tekstowa
str1 = 'Halo'
str2 = "Witam"
print(type(str1), type(str2))

#4 BOOLEAN - wartosc logiczna
log1 = True
log2 = False
print(type(log1), type(log2))

#można ją uzyskac porównując ze sobą różne obiekty
#przyklad 
porownanie = 55 == 'zwykły tekst'
print(porownanie)
print(type(porownanie))

#5 Typ NONE sqlowy NULL
typnone = None
print(typnone, type(typnone))

# typ daty??


#CASTOWANIE WARTOŚCI
# float na int
x = 10.2
print(x)
x = int(x)
print(x)

#int float na str
y = 10
x = 5
y = str(y)
x = str(x)
print(y, x)
print(type(y))
print(type(x))

#str na int, float, ale tylko gdy to liczba
licz = '4'
print(int(licz))
print(type(int(licz)))

licz1 = '4.8'
print(type(float(licz1)))
#przyklad blednego castowania
licz_error = 'cztery'
# print(int(licz_error))