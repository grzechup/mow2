2021-03-25
==========

## Done

- Które sensory mają dużo pomiarów?
- Agregacja na przedziale czasowym - feature vector
- Wizualizacja sensorów

## Pytania, dalsze cele

### Wektor danych uczących, target
#### Feature verctor
Bazując na uśrednionych danych z 1 dnia, 2 dni, Pon-piątek

#### Target
Przewidujemy stan pm1, pm10, pm25 na jutro, na najbliższy tydzień, na weekend.


### Baseline model - regresja
Prosty model predykcyjny dla jednego sensora (zawierającego najwiecej danych).  
Czy sensor potrafi przewidywać swoje pomiary?

Bierzemy dane z jednego dnia (pogoda + pm), przewidujemy pm następnego dnia.



### Definicja stanu powietrza w całym Krakowie
- uśrednione wartości (pm1, pm10, pm25) ze wszystkich dostępnych sensorów?
- wykrycie/odrzucenie sensorów - outlierów
- np. sonsor przy dużej ulicy


### Model predykcyjny w oparciu o zagregowane dane ze wszystkich/dostępnych sensorów.
- Czy bazując na danych z wielu sensorów da się przewidywać ogólne/średnie stężenie pyłów w Krakowie?
- Czy istnieje jeden/kilka sensorów które najlepiej przewidują ogólne/średnie stężenie pyłów w Krakowie?

### Uzupełnienie danych brakujących
- uśrednienie z istniejących sensorów
- info o pogodzie z zewnętrznego żródła


### Uwagi   
Wszystkie kolumny są ordinal, nie ma potrzeby korzystania z one-hot encoding.