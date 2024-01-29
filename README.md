# powerpuff-girls

Wij hebben de case smartgrid gekozen. Smartgrid is een gesimplificeerde versie van een energiegrid. Het grid bestaat uit `Houses`, `Cables` en `Batteries`, deze zullen later in onze code als classes worden aangmaakt. Hierover later meer. De huizen vragen allemaal een bepaalde stroomcapaciteit en bevinden zich ergens in het grid. De kabels worden vanaf elk huis getrokken door het grid en hebben een kosten per kabelstuk aangeduid als een kosten per segment. De batterijen hebben allemaal een eigen capaciteit aan stroom die ze kunnen leveren en liggen ook ergens in het grid. De batterijen komen ook met hun eigen kosten per batterij. Het doel van Smartgrid is het verbinden van alle huizen met de batterijen tegen zo laag mogelijke kosten. 

- Voor het eerste gedeelte van de case hoeft er geen rekening gehouden te worden met gedeelde kabelsegemnten. Hiernaast hebben de        batterijen allemaal dezelfde capaciteit en zijn ze even duur. Dit zorgt voor de volgende kostenfunctie:
```python
self.cost = self.batteries * 5000 + total_lenghth * 9
```

- In het tweede gedeelte van de case zijn er drie soorten batterijen, elk met een verschillende kosten en capaciteit. Kabels die over elkaar heen lopen en naar dezelfde batterij kunnen gedeeld worden waardoor er een kostenvermindering onstaat. De nieuwe kostenfunctie is:
``` python
DIT MOET ANDERS!
self.cost = self.batterie * 5000 + (total_length - total_shared_cables) * 9
```




## Repository 
- `classes`:            Hierin staan alle classes en algoritmen
- `figures`:            Hier worden alle plots van visualize cost opgeslagen
- `huizen_batterijen`:  De data van de grids waarmee we werken
- `main.py`:            Hier roep je alle functies en de verschillende algoritmen aan
- `experiment.py`:      Functie die een aantal experimenten runt om een kostenverdeling csv te produceren
- `visualize_cost.py`:  Functie die de kosten visualiseert van een aantal experimenten gebruikmakend van de csv van experiment.py.
