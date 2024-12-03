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

- [x] seznam všech filmů (movies)
- [x] informace o filmu (viewer/movie-detail)
- [x] informace o režisérech/hercích (viewer/creator-details)
- [x] tvůrce
  - [x] vkládání
  - [x] editace
  - [x] mazání
- [x] film   
  - [x] vkládání  
  - [x] editace  
  - [x] mazání  
- [x] hodnocení filmu
- [ ] filtrování filmů na základě: 
  - [x] žánru, (viewer/genre-detail)
  - [ ] roku, 
  - [x] herce, 
  - [ ] země  # TODO
- [ ] seřazení filmů podle ratingu, roku,...
- [x] vyhledávání filmu/režiséra/herce...

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
  - [x] movies_actor (n:m -> movie)
  - [x] movies_director (n:m -> movie)
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
  - [x] rating
  - [ ] medias (n:m -> media)
  - [ ] awards (n:m -> award)
  - [x] description
  - [x] reviews -> review
- [x] review
  - [x] id
  - [x] movie_id -> movie
  - [x] reviewer -> user 
  - [x] rating
  - [x] comment 
  - [x] time  
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
- [x] user
  - [x] id
  - [x] username
  - [x] first_name
  - [x] last_name
- [ ] media
  - [ ] id
  - [ ] type (image/video/text/sound)
  - [ ] url
  - [ ] movie_id -> movie
  - [ ] actors (n:m -> creators)
  - [ ] description
- [x] image
  - [x] id
  - [x] image
  - [x] movie_id -> movie
  - [x] actors (n:m -> creators)
  - [x] description

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

## DUMP/LOAD databáze (export/import) s UTF znaky
Nainstalujeme rozšíření:
```bash
pip install django-dump-load-utf8
```

Přidáme `'django_dump_load_utf8'` do `INSTALLED_APPS` v souboru `settings.py`.

Export (DUMP):
```bash
python manage.py dumpdatautf8 viewer --output ./files/fixtures.json
```

Import (LOAD):
```bash
python manage.py loaddatautf8 ./files/fixtures.json
```

## Dotazy do databáze
### .all()
Vrací kolekci všech nalezených záznamů z dané tabulky:
`Movie.objects.all()`

### .get()
Vrací jeden nalezený záznam pro dané podmínky:
`Movie.objects.get(id=3)`

### .filter()
Vrací kolekci záznamů, které splňují podmínky:
`Movie.objects.filter(id=3)`

`Movie.objects.filter(year=1994)`

`Movie.objects.filter(title_orig="The Green Mile")`

`drama = Genre.objects.get(name="Drama")`

`Movie.objects.filter(genres=drama)`

`Movie.objects.filter(genres=Genre.objects.get(name="Krimi"))`

`Movie.objects.filter(genres__name="Drama")`

`Creator.objects.filter(date_of_birth__year=1955)`

`Movie.objects.filter(year=1995)`

`Movie.objects.filter(year__gt=1995)` -- `gt` => "větší než" (greater then)

`Movie.objects.filter(year__gte=1995)` -- `gte` => "větší nebo rovno" (greater then equal)

`Movie.objects.filter(year__lt=1995)` -- `lt` => "menší než" (less then)

`Movie.objects.filter(year__lte=1995)` -- `lte` => "menší nebo rovno" (less then equal)

`Movie.objects.filter(title_orig__contains="The")`

`Movie.objects.filter(title_orig__in=['Se7en', 'Forrest Gump'])`

`Movie.objects.exclude(title_orig="Se7en")`

Test, jestli hledaný záznam existuje:
`Movie.objects.filter(year=1990).exists()`

Spočítáme počet vyhovujících záznamů:
`Movie.objects.all().count()`

`Movie.objects.filter(year=1994).count()`

Uspořádání výsledků dotazu:
`Movie.objects.all()`

`Movie.objects.all().order_by('year')` -- uspořádání vzestupně

`Movie.objects.all().order_by('-year')` -- uspořádání sestupně

## Manipulace s daty
### Vytvoření nového záznamu (create)
`Genre.objects.create(name="Dokumentární")`

```python
genre = Genre(name="Sci-fi")
genre.save()
```

### Úprava existujícího záznamu (update)
```python
scifi = Genre.objects.get(name="Sci-fi")
scifi.name = "SciFi"
scifi.save()
```

### Smazání záznamu (delete)
`Genre.objects.get(name="SciFi").delete()`

> [!WARNING] 
> Data se do databáze nahrají i se svým id, tedy dojde k přepisu již existujících záznamů.

## Testy
V každé aplikaci máme soubor `tests.py`, do kterého můžeme vkládat testy. 
Můžeme vytvořit další testovací soubory, je ale vhodné, aby název začínal `test*.py`.

Testování spustíme příkazem `python manage.py test` - tento příkaz spustí všechny testy 
ve všech souborech začínajích `test`.

Příkaz `python manage.py test viewer.test_models` spustí testování definované v souboru `test_models` v 
aplikaci `viewer`.

Základní testy se spouštějí na virtuální databázi, která obsahuje stejné tabulky jako projektová databáze,
ale je prázdná.

### GUI
Pro testování GUI si nainstalujeme selenium (pro práci s webovou stránkou): 
`pip install selenium`.

Během testování musí být spuštěn server.

> [!WARNING] 
> Zde již pracujeme s reálnou aplikací a tedy i s reálnými daty v databázi.

## Image
Nainstalujeme Pillow knihovnu `pip install Pillow`

V modelech můžeme využít `ImageField`: `image = ImageField(upload_to='images/', defaulf=None, null=False, blank=False')` 

Provedeme migraci.

V `settings.py` přidáme cesty:
```python
MEDIA_ROOT = BASE_DIR
MEDIA_URL = 'images/'
```

Do `urls.py` přidáme za konec seznamu urlpatterns:
`+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`

Aby fungovalo odesílání souboru přes formulář, musí obsahovat:
`<form method="post" enctype="multipart/form-data">`

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

