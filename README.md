# powerpuff-girls

Wij hebben de case smartgrid gekozen. Smartgrid is een gesimplificeerde versie van een energiegrid. Het grid bestaat uit `Houses`, `Cables` en `Batteries`, deze zullen later in onze code als classes worden aangmaakt. Hierover later meer. De huizen vragen allemaal een bepaalde stroomcapaciteit en bevinden zich ergens in het grid. De kabels worden vanaf elk huis getrokken door het grid en hebben een kosten per kabelstuk aangeduid als een kosten per segment. De batterijen hebben allemaal een capaciteit aan stroom die ze kunnen leveren en liggen ook ergens in het grid. De batterijen komen ook met hun eigen kosten per batterij. Het doel van Smartgrid is het verbinden van alle huizen met de batterijen tegen zo laag mogelijke kosten. 

- Voor het eerste gedeelte van de case hoeft er geen rekening gehouden te worden met gedeelde kabelsegemnten. Hiernaast hebben de        batterijen allemaal dezelfde capaciteit en zijn ze even duur. Dit zorgt voor de volgende kostenfunctie:
```python
self.cost = self.batteries * 5000 + total_lenghth * 9
```

- In het tweede gedeelte van de case is het ook mogelijk om kabels te delen. Kabels die over elkaar heen lopen en naar dezelfde batterij kunnen kunnen leveren een kostenvermindering op. De nieuwe kostenfunctie is:
``` python
self.cost = self.batteries * 5000 + (total_length - total_shared_cables) * 9
```

### Indeling repository

- `classes`:            Hierin staan alle classes en algoritmen
- `figures`:            Hier worden alle plots van visualize cost opgeslagen EN OOK DIE VAN HILLCLIMBER COST DECREASE
- `huizen_batterijen`:  De data van de grids waarmee we werken
- `access_data.py`:     Leest de csv met info voor de grid
- `main.py`:            Hier roep je alle functies en de verschillende algoritmen aan
- `experiment.py`:      Functie die een aantal experimenten runt om een kostenverdeling csv te produceren
- `visualize_cost.py`:  Functie die de kosten visualiseert van een aantal experimenten gebruikmakend van de csv van experiment.py
- `results.csv`:        Hier worden de kosten die uit ecperiment komen opgeslagen.

#### `main.py`
Je runt de Main door in je terminal `python main.py` te typen.

`main.py` gebruikt de functie `access_data()` om de csv files met de informatie over de huizen batterijen in te lezen, en slaat deze op in de variabelen `batteries` en `houses`. 

#### `experiment.py`
De `experiment.py` functie wordt aangeroepen in de main en krijgt de volgende parameters meegegeven:
- `iteraties`: Deze kun je zelf bepalen door het getal aan te passen als je de experiment functie aanroept
- `algoritme`: Keuze uit de twee algoritmen: Greedy_Random of Greedy_Random_kmeans, zelf invullen
- `houses`: De informatie van de huizen
- `batteries`: De informatie van de batterijen
- `file_name`: Welke naam je het bestand wilt geven, in de vorm van een string.

De output van experiments is een csv file, `results.csv` met kosten voor elk grid. Deze csv wordt gebruikt als input voor `visualise_cost.py`

#### `visualize_cost.py` 
De `visualize_cost.py` functie wordt gebruikt voor het visualiseren van de kostenspreiding van meerdere grids met hetzelfde algoritme. De input parameters zijn:
- `results.csv`: Een csv, de output van experiments
- `pathname.png`: Een png, deze wordt opgeslagen in het pad dat je aangeeft. Wij slaan alles op in `figures`. Dit moet je zelf specificeren

### Classes
In classes staan alle classes en algoritmen.

De eenvoudige classes zijn:
- `House`: Krijgt `pos_x`, `pos_y`, `capacity` mee
- `Battery`: Krijgt `pos_x`, `pos_y`, `capacity` mee en heeft ook een `used_capacity` die op 0 staat aan het begin.
- `Cables`: Kan een lijst aan coordinaten opslaan. Dit is een kabel
- `Grid`: Grid simuleert een heel aangelegd grid van kabel batterijen en huizen. Deze grid wordt gebruikt voor ons `greedy_random` algoritme
- `Grid_k_means`: Een aangepaste grid voor het algoritme kmeansdie een numpy array maakt van de huiscoordinaten. 

### Algoritmen:
#### `greedy_random`: 
Dit constructieve algoritme neemt een grid en legt een kabel in random stappen neer. Het berekend eerst welke batterij de kleinste Manhattan distance heeft van de huizen. Deze huizen worden met die huizen verbonden zo lang de capaciteit van de batterij niet oeverschreden wordt. Omdat de huizen niet met random batterijen verbonden worden maar met de dihtstbijzijnde batterij met voldoende capaciteit is het greedy. De stappen die de kabel legt zijn elke stap random in de x of de y richting totdat de batterij bereikt is.

#### `greedy_random_k_means`: 
Dit constructieve algoritme neemt een grid en legt een kabel in random stappen neer. In dit algoritme moeten de locaties van de batterij nog gekozen worden. Hiervoor gebruiken we een heuristiek. Deze gaat er van uit dat huizen die dicht bij elkaar liggen zo veel mogelijk aan dezelfde batterij verbonden worden om kabelkosten per segment te besparen. De huizen worden door K-Means in clusters opgedeeld die volgens de euclidische afstand het dichtst bij elkaar liggen. De batterijen liggen nu midden in deze clusters. Hierna wordt greedy_random gebruikt om de batterijen met de kortste Manhatten_distance van de huizen aan deze huizen te verbinden met kabels.

#### `hill_climber`: 
Dit iteratieve algoritme krijgt als input een grid en probeert de kosten te verlagen van dit grid. Het doet een aantal iteraties. Bij elke iteratie pakt het een random kabel en legt deze opnieuw aan. Als dit leid tot kostenverlaging wordt de oude kabel vervangen met deze betere kabel.



