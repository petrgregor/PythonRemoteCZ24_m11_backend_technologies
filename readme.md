# Projekt Hollymovies

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

