# Pokemon Scraper 

_Programa que extrae la informacion referente a los Pokemons de la web [pokemondb](https://pokemondb.net/pokedex/all)_



<img src="https://user-images.githubusercontent.com/54951789/113504827-0a19bc80-953b-11eb-857a-38bb5bfedde6.jpg" width="250" height="200">

Foto de Vincent M.A. Janssen en Pexels


### Pre-requisitos 📋

_Para ejecutar el programa es necesario instalar los siguientes paquetes (ver archivo requiterments.txt)_

```
pip install pandas
pip install requests
pip install beautifulsoup4
```

### Análisis de robots.txt 🔩
_El análisis previo realizado sobre robots.txt de esta web nos asegura que no hay inconveniente en rastrear las urls que contienen la información referente a los Pokémon_

```
User-agent: *
Disallow: /pokebase/login
Disallow: /pokebase/forgot
Disallow: /pokebase/search?
Disallow: /pokebase/revisions
Disallow: /pokebase/meta/login
Disallow: /pokebase/meta/forgot
Disallow: /pokebase/meta/search?
Disallow: /pokebase/meta/revisions
Disallow: /pokebase/rmt/login
Disallow: /pokebase/rmt/forgot
Disallow: /pokebase/rmt/search?
Disallow: /pokebase/rmt/revisions
Crawl-delay: 4

User-agent: Yandex
Crawl-delay: 30

User-agent: SindiceBot
Crawl-delay: 30

User-agent: CCBot
Crawl-Delay: 30

User-agent: wget
Disallow: /

User-agent: WebReaper
Disallow: /

User-agent: AhrefsBot
Disallow: /

Sitemap: https://pokemondb.net/static/sitemaps/pokemondb.xml
Sitemap: https://pokemondb.net/static/sitemaps/pokebase.xml
Sitemap: https://pokemondb.net/static/sitemaps/images.xml
```


## Ejecutando las pruebas 🚀

_El script se debe ejecutar de la siguiente forma_

```
python main.py
```


## Datos Obtenidos 📦

* Name: Nombre del pokemon
* Evolution: Evolución del pokemon
* Type: Clase del Pokemon
* Total: Puntos totales
* HP: Puntos de vida (Hit Points)
* Attack: Mide la fuerza de los movimientos
* Defense: Mide la habilidad de recibir ataques
* Sp.Atk: Mide la fuerza de los movimientos (ataques especiales)
* Sp.Def: Mide la habilidad de recibir ataques (ataques especiales)
* Speed: Define que Pokemon hará el primer movimiento en la batalla
* Species: La especie a la que pertenece
* Height: Altura
* Weight: Peso
* abilities: Habilidades
* ev_yield: Valor de esfuerdo producido (effort value yield)
* catch_rate: probablidad de atraparlo
* base_friendship: Amistad base
* base_experience: Experiencia base
* growth_rate: valocidad de crecimiento
* eggs_groups: Grupos de huevos
* gender_rate: porcentaje de género
* eggs_cycles_rate: ciclo de huevo hasta que eclosiona

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - IDE usado
* [Git](https://git-scm.com/) - Gestor de versiones


## Autor ✒️

* **David López Ujaque** - *Desarrollo del proyecto* - [ujaque](https://github.com/ujaque)

## Licencia 📄

Este proyecto está bajo la Licencia (GNU General Public License v3.0) - mira el archivo [LICENSE.md](https://github.com/ujaque/Pokemon_scraper/blob/master/LICENSE) para detalles

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4661775.svg)](https://doi.org/10.5281/zenodo.4661775)


