import os
from owlready2 import *

def create_ontology():
    onto_path = os.path.join("kb", "plant_topology.owl")
    
    onto = get_ontology("http://test.org/plant.owl")

    with onto:
        class Component(Thing): pass
        class Sensor(Thing): pass
        
        class connectedTo(Component >> Component): 
            transitive = True 
        
        class hasSensor(Component >> Sensor): pass
        
        class status(DataProperty):
            domain = [Component]
            range = [str] 

    pump = Component("Pump_01")
    pipe = Component("Pipe_01")
    tank = Component("Tank_01")
    
    pump.connectedTo.append(pipe)
    pipe.connectedTo.append(tank)
    
    onto.save(file=onto_path)
    print(f"[KB] Ontologia salvata in: {onto_path}")
    return onto

if __name__ == "__main__":
    create_ontology()