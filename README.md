# powerpuff-girls

Wij hebben de case smartgrid gekozen. Smartgrid is een gesimplificeerde versie van een energiegrid. Het grid bestaat uit `Houses`, `Cables` en `Batteries`, deze zullen later in onze code als classes worden aangmaakt. Hierover later meer. De huizen vragen allemaal een bepaalde stroomcapaciteit en bevinden zich ergens in het grid. De kabels worden vanaf elk huis getrokken door het grid en hebben een kosten per kabelstuk aangeduid als een kosten per segment. De batterijen hebben allemaal een eigen capaciteit aan stroom die ze kunnen leveren en liggen ook ergens in het grid. De batterijen komen ook met hun eigen kosten per batterij. Het doel van Smartgrid is het verbinden van alle huizen met de batterijen tegen zo laag mogelijke kosten. 

- Voor het eerste gedeelte van de case hoeft er geen rekening gehouden te worden met gedeelde kabelsegemnten. Hiernaast hebben de        batterijen allemaal dezelfde capaciteit en zijn ze even duur. Dit zorgt voor de volgende kostenfunctie:
```python
self.cost = self.batteries * 5000 + total_lenghth * 9
```

- In het tweede gedeelte van de case zijn er drie soorten batterijen, elk met een verschillende kosten en capaciteit. Kabels die over elkaar heen lopen en naar dezelfde batterij kunnen gedeeld worden waardoor er een kostenvermindering onstaat. De nieuwe kostenfunctie is:
``` python
DIT MOET ANDERS!
self.cost = self.batteries * 5000 + (total_length - total_shared_cables) * 9
```




## Repository KLOPT NOG NIET VOLLEDIG (Check na cleanen)

- `classes`:            Hierin staan alle classes en algoritmen
- `figures`:            Hier worden alle plots van visualize cost opgeslagen EN OOK DIE VAN HILLCLIMBER COST DECREASE
- `huizen_batterijen`:  De data van de grids waarmee we werken
- `main.py`:            Hier roep je alle functies en de verschillende algoritmen aan
- `experiment.py`:      Functie die een aantal experimenten runt om een kostenverdeling csv te produceren
- `visualize_cost.py`:  Functie die de kosten visualiseert van een aantal experimenten gebruikmakend van de csv van experiment.py.

## Leg hier Main uit. Wat moet je doen om het aan de praat te krijgen
Je runt de Main door in je terminal `python main.py` te typen.

`main.py` gebruikt de functie `access_data()` om de csv files met de informatie over de huizen batterijen in te lezen, en slaat deze op in de variabelen `batteries` en `houses`. 

## Leg hier experiment uit. Wat moet je doen om het aan de praat te krijgen
De `experiment` functie wordt aangeroepen en krijgt de volgende parameters meegegeven:
iteraties=eigen input, algoritme=Greedy_Random of Greedy_Random_kmeans, houses=houses, batteries=batteries, file_name='eigen input'.
Deze functie moet in de main worden aangeroepen en vervolgens voer je dus de main uit.


## Leg hier visualize cost uit uit. Wat moet je doen om het aan de praat te krijgen

## Classes Hier komen classes en algoritmes en hoe ze werken
Bij kmeans warning message voorkomen door:
