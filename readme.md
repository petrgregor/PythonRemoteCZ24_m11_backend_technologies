# Projekt Hollymovies

Filmová databáze.

## Funkcionalita

-[ ] informace o filmu
-[ ] informace o režisérech/hercích
-[ ] vkládání/editace/mazání filmu, režiséra, herce,...
-[ ] hodnocení filmu
-[ ] filtrování filmů na základě žánru, roku, herce, země...
-[ ] seřazení filmů podle ratingu, roku,...
-[ ] vyhledávání filmu/režiséra/herce...

## Databáze

-[ ] movie
  -[ ] id
  -[ ] title_orig
  -[ ] title_cz
  -[ ] year
  -[ ] length (min)
  -[ ] novel_id -> novel
  -[ ] productions (n:m -> production_company)
  -[ ] directors (n:m -> creator)
  -[ ] actors (n:m -> creator)
  -[ ] countries (n:m -> country)
  -[ ] genres (n:m -> genre)
  -[ ] rating
  -[ ] medias (n:m -> media)
  -[ ] awards (n:m -> award)
  -[ ] description
  -[ ] reviews -> review
-[ ] review
  -[ ] id
  -[ ] movie_id -> movie
  -[ ] reviewer -> user 
  -[ ] rating
  -[ ] comment 
  -[ ] time  
-[ ] award
  -[ ] id
  -[ ] name (-> award_name)
  -[ ] category (-> category_name)
  -[ ] year 
-[ ] production_company
  -[ ] id
  -[ ] name
  -[ ] foundation_year
  -[ ] country_id
-[ ] novel
  -[ ] id  
  -[ ] title
  -[ ] author -> creator
-[ ] creator
  -[ ] id
  -[ ] first_name
  -[ ] last_name
  -[ ] date_of_birth
  -[ ] date_of_death
  -[ ] nationality -> country
  -[ ] biography
  -[ ] awards (n:m -> award)
  -[ ] movies_actor (n:m -> movie)
  -[ ] movies_director (n:m -> movie)
-[ ] genre
  -[ ] id
  -[ ] name
-[ ] country
  -[ ] id
  -[ ] name
-[ ] user
  -[ ] id
  -[ ] username
  -[ ] first_name
  -[ ] last_name
-[ ] media
  -[ ] id
  -[ ] type (image/video/text/sound)
  -[ ] url
  -[ ] movie_id -> movie
  -[ ] actors (n:m -> creators)
  -[ ] description


# Finální projekt - rady

- jeden člen týmu vytvoří projekt
  - nainstaluje Django:
```bash
pip install django
```
  - vytvoří soubor requirements.txt
```bash
pip freeze > requirements.txt
```
  - vytvoří Django projekt
```bash
django-admin startproject <nazev_projektu> . 
```
  - vytvoří git repozitář
    - vytvoří .gitignore soubor 
    - odešle ho na GitHub
    - nasdílí ostatním členům v týmu adresu repozitáře
    - nastaví spolupracovníky (Settings -> Collaborators -> Add people)
- ostatní členové
  - naklonují si projekt
  - vytvoří virtuální prostředí (.venv)
  - nainstalují potřebné balíčky ze souboru requirements.txt
```bash
pip install -r requirements.txt
```
- vytvořit readme.md soubor
  - popis projektu
  - může být anglicky (preferováno) nebo česky
  - může obsahovat ER diagram
  - může obsahovat screenshoty

