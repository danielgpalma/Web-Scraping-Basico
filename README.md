# Web Scraping Basico

Este repositorio se realiza con la finalidad de mostrar un ejemplo de como hacer web scraping con Xpath.
En este se lleva acabo un scraping de la pagina Wikidex, de la cual se extraera informacion de los Pokemons existentes en la generacion 9 del nuevo juego de Nintendo Pokemon Escarlata/Purpura.

## Informacion a Extraer

* Nombre
* Tipo primario
* Tipo secundario (en caso de tener)
* Puntos de Salud Maximo
* Puntos de Salud Minimo
* Ataque Maximo
* Ataque Minimo
* Defensa Maximo
* Defensa Minimo
* Ataque Especial Maximo
* Ataque Especial Minimo
* Defensa Especial Maximo
* Defensa Especial Minimo
* Velocidad Maximo
* Velocidad Minimo

Todos estos datos se recopilan de la pagina [Wikidex](https://www.wikidex.net/wiki/Lista_de_Pok%C3%A9mon_seg%C3%BAn_la_Pok%C3%A9dex_de_Paldea) la cual nos proporciona la informacion, no se comprueba su veracidad y unicamente son para la demostracion del ejercicio de Web Scraping.

## Resultados

Con la libreria de pandas se maneja la informacion para crear un archivo .csv en el cual se encontraran los datos ordenados del Pokemon numero 1 al 514 y en las columnas se encontraran los datos mencionados anteriormente.

No se lleva a cabo la tarea de preprocesamiento del .csv por lo cual puede incluir corchetes, saltos de linea e informacion adicional.
