import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, precision_score
from models.baseline_model import run_baseline
from models.bayesian_reasoner import OntoBayes

def run_cross_validation(data, ontology_file, n_splits=5):
    """
    Esegue la Cross Validation confrontando Random Forest e Onto-Bayes.
    Restituisce i risultati per essere plottati.
    """
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    
    results = {
        'rf': [],
        'kb': []
    }
    
    fold = 1
    for train_idx, test_idx in kf.split(data):
        print(f"[EXPERIMENT] Esecuzione Fold {fold}/{n_splits}...")
        train_data = data.iloc[train_idx]
        test_data = data.iloc[test_idx]
        y_true = test_data['Pump_Fail']
        
        preds_rf = run_baseline(train_data, test_data)
        acc_rf = accuracy_score(y_true, preds_rf)
        results['rf'].append(acc_rf)
        
        kb_system = OntoBayes(ontology_file)
        kb_system.build_structure_from_kb() 
        preds_kb = kb_system.fit_and_predict(train_data, test_data)
        acc_kb = accuracy_score(y_true, preds_kb)
        results['kb'].append(acc_kb)
        
        fold += 1
        
    return results['rf'], results['kb']