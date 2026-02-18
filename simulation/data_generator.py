import pandas as pd
import numpy as np
import random

def generate_synthetic_data(num_samples=1000):
    data = []
    print(f"[SIM] Generazione di {num_samples} campioni sintetici...")
    
    for _ in range(num_samples):
        sample = {}
        
        pump_fail = random.random() < 0.05
        sample['Pump_Fail'] = 1 if pump_fail else 0
        
        prob_pipe_issue = 0.9 if pump_fail else 0.01
        pipe_fail = random.random() < prob_pipe_issue
        sample['Pipe_Pressure_Low'] = 1 if pipe_fail else 0
        
        prob_tank_empty = 0.95 if pipe_fail else 0.05
        tank_fail = random.random() < prob_tank_empty
        sample['Tank_Level_Low'] = 1 if tank_fail else 0
        
        data.append(sample)
        
    return pd.DataFrame(data)