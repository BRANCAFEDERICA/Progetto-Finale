import pandas as pd

# Carica il dataset
file_path = r"C:\Users\fedeb\OneDrive\Desktop\Python\1_BW Finale\Climate Anxiety-3.xlsx"
df = pd.read_excel(file_path)

# Seleziona solo le colonne desiderate
df_selected = df[['Respondent_Serial', 'language', 'country', 'Q1', 'sad', 'helpless', 'anxious', 'afraid', 'optimistic', 'angry', 'guilty', 'ashamed', 'hurt', 'depressed', 'despair', 'grief', 'powerless', 'indifferent', 'Q3']]

# Rinomina le colonne per renderle più comprensibili
df_selected.columns = ['Respondent_Serial', 'Language', 'Country', 'Q1', 'Sad', 'Helpless', 'Anxious', 'Afraid', 'Optimistic', 'Angry', 'Guilty', 'Ashamed', 'Hurt', 'Depressed', 'Despair', 'Grief', 'Powerless', 'Indifferent', 'Q3']

# Melt il dataframe per avere una riga per ogni combinazione di domanda e risposta
df_melted = df_selected.melt(id_vars=['Respondent_Serial', 'Language', 'Country', 'Q1', 'Q3'], var_name='Emotion', value_name='Response')


