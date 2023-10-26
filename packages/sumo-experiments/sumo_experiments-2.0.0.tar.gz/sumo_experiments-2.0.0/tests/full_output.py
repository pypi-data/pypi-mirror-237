import sys

from src.sumo_experiments import Experiment
from src.sumo_experiments.preset_networks import *
from src.sumo_experiments.traci_util import *
import time
import matplotlib.pyplot as plt

t = time.time()

net = SquareNetwork()

exp = Experiment(
    name = 'test_output',
    infrastructures = net.generate_random_infrastructures,
    flows = net.generate_flows_all_directions,
    detectors = net.generate_boolean_detectors
)

exp.set_parameter('lane_length', 100)
exp.set_parameter('yellow_time', 3)
exp.set_parameter('max_speed', 30)
exp.set_parameter('simulation_duration', 1500)
exp.set_parameter('stop_generation_time', 1000)
exp.set_parameter('flow_frequency', 100)
exp.set_parameter('square_side_length', 3)
exp.set_parameter('min_duration_tl', 15)
exp.set_parameter('max_duration_tl', 60)
exp.set_parameter('vehicle_threshold', 6)
exp.set_parameter('boolean_detector_length', 10)
exp.set_parameter('distribution', 'binomial')
exp.set_parameter('minimum_edge_length', 100)
exp.set_parameter('maximum_edge_length', 500)

period_time = 2000
load_vector = np.array([1500, 1500, 750])
coeff_matrix = np.array([
    # First entry
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    # Second entry
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    # Third entry
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    # East entry
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    # Fourth entry
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    # Fifth entry
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    # Sixth entry
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    [1/56, 1/42, 0.0001],
    # West entry
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
    [1/56, 10**-10, 1/14],
])

exp.set_parameter('period_time', period_time)
exp.set_parameter('load_vector', load_vector)
exp.set_parameter('coeff_matrix', coeff_matrix)
exp.set_parameter('simulation_duration', len(load_vector) * period_time)

wrapper = TraciWrapper()
wrapper.add_stats_function(get_speed_data)
wrapper.add_stats_function(get_acceleration_data)
wrapper.add_stats_function(get_nb_vehicles)
wrapper.add_behavioural_function(net.boolean_detection)

data = exp.run_traci(wrapper.final_function, no_warnings=True, gui=True)

exp.clean_files(except_trip_info=True, except_emission=True)

print(time.time() - t)

print(data)