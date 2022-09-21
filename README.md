# TextMining

## Objection <br>
Cette analyse consiste à la construction d'un modèle permettant de déterminer l’impact d’une allergie quelconque sur la qualité de la nutrition proposée par auchan.

## Plan de travail
Etape 1 : **Le Web Scrapping** 
Etape 2 : **Le traitement de nos données** 
Etape 3 : **L’analyse** 

## Detail du plan 

**Etape 1 : Le Web Scrapping** <br>

Il s’agît de l’étape fondamentale de notre projet. Nous y extrayons les données nécessaire afin de réaliser notre analyse.
Nous récoltons nos données dans le site internet propriétaire d’Auchan. L’extraction se fait à même le code source de la page 
notamment à l’aide de packages spécialisés tels que « BeautifulSoup » ou encore « urllib »
Nous avons pu noter 2 difficultés dans ce premier travail :
  - D’une part l’identification d’un URL central permettant d’accéder aux différentes catégories de produit.
  - Et d’autre part, l’extraction via des balises clés dans lesquelles sont contenues les informations nécessaires.<br>


**Etape 2 : Le traitement de nos données**

Maintenant que les données sont extraites, il nous faut les adapter. En effet, ces données sont brutes et par conséquent pas adaptées à l’analyse. 
Pour se faire nous utiliserons principalement deux nouveaux packages:
  - Le package « Regex » qui nous permettra de modifier nos les données textuelles de notre base de données (suppression des points/virgules, suppression des s en fin de mots, modification de polices, …)<br>
  - Le package « nltk » qui, lui, nous permettra de tokeniser nos différents termes afin de mener notre analyse à son terme.<br>


**Etape 3 : L’analyse** 

Nous allons utiliser un modèle logistique multiclasse. Le modèle logistique multiclasse étend le modèle standard en permettant d’augmenter le nombre de variable à prédire (on pourra avoir trois classes ou plus). Nous chercherons ici un lien entre les mots plus fréquents dans les ingrédients et le score nutritionnel associé au produit. Nous utiliseront la librairie sci-kit learn pour développer notre modèle.






.
