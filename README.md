## Projekt zaliczeniowy na zajęcia Projektowanie i programowanie obiektowe.

Przedstawiony projekt tworzy symulację systemu produkcyjnego, generując losowe dane o produktach i zamówieniach. 
Dane te mogą być następnie wykorzystane do różnych celów, takich jak testowanie aplikacji zarządzających produkcją, 
tworzenie symulacji "co by było gdyby" czy analiza wydajności różnych scenariuszy produkcyjnych.

Główne elementy kodu:
>ProductGenerator: Generuje losowe produkty z określonymi atrybutami (ID, liczba form, liczba pasków na formę).
>
>Product (abstrakcyjna): Reprezentuje ogólny produkt i definiuje podstawowe atrybuty.
>
>SpecialProduct: Dziedziczy po Product i dodaje atrybut określający, czy produkt jest premium.
>
>Order: Reprezentuje zamówienie na produkt, zawierając informacje o produkcie, ilości i terminie realizacji.

Funkcje:
>generate_products_csv: Tworzy plik CSV z losowymi danymi o produktach.
>
>generate_orders_csv: Tworzy plik CSV z losowymi zamówieniami, wykorzystując wcześniej wygenerowane dane o produktach.

Modelowanie obiektów:

>product.py: Definiuje abstrakcyjną klasę Product oraz jej konkretne podklasy: Belt i Slab. Klasy te przechowują informacje >o produktach i umożliwiają obliczenie zużycia materiałów.
>
>slab.py: Rozszerza klasę Product o dodatkowe właściwości związane z płytami (slabs).

Planowanie produkcji:
>production_plan.py: Zawiera klasę WeeklyPlanner, która tworzy harmonogram produkcji na podstawie zamówień i dostępnych zasobów.

Konfiguracja
>config.py: Definiuje parametry konfiguracji produkcji, takie jak liczba zmian, liczba maszyn itp.

Główne Moduły i Ich Funkcje
>ProductGenerator: Generuje losowe produkty z różnymi właściwościami.
>
>OrderGenerator: Tworzy losowe zamówienia na podstawie dostępnych produktów.
>
>Product: Klasa bazowa dla wszystkich produktów, definiuje podstawowe atrybuty.
>
>Belt, Slab: Konkretne implementacje klasy Product dla różnych rodzajów produktów.
>
>WeeklyPlanner: Planuje produkcję na cały tydzień, biorąc pod uwagę dostępność maszyn, zamówienia i ograniczenia czasowe.
>
>ScheduleConfig: Przechowuje parametry konfiguracji produkcji.

Jak działa system:
>Generowanie danych: Na początku tworzone są losowe produkty i zamówienia.
>
>Planowanie: Klasa WeeklyPlanner analizuje zamówienia i tworzy szczegółowy harmonogram produkcji, uwzględniając ograniczenia >dotyczące maszyn i czasu.
>
>Obliczenia zużycia materiałów: Klasy produktów (np. Belt, Slab) umożliwiają obliczenie ilości potrzebnych materiałów dla >każdego zamówienia.

Przedstawiony kod stanowi solidną podstawę do tworzenia symulacji produkcji. Można go łatwo rozbudować i dostosować do konkretnych potrzeb. Generowane dane mogą być przydatne zarówno dla programistów tworzących aplikacje produkcyjne, jak i dla analityków biznesowych chcących przeprowadzać symulacje i analizy.


## Generators.py
Kod stanowi fundament dla systemu zarządzania produkcją taśm. Jego głównym celem jest generowanie danych wejściowych dla procesu planowania produkcji. Składa się z kilku modułów, które współpracują ze sobą, aby stworzyć realistyczne scenariusze produkcyjne.

Kluczowe klasy i ich funkcje
>ProductGenerator generuje losowe produkty. Stosuje klasy i obiekty do reprezentowania produktów, wykorzystuje konstruktory do inicjalizacji obiektów.

>OrderGenerator tworzy losowe zamówienia na podstawie wygenerowanych produktów.Korzysta z klas i obiektów do reprezentowania zamówień, wykorzystuje konstruktory do inicjalizacji obiektów.

Hermetyzacja
>Atrybuty obiektów są zazwyczaj prywatne (np. _product_id), co chroni je przed przypadkową modyfikacją.
>
>Dostęp do atrybutów odbywa się za pomocą metod dostępowych (getterów), co pozwala na kontrolę nad zmianami danych.

Dziedziczenie
>Klasa Belt dziedziczy po klasie Product, co pozwala na tworzenie bardziej szczegółowych definicji produktów.
>
>Dzięki dziedziczeniu, obiekty typu Belt mogą mieć dodatkowe atrybuty i metody specyficzne dla taśm.

Konstruktory
>Konstruktory są używane do inicjalizacji obiektów, ustawiając wartości początkowe dla ich atrybutów.

Funkcje anonimowe (lambda):
>Służą do tworzenia prostych funkcji, które są używane w określonych miejscach kodu, np. do generowania losowych wartości logicznych.
