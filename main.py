import matplotlib.pyplot as plt
from pprint import pprint
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.greedy_random_kmeans import Greedy_Random_kmeans
from classes.grid_k_means import Grid_kmeans
from classes.grid import Grid
from classes.greedy_random import Greedy_Random
from functies.access_data import access_data
from functies.experiment import experiments
from functies.visualize_cost import visualize_cost
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from classes.hill_climber import Hill_Climber
from functies.run_all import run_algorithm


if __name__ == "__main__":
    run_algorithm(Hill_Climber, 3, visualize=True, output=True)

    experiments(2, Greedy_Random_kmeans, 3, 'results.csv')
