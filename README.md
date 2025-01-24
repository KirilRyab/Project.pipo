## Projekt zaliczeniowy na zajęcia Projektowanie i programowanie obiektowe.

Przedstawiony projekt tworzy symulację systemu produkcyjnego, generując losowe dane o produktach i zamówieniach. 
Dane te mogą być następnie wykorzystane do różnych celów, takich jak testowanie aplikacji zarządzających produkcją, 
tworzenie symulacji "co by było gdyby" czy analiza wydajności różnych scenariuszy produkcyjnych.

Główne elementy kodu:

>ProductGenerator: Generuje losowe produkty z określonymi atrybutami (ID, liczba form, liczba pasków na formę).
>Product (abstrakcyjna): Reprezentuje ogólny produkt i definiuje podstawowe atrybuty.
>SpecialProduct: Dziedziczy po Product i dodaje atrybut określający, czy produkt jest premium.
>Order: Reprezentuje zamówienie na produkt, zawierając informacje o produkcie, ilości i terminie realizacji.
