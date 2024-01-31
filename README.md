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

## Indeling repository

- `classes`:            Hierin staan alle classes en algoritmen
- `figures`:            Hier worden alle plots van visualize cost opgeslagen EN OOK DIE VAN HILLCLIMBER COST DECREASE
- `functies`:           Hierin staan alle functies die `main.py` nodig heeft
- `huizen_batterijen`:  De data van de grids waarmee we werken
- `main.py`:            Hier roep je alle functies en de verschillende algoritmen aan
- `results.csv`:        Hier worden de kosten die uit ecperiment komen opgeslagen.

#### `main.py`
  Je runt de Main door in je terminal `python main.py` te typen.


In de main.py zijn er twee functies die aangeroepen kunnen worden. De eerste functie is de 'run_algorithm' functie.  Deze krijgt de volgende parameters mee:
- `algorithm`: Met deze parameter kies je welk algoritme je wilt runnen. Je hebt de keuze uit Greedy_Random, Greedy_Random_kmeans en Hill_Climber
- `district`: Keuze uit de verschillende districten. Dit kan dus 1, 2, of 3 zijn.
- `visualize`: Boolean die, wanneer hij op True staat, De grid visualiseert
- `output`: Boolean die, wanneer hij op True staat, de output print
- `experiment`: Dit parameter hoeft niet aangepast te worden, het is puur zodat we deze functie in experiment() kunnen runnen.

   Deze functie returnt niks.

## functies

- `access_data.py`:     Leest de csv met info voor de grid
- `experiment.py`:      Functie die een aantal experimenten runt om een kostenverdeling csv te produceren
- `visualize_cost.py`:  Functie die de kosten visualiseert van een aantal experimenten gebruikmakend van de csv van experiment.py
- `run_all.py`: Met deze functie kies je makkelijk een algoritme om te runnen en of je het grid wil plotten


De volgende functie die kan aangeroepen worden is de experiment functie. Zie hiervoor het experiment kopje.

#### `experiment.py`
``` python
    experiments(10, Greedy_Random_kmeans, 1, 'results.csv')
```
De experiment() functie wordt aangeroepen in de main en krijgt de volgende parameters meegegeven:
- `iteraties`: Deze kun je zelf bepalen door het getal aan te passen als je de experiment functie aanroept
- `algoritme`: Keuze uit de drie algoritmen: Greedy_Random, Greedy_Random_kmeans, en Hill_Climber
- `file_name`: Welke naam je het bestand wilt geven, in de vorm van een string.

De output van experiments is een csv file, `results.csv` met kosten voor elk grid. Deze csv wordt gebruikt als input voor `visualise_cost.py`

#### `visualize_cost.py` 
``` python
visualize_cost('results.csv', 'figures/district_3_kmeans.png')
```
De `visualize_cost.py` functie wordt gebruikt voor het visualiseren van de kostenspreiding van meerdere grids met hetzelfde algoritme. De input parameters zijn:
- `results.csv`: Een csv, de output van experiments
- `pathname.png`: Een png, deze wordt opgeslagen in het pad dat je aangeeft. Wij slaan alles op in `figures`. Dit moet je zelf specificeren


#### `run_all.py`
``` python
run_algorithm(Hill_Climber, 1, visualize=True)
```


## Classes
In classes staan alle classes en algoritmen.

De eenvoudige classes zijn:
- `House`: Krijgt `pos_x`, `pos_y`, `capacity` mee
- `Battery`: Krijgt `pos_x`, `pos_y`, `capacity` mee en heeft ook een `used_capacity` die op 0 staat aan het begin.
- `Cables`: Kan een lijst aan coordinaten opslaan. Dit is een kabel
- `Grid`: Grid simuleert een heel aangelegd grid van kabel batterijen en huizen. Deze grid wordt gebruikt voor ons `greedy_random` algoritme
- `Grid_k_means`: Een aangepaste grid voor het algoritme `greedy_random_k_means`. Hij inherit grid en voegt een fucntie toe die een numpy array maakt van de huiscoordinaten.

### Algoritmen:
#### `greedy_random`: 
Dit constructieve algoritme neemt een grid en legt een kabel in random stappen neer. Het berekend eerst welke batterij de kleinste Manhattan distance heeft van de huizen. Deze huizen worden met die huizen verbonden zo lang de capaciteit van de batterij niet oeverschreden wordt. Omdat de huizen niet met random batterijen verbonden worden maar met de dihtstbijzijnde batterij met voldoende capaciteit is het greedy. De stappen die de kabel legt zijn elke stap random in de x of de y richting totdat de batterij bereikt is.

#### `greedy_random_k_means`: 
Dit constructieve algoritme neemt een grid en legt een kabel in random stappen neer. In dit algoritme moeten de locaties van de batterij nog gekozen worden. Hiervoor gebruiken we een heuristiek. Deze gaat er van uit dat huizen die dicht bij elkaar liggen zo veel mogelijk aan dezelfde batterij verbonden worden om kabelkosten per segment te besparen. De huizen worden door K-Means in clusters opgedeeld die volgens de euclidische afstand het dichtst bij elkaar liggen. De batterijen liggen nu midden in deze clusters. Hierna wordt greedy_random gebruikt om de batterijen met de kortste Manhatten_distance van de huizen aan deze huizen te verbinden met kabels.

Kmeans zal warnings geven. Om ze te verwijderen type je in je terminal:
``` python
OMP_NUM_THREADS=1 
```
Doe dit voordat je `main.py` functie aanroept


#### `hill_climber`: 
Dit iteratieve algoritme krijgt als input een grid en probeert de kosten te verlagen van dit grid. Het doet een aantal iteraties. Bij elke iteratie pakt het een random kabel en legt deze opnieuw aan. Als dit leid tot kostenverlaging wordt de oude kabel vervangen met deze betere kabel.



