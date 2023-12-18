from Simulation.simulation_manager import SimulationManager

strategies_name=["Strategy2","StrategyRecuitSimule"]

Simu=SimulationManager()
Simu.set_blocs()
Simu.set_zones(20, 40)

for strategy_name in strategies_name: 
    Simu.launch_strategy(strategy_name)


Simu.compare_solutions(strategies_name)
print(Simu.metrics)

results=Simu.contexts[strategies_name[1]].modified_data.blocs