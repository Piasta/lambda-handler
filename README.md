# lambda-handler
Zadanie 2.
Zapoznaj się z dokumentacją czym jest funkcja Lambda na AWS:
https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
Utwórz analogicznie jak w powyższej dokumentacji, funkcję, która pobiera pliki .csv, następnie
tworzy z nich jeden plik .json i wyświetla dostępną paletę kolorów farb. Oprócz zapisu koloru HEX
dodaj jeszcze zapis RGB. Pliki trafiają do funkcji z S3 Bucketa (S3 Bucket powinien być MOCKIEM)
Ogólna postać funkcji wygląda następująco.

def handler_name(event, context):
...
return some_value

Event – jest payload, który przychodzi do funkcji, json, zawiera informacje o typie i liczbie plików.
Context – obiekt, który udostępnia metody i właściwości, które dostarczają informacji o wywołaniu,
funkcji i środowisku wykonawczym, może być pomijany w tym ćwiczeniu.
Rozwiązanie zadania powinno znaleźć się w repozytorium publicznym na Githubie.
Proszę o zamieszczenie pliku .txt z linkiem do repozytorium, w którym znajdują się zadania.
