# Onto-Maintenance: Diagnostica Ibrida per Impianti Industriali

Il sistema implementa un approccio **Neuro-Simbolico** per la diagnosi di guasti, integrando Ontologie (OWL) e Reti Bayesiane.

## Obiettivo
Confrontare un approccio puramente Data-Driven (Random Forest) con un approccio Knowledge-Based (Onto-Bayes) nella diagnosi di guasti, specialmente in contesti dove la struttura causale è nota ma i dati possono essere rumorosi.

## Struttura del Progetto
* `kb/`: Contiene l'Ontologia (T-Box) generata via codice e salvata in formato OWL.
* `models/`: Implementazione dei classificatori (Random Forest vs Bayesian Network).
* `simulation/`: Generatore di dati sintetici basato sulla logica dell'ontologia.
* `evaluation/`: Script per la Cross-Validation e la generazione dei grafici.

## Requisiti
* Python 3.8+
* Librerie: `owlready2`, `pgmpy`, `scikit-learn`, `pandas`, `matplotlib`

Installazione:
```bash
pip install -r requirements.txt

PS:Al termine di ogni esecuzione verrà generato un grafico nella cartella "evaluation"
