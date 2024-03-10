import pandas as pd 

csv = pd.read_csv(r'C:\Users\fedeb\OneDrive\Desktop\Python\1_BW Finale\Indicator_3_1_Climate_Indicators_Annual_Mean_Global_Surface_Temperature_577579683071085080.csv')
print(csv.columns)
anni = ['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', 
        '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978',
        '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
        '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', 
        '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', 
        '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', 
        '2015', '2016', '2017', '2018', '2019','2020','2021','2022']
# print(anni)

years = pd.DataFrame()

for y in anni:
    df = pd.DataFrame()
    df["Country"] = csv["Country"].replace(",","",regex=True)
    df["ISO3"] = csv['ISO3']
    df["Value"]= csv[y]
    df["Year"] = y
    years = pd.concat([years,df], ignore_index=True)
print(years)

years.to_csv("Annual_Global_Surface_Temperature_.csv",index=False, encoding='utf-8')