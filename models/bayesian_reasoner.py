from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from owlready2 import *
import os

class OntoBayes:
    def __init__(self, ontology_path):
       
        self.onto = get_ontology(ontology_path).load()
        self.model = DiscreteBayesianNetwork()
        
    def build_structure_from_kb(self):
        print("[KBS] Costruzione Rete Bayesiana dall'Ontologia...")
        mappings = {
            "Pump_01": "Pump_Fail",
            "Pipe_01": "Pipe_Pressure_Low",
            "Tank_01": "Tank_Level_Low"
        }
        
        for comp in self.onto.Component.instances():
            for target in comp.connectedTo:
                source_node = mappings.get(comp.name)
                target_node = mappings.get(target.name)
                
                if source_node and target_node:
                    self.model.add_edge(source_node, target_node)
                    # print(f"      -> Arco aggiunto: {source_node} -> {target_node}")

    def fit_and_predict(self, train_data, test_data):

        state_names = {
            'Pump_Fail': [0, 1],
            'Pipe_Pressure_Low': [0, 1],
            'Tank_Level_Low': [0, 1]
        }

        
        self.model.fit(train_data, estimator=MaximumLikelihoodEstimator, state_names=state_names)
        
        
        features = ['Pipe_Pressure_Low', 'Tank_Level_Low']
        target = 'Pump_Fail'
        
        inference_data = test_data[features]
        
        predictions = self.model.predict(inference_data)
        
        return predictions[target].values