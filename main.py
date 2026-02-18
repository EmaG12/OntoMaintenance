import os
import numpy as np
from kb.ontology_manager import create_ontology
from simulation.data_generator import generate_synthetic_data
from evaluation.experiments import run_cross_validation
from evaluation.plotter import save_results_plot

def main():
    print("=== AVVIO PROGETTO ONTO-MAINTENANCE ===")
    
    if not os.path.exists("kb"): os.makedirs("kb")
    if not os.path.exists("evaluation"): os.makedirs("evaluation")
    ontology_path = os.path.join("kb", "plant_topology.owl")

    print("\n--- FASE 1: Generazione Knowledge Base ---")
    create_ontology()
    
    print("\n--- FASE 2: Simulazione Dati ---")
    data = generate_synthetic_data(num_samples=50)

    print("\n--- FASE 3: Valutazione Sperimentale ---")
    rf_scores, kb_scores = run_cross_validation(data, ontology_path)

    print("\n=== RISULTATI FINALI (Accuracy Media) ===")
    print(f"Random Forest: {np.mean(rf_scores):.3f} (+/- {np.std(rf_scores):.3f})")
    print(f"Onto-Bayes   : {np.mean(kb_scores):.3f} (+/- {np.std(kb_scores):.3f})")
    
    save_results_plot(rf_scores, kb_scores)

if __name__ == "__main__":
    main()