# Projekt Hollymovies

Filmová databáze.

## Struktura projektu
- `hollymovies` - složka projektu (obsahuje informace o celém projektu)
  - `__init.py__` - je zde jen proto, aby daná složka byla package
  - `asgi.py` - nebudeme používat
  - `settings.py` - nastavení celého projektu
  - `urls.py` - zde jsou definované url cesty
  - `wsgi.py` - nebudeme používat

## Spuštění projektu/serveru
```bash
python manage.py runserver
```

Případně můžeme zadat i číslo portu:
```bash
python manage.py runserver 8001
```

## Vytvoření aplikace
```bash
python manage.py startapp viewer
```

> [!WARNING]  
> Nesmíme zapomenout zaregistrovat aplikaci do souboru `settings.py`:
> ```python
> INSTALLED_APPS = [
>     'django.contrib.admin',
>     'django.contrib.auth',
>     'django.contrib.contenttypes',
>     'django.contrib.sessions',
>     'django.contrib.messages',
>     'django.contrib.staticfiles',
> 
>     'viewer',
> ]
> ```

### Struktura aplikace
- `viewer` - složka aplikace
  - `migrations` - složka obsahující migrační skripty
  - `__init__.py` - prázný soubor, slouží k tomu, aby složka fungovala jako package
  - `admin.py` - zde uvádíme modely, které se budou zobrazovat v admin sekci
  - `apps.py` - nastavení aplikace
  - `models.py` - definice modelů (schéma databáze)
  - `tests.py` - testy
  - `views.py` - funcionalita

## Funkcionalita

- [ ] informace o filmu
- [ ] informace o režisérech/hercích
- [ ] vkládání/editace/mazání filmu, režiséra, herce,...
- [ ] hodnocení filmu
- [ ] filtrování filmů na základě žánru, roku, herce, země...
- [ ] seřazení filmů podle ratingu, roku,...
- [ ] vyhledávání filmu/režiséra/herce...

## Databáze

### Modely

- [x] genre
  - [x] id
  - [x] name
- [x] country
  - [x] id
  - [x] name
- [ ] creator
  - [x] id
  - [x] first_name
  - [x] last_name
  - [x] date_of_birth
  - [x] date_of_death
  - [x] nationality -> country
  - [x] biography
  - [ ] awards (n:m -> award)
  - [ ] movies_actor (n:m -> movie)
  - [ ] movies_director (n:m -> movie)
- [ ] movie
  - [x] id
  - [x] title_orig
  - [x] title_cz
  - [x] year
  - [x] length (min)
  - [ ] novel_id -> novel
  - [ ] productions (n:m -> production_company)
  - [x] directors (n:m -> creator)
  - [x] actors (n:m -> creator)
  - [x] countries (n:m -> country)
  - [x] genres (n:m -> genre)
  - [ ] rating
  - [ ] medias (n:m -> media)
  - [ ] awards (n:m -> award)
  - [x] description
  - [ ] reviews -> review
- [ ] review
  - [ ] id
  - [ ] movie_id -> movie
  - [ ] reviewer -> user 
  - [ ] rating
  - [ ] comment 
  - [ ] time  
- [ ] award
  - [ ] id
  - [ ] name (-> award_name)
  - [ ] category (-> category_name)
  - [ ] year 
- [ ] production_company
  - [ ] id
  - [ ] name
  - [ ] foundation_year
  - [ ] country_id
- [ ] novel
  - [ ] id  
  - [ ] title
  - [ ] author -> creator
- [ ] user
  - [ ] id
  - [ ] username
  - [ ] first_name
  - [ ] last_name
- [ ] media
  - [ ] id
  - [ ] type (image/video/text/sound)
  - [ ] url
  - [ ] movie_id -> movie
  - [ ] actors (n:m -> creators)
  - [ ] description

### Migrace
Při každé změně v modelech musíme provést migraci databáze:
- vytvoření migračního skriptu:
```bash
python manage.py makemigration
```
- spuštění migrace:
```bash
python manage.py migrate 
```

> [!INFO]
> Migrační skripty by měli být součástí repozitáře.

> [!WARNING]  
> Databázový soubor není součástí repozitáře, což znamená, že může dojít k situaci, kdy v nějaké
> branch či commit nebude zdrojový kód odpovídat aktuálnímu schématu v databázi

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
  - nainstaluje dotenv:
```bash
pip install python-dotenv
```
  - vytvoří soubor `.env`, který bude obsahovat citlivé informace
  - vytvoří git repozitář
    - vytvoří .gitignore soubor 
    - do .gitignore vloží:
    ```git
    /.idea/*
    /db.sqlite3
    /.env
    ```
    - odešle ho na GitHub
    - nasdílí ostatním členům v týmu adresu repozitáře
    - nastaví spolupracovníky (Settings -> Collaborators -> Add people)
- ostatní členové
  - naklonují si projekt
  - vytvoří virtuální prostředí (.venv)
  - nainstalují potřebné balíčky ze souboru requirements.txt
  - vytvoří `.env` soubor obsahující SECURITY_KEY
```bash
pip install -r requirements.txt
```
- vytvořit readme.md soubor
  - popis projektu
  - může být anglicky (preferováno) nebo česky
  - může obsahovat ER diagram
  - může obsahovat screenshoty

