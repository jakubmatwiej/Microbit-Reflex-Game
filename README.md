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


# Założenia techniczne i komunikacja

1. Dane wyjściowe z Micro

W mojej grze Micro będzie odpowiadał za pomiar czasu reakcji użytkownika i obliczanie wyniku. Po zakończeniu rozgrywki urządzenie przygotuje dane zawierające identyfikator gracza, identyfikator rozgrywki oraz uzyskany wynik.

2. Komunikacja radiowa

Do przesyłania wyników wykorzystam wbudowany moduł radiowy Micro. Dane będą wysyłane bezprzewodowo do Micro wykładowcy. Format wiadomości, parametry komunikacji oraz sposób kodowania lub szyfrowania dostosuję do wspólnego standardu, który zostanie ustalony podczas zajęć.

3. Brama komunikacyjna

Micro podłączony do komputera wykładowcy będzie pełnił funkcję bramy komunikacyjnej. Będzie odbierał wyniki przesyłane radiowo, a następnie przekazywał je przez USB do komputera wykładowcy.

4. Przesyłanie danych przez internet

Zakładam, że dane z komputera wykładowcy będą przekazywane do mojego API za pomocą protokołu HTTPS w formacie JSON. Dokładny sposób integracji zostanie dostosowany do uzgodnionego standardu.

5. API

Do stworzenia własnego REST API zamierzam wykorzystać Python i framework FastAPI.

API będzie udostępniało dwa podstawowe endpointy:

POST /results – przyjmowanie i zapisywanie wyników.

GET /ranking – pobieranie rankingu graczy.

6. Sposób zapisu danych w bazie

Do przechowywania wyników wykorzystam Firebase Realtime Database. Każda rozgrywka będzie zapisywana jako osobny rekord w formacie JSON.

Proponowana struktura danych:

Pole

Typ

Znaczenie

game_id

String

Identyfikator rozgrywki

player_id

String

Identyfikator gracza

score

Integer

Uzyskany wynik

timestamp

String

Data i godzina zapisu

Datę i godzinę zapisu będzie automatycznie dodawał serwer.

7. Ranking internetowy

Stworzę prostą stronę internetową wykorzystującą HTML, CSS i JavaScript. Strona będzie pobierała wyniki przez moje API i wyświetlała ranking graczy posortowany od najwyższego wyniku.

Ranking będzie dostępny przez publiczny adres internetowy.

8. Niezależność poszczególnych elementów

Zamierzam zaprojektować system w taki sposób, aby gra, API, baza danych i strona internetowa mogły działać jako niezależne elementy.

Dzięki wykorzystaniu wspólnego standardu komunikacji będę mógł przesyłać wyniki do systemu wykładowcy bez konieczności fizycznego podłączania mojego Micro do jego komputera.

9. Dokumentacja projektu

Kod źródłowy, dokumentację techniczną, opis architektury oraz instrukcję uruchomienia będę przechowywał w repozytorium GitHub.

10. Aktualny status

Obecnie opracowuję koncepcję i architekturę rozwiązania. Standard komunikacji radiowej oraz szczegóły integracji z systemem wykładowcy pozostają do ustalenia.
