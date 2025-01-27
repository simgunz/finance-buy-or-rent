# COPILOT INSTRUCTIONS
# - Help me write clean, documented Python code
# - Suggest relevant Python libraries when needed
# - Help with proper data structures and variable naming
# - Suggest error handling and edge cases
# - Help with numerical accuracy in financial calculations
# - Suggest visualization approaches when needed
# - Help writing clear docstrings and comments
# - Point out potential bugs or logical errors
# - Suggest performance improvements when relevant
#
# I will develop the solution step by step in this notebook,
# asking for specific help when needed.

# PROBLEM STATEMENT

SCENARIO AFFITTO:
1. Spese una tantum:
   - Cauzione (tipicamente 3 mensilità)
   - Eventuali spese di agenzia (solitamente 1 mensilità)

2. Spese ricorrenti mensili:
   - Canone d'affitto
   - Spese condominiali (ordinarie)
   - Utenze (acqua, luce, gas, internet)
   - Piccola manutenzione ordinaria
   - TARI (tassa rifiuti)

SCENARIO ACQUISTO:
1. Spese iniziali una tantum:
   - Anticipo mutuo (tipicamente 20% del valore casa)
   - Spese notarili (circa 2-3% del valore casa)
   - Imposta di registro (2% per prima casa)
   - IVA se applicabile (4% per prima casa da costruttore)
   - Spese di istruttoria mutuo
   - Eventuali spese di agenzia (2-3% del valore casa)
   - Perizia tecnica
   - Assicurazione obbligatoria incendio/scoppio

2. Spese ricorrenti mensili:
   - Rata mutuo (capitale + interessi)
   - Spese condominiali (ordinarie)
   - Utenze (acqua, luce, gas, internet)
   - TARI (tassa rifiuti)

3. Spese ricorrenti annuali:
   - IMU (se applicabile, esente prima casa tranne categorie A/1, A/8, A/9)
   - Manutenzione ordinaria (circa 1-1.5% del valore casa/anno)
   - Assicurazione casa (facoltativa ma consigliata)

4. Spese straordinarie (da modellare come accantonamento annuale):
   - Manutenzione straordinaria (ristrutturazioni, impianti)
   - Spese condominiali straordinarie

CONSIDERAZIONI AGGIUNTIVE:
1. Detrazioni fiscali:
   - Detrazione interessi mutuo prima casa (19% fino a 4.000€/anno)
   - Eventuali detrazioni per ristrutturazioni/efficientamento energetico

2. Evoluzione temporale:
   - Rivalutazione del canone d'affitto (ISTAT)
   - Rivalutazione del valore immobiliare
   - Evoluzione dei tassi di interesse (per mutui variabili)

3. Costo opportunità:
   - Rendimento del capitale non immobilizzato nell'acquisto
   - Rendimento del risparmio mensile differenziale

Ti sembra ora sufficientemente dettagliata la formulazione? Possiamo procedere con la definizione della struttura del codice per la simulazione.
