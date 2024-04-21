# get_terrain_heights_from_gugik

Scripts developed and tested on Ubuntu 22.04.3 LTS with Python 3.10.12.

## About GUGIK NMT

### API

GUGIK NMT (Główny Urząd Geodezji i Kartografii - Numeryczny Model Terenu) allows to get Poland terrain heigths via API. Heights can be retrieved for a single point as well as for multiple points at once. However, I don't recommned retrievieng multiple points because in case of error returned is 0. It is very hard to debug and to distinguish real 0 and error 0. The API is not efficient, it may take days to get some terrain model. Anyway it can be useful to get some heights of terrain.

### Coordinates

When calling API, x and y coordinates need to be provided. X and y need to be in PUWG92 coordinate system. You can check coordinates you need in geoportal web page. This system is confusing, in particular x is replaced with y.

### WARNING !

GUGIK NMT is public API and you shouldn't stress it too much because they may accuse you of DDOS attack. Author of this software doesn't take ANY responsibility for inapropriate usage.

## Script usage

### Generate API calls

Edit config and put your base dir. Edit generate_calls_example.py: add your coordinates and other things. Run generate_calls_example.py.

### Execute calls

get_from_gugik.py will execute API calls generated by generate_calls_example.py. Result files are in CSV format. Call example: get_from_gugik_example.sh

### Correct errors

In result CSV files there may be errors like HTTP Error 502: Bad Gateway. To correct errors run correct_errors.py. Example call: correct_errors_example.sh


===================teraz po polsku / polish version========================

Skrypty odpalane na Ubuntu 22.04.3 LTS z Pythonem 3.10.12.

## O GUGIK NMT

### API

GUGIK NMT (Główny Urząd Geodezji i Kartografii - Numeryczny Model Terenu) pozwala na pobranie wysokości nad poziomem morza dowolnego punktu w Polsce. Można pobierać pojedyńcze punkty jak i całe grupy punktów. Jednakże w przypadku grup punktów jeśli jest błąd to zwracane jest 0. Niestety jest to bardzo trudne w debugowaniu bo nie wiadomo które 0 to error a które to prawdziwe 0 nad poziomem morza. API nie jest zbyt wydajne w związku z czym pobieranie jakiegoś większego modelu może zająć dni.

### Współrzędne

Do wywołań API potrzebne są współrzędne z systemu PUWG92. Te współrzędne można odczytać w geoportalu. W PUWG92 x jest zamieniony z y czyli oś y jest równoległa do równoleżników a oś x jest równoległa do południków.

### UWAGA !

GUGIK NMT jest publicznym API i nie wolno go zbyt mocno obciążać. Jak przyjadą bagiety i oskarżą Was o DDOS to nie mówcie że nie ostrzegałem. Autor tego oprogramowania nie ponosi ŻADNEJ odpowiedzialności za nieprawidłowe użycie. 

## Użycie skryptów

### Generowanie zapytań API

Należy wyedytować config i dodać główny katalog. Następnie należy wyedytować generate_calls_example.py i dodać współrzędne i inne parametry. Uruchamiamy generate_calls_example.py który wygeneruje plik z zapytaniami API. 

### Odpalenie zapytań do API

get_from_gugik.py odpali zapytania API wygenerowane przez generate_calls_example.py. Wynikowe pliki w formacie CSV. Przykład wywołania get_from_gugik_example.sh

### Naprawa błędów

W wynikowym CSV mogą być błędy typu HTTP Error 502: Bad Gateway. Aby je poprawić należy odpalić run correct_errors.py. Przykładowe wywołanie: correct_errors_example.sh

===================Further processing of result files=============================

Result files can be converted to ESRI grid using [esri_grid_helper](https://github.com/kowalpy/esri_grid_helper)

===================Example 3D Poland downloaded from GUGIK========================

Don't ask how much time it took to download whole Poland...

![alt text](https://github.com/kowalpy/get_terrain_heights_from_gugik/blob/main/img/polska_3d.png "Example of 3D Poland based on GUGIK data")

Model printed on 3D printer:

![alt text](https://github.com/kowalpy/get_terrain_heights_from_gugik/blob/main/img/Polska_3d_printout.jpg "Example of 3D Poland printout")

