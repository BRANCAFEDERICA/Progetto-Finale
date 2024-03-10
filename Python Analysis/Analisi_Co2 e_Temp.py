import pandas as pd

# Carico il dataset delle temperature
df_temperature = pd.read_csv(r'C:\Users\fedeb\OneDrive\Desktop\Python\1_BW Finale\Annual_Mean_Global_Surface_Temperature_.csv', sep = ';')

# Creo una mappatura tra i codici ISO3 e il codice ISO3 unificato per la Cina (CHN)
china_iso3_mapping = {'HKG': 'CHN', 'MAC': 'CHN', 'CHN': 'CHN'}

# Sostituisco i codici ISO3 nel dataset delle temperature con il codice ISO3 unificato per la Cina
df_temperature['ISO3'] = df_temperature['ISO3'].replace(china_iso3_mapping)


# Verifico che l'operazione sia avvenuta correttamente
# print(df_temperature[df_temperature['Country'] == 'China'].head())

# Ora procedo con il merge tra il dataset delle temperature e il dataset sulla CO2

# Carico il dataset sulla CO2, selezionando solo le colonne desiderate e gli anni dal 1961 al 2022
columns_to_keep = ['country', 'year', 'ISO3', 'population', 'gdp', 'co2', 'co2_per_capita', 'co2_per_gdp', 'cumulative_co2']
df_co2 = pd.read_csv(r'C:\Users\fedeb\OneDrive\Desktop\Python\1_BW Finale\TOPOco2mondo_filtered_y.csv', usecols=columns_to_keep, sep = ';')

# Effettuo il merge dei due dataset basato sul codice ISO3
df_merged = pd.merge(df_co2, df_temperature, on=['year', 'ISO3'], how='inner')
print(df_merged.head())

# Salvo il nuovo dataset combinato
df_merged.to_csv("temperature_co2_merged.csv", index=False)
