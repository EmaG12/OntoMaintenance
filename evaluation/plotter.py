import matplotlib.pyplot as plt
import numpy as np
import os

def save_results_plot(rf_acc, kb_acc, filename="confronto_accuratezza.png"):
    """
    Crea un grafico a barre che confronta i due modelli e lo salva in evaluation/
    """
    means = [np.mean(rf_acc), np.mean(kb_acc)]
    stds = [np.std(rf_acc), np.std(kb_acc)]
    labels = ['Random Forest\n(Solo Dati)', 'Onto-Bayes\n(Ibrido)']
    
    x_pos = np.arange(len(labels))
    fig, ax = plt.subplots()
    
   
    ax.bar(x_pos, means, yerr=stds, align='center', alpha=0.7, ecolor='black', capsize=10, color=['gray', 'green'])
    
    ax.set_ylabel('Accuratezza')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    ax.set_title('Confronto Prestazioni Modelli')
    ax.yaxis.grid(True)

    save_path = os.path.join("evaluation", filename)
    plt.savefig(save_path)
    plt.close()
    
    print(f"[EVAL] Grafico salvato in: {save_path}")