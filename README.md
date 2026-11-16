# Microbit Reflex Game

## 1. Cel projektu

Realizuję indywidualny projekt prostej gry zręcznościowej na platformie BBC Micro:bit, polegającej na pomiarze czasu reakcji gracza.

Po pojawieniu się sygnału na wyświetlaczu LED użytkownik będzie musiał jak najszybciej nacisnąć odpowiedni przycisk. Na podstawie czasu reakcji zostanie obliczony wynik.

Wynik wraz z identyfikatorem gracza będzie przesyłany bezprzewodowo do systemu wykładowcy, a następnie zapisywany w internetowej bazie danych. Docelowo wyniki będą dostępne na stronie WWW w postaci rankingu.

## 2. Architektura systemu

Projekt składa się z następujących elementów:

**1. Micro:bit – gra zręcznościowa**

Micro:bit będzie odpowiadał za obsługę gry, pomiar czasu reakcji, obliczanie wyniku oraz przygotowanie wiadomości zawierającej identyfikator użytkownika, wynik i adres API.

**2. Micro:bit wykładowcy – brama komunikacyjna**

Wyniki będą przesyłane radiowo na grupie 67 do Micro:bita wykładowcy, który będzie podłączony do jego komputera przez USB.

**3. Komputer wykładowcy**

Komputer odbierze wiadomość z bramy, przekształci ją do formatu JSON i prześle metodą HTTP POST pod adres mojego API.

**4. REST API – Python FastAPI**

Moje API odpowiada za odbieranie wyników, sprawdzanie danych oraz przekazywanie ich do bazy Firebase.

**5. Firebase Realtime Database**

Internetowa baza danych przechowuje identyfikatory graczy, uzyskane wyniki oraz daty i godziny zapisów.

**6. Strona internetowa**

Docelowo przygotuję stronę WWW w HTML, CSS i JavaScript, która będzie wyświetlała ranking graczy.

Nie planuję rankingu na dodatkowym urządzeniu fizycznym, ponieważ jest opcjonalny.

## 3. Standard komunikacji

### Wiadomość wejściowa – String

Zgodnie ze standardem ustalonym przez wykładowcę Micro:bit będzie wysyłał wiadomość:

`id:<wartość>;wynik:<wartość>;adresAPI:<wartość>`

Przykład:

`id:001;wynik:950;adresAPI:https://microbit-reflex-game.vercel.app/results`

Komunikacja radiowa będzie wykorzystywać grupę **67**, bez dodatkowego szyfrowania wiadomości.

### Wiadomość HTTP POST – JSON

Komputer wykładowcy będzie wysyłał do mojego API obiekt:

```json
{
  "id": "001",
  "wynik": 950
}
```

Adres endpointu:

`https://microbit-reflex-game.vercel.app/results`

## 4. API

API przygotowałem w Pythonie z wykorzystaniem frameworka FastAPI.

Aktualnie zaimplementowałem:

- **GET /** – sprawdzenie działania API.
- **POST /results** – przyjmowanie i zapisywanie wyników w Firebase.

Docelowo dodam:

- **GET /ranking** – pobieranie rankingu graczy.

API zostało opublikowane na platformie Vercel.

**Adres usługi:**

https://microbit-reflex-game.vercel.app/

**Dokumentacja Swagger UI:**

https://microbit-reflex-game.vercel.app/docs

## 5. Sposób zapisu danych w bazie

Do przechowywania wyników wykorzystuję Firebase Realtime Database.

Każda rozgrywka jest zapisywana jako osobny rekord zawierający trzy pola:

| Pole | Typ danych | Znaczenie |
|---|---|---|
| id | String | Identyfikator gracza |
| wynik | Integer | Uzyskany wynik |
| data | String | Data i godzina zapisu |

Datę i godzinę automatycznie dodaje API.

Firebase generuje również unikalny klucz dla każdego rekordu, dzięki czemu jeden użytkownik może mieć wiele zapisanych wyników.

## 6. Ranking internetowy

W kolejnym etapie przygotuję prostą stronę internetową w HTML, CSS i JavaScript.

Strona będzie pobierała wyniki z API i wyświetlała je w formie rankingu, uporządkowanego od najwyższego wyniku.

Ranking będzie dostępny przez publiczny adres WWW.

## 7. Diagram architektury C4

Przygotowałem model architektury systemu w diagrams.net, obejmujący cztery poziomy:

- C1 – kontekst systemu.
- C2 – kontenery i komunikacja.
- C3 – komponenty API.
- C4 – planowana struktura kodu.

[Diagram C4 – plik edytowalny](https://github.com/jakubmatwiej/Microbit-Reflex-Game/blob/main/Microbit-Reflex-Game-C4-komplet.drawio)

## 8. Wykorzystane technologie

- BBC Micro:bit
- Microsoft MakeCode
- Python
- FastAPI
- Firebase Realtime Database
- HTTP / HTTPS / JSON
- Vercel
- HTML, CSS, JavaScript
- GitHub
- diagrams.net

## 9. Aktualny postęp projektu

**Zrealizowane:**

- Opracowanie koncepcji i architektury systemu.
- Przygotowanie diagramów C4.
- Utworzenie repozytorium GitHub.
- Konfiguracja środowiska Python i FastAPI.
- Implementacja endpointu POST /results.
- Utworzenie bazy Firebase Realtime Database.
- Połączenie API z bazą danych.
- Automatyczne dodawanie daty i godziny zapisu.
- Publikacja API na Vercel.
- Przetestowanie publicznego endpointu HTTP POST – odpowiedź 200 OK.

**Pozostało do wykonania:**

- Implementacja endpointu GET /ranking.
- Przygotowanie strony WWW z rankingiem.
- Programowanie gry w Microsoft MakeCode.
- Wysyłanie wiadomości radiowych na grupie 67.
- Integracja z bramą wykładowcy.
- Testy końcowe całego systemu.

## 10. Aktualny status

Aktualnie mam działające, publicznie dostępne API połączone z internetową bazą Firebase. Przeprowadziłem pomyślny test przesłania danych JSON metodą HTTP POST i zapisu wyniku w bazie danych.

Pozostałe elementy projektu będę rozwijał w kolejnych etapach.

Mechanizm uwierzytelniania żądań API pozostaje do ustalenia. Obecny endpoint zapisu ma charakter testowy.
