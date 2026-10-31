# Microbit-Reflex-Game
Gra zręcznościowa na Micro:bit z rankingiem online
1. Micro- gra zręcznościowa
Stworzenie prostej gry polegającej na pomiarze czasu reakcji gracza. Po pojawieniu się sygnału na wyświetlaczu LED gracz naciska odpowiedni przycisk. Urządzenie oblicza wynik i przesyła go wraz z identyfikatorem gracza przez USB do komputera.

2. Python- komunikacja
Program Python odbiera dane z Micro przez USB i przesyła je przez internet do bazy Firebase. Odpowiada również za pobieranie rankingu i przekazywanie go do drugiego Micro.

3. Firebase- baza danych
Przechowywanie identyfikatorów graczy, zdobytych punktów oraz dat rozgrywek. Dane pozostają dostępne online niezależnie od działania urządzeń.

4. Strona internetowa- ranking
Prosta strona wykonana w HTML, CSS i JavaScript, która pobiera wyniki z Firebase i wyświetla ranking graczy. Strona będzie dostępna przez publiczny adres WWW.

5. Drugi Micro- wyświetlanie rankingu
Drugie urządzenie podłączone przez USB do komputera będzie wyświetlało najlepsze wyniki pobrane z bazy danych.

6. GitHub- dokumentacja projektu
Repozytorium zawierające kod źródłowy, strukturę projektu, opis działania oraz instrukcję uruchomienia.
Schemat połączeń:

Micro (gra)- USB- Python- Internet- Firebase

Firebase- Strona WWW (ranking online)

Firebase- Python- USB- Micro (ranking fizyczny)

Wykorzystane technologie: Micro, Microsoft MakeCode, Python, Firebase, HTML, CSS, JavaScript, GitHub.
