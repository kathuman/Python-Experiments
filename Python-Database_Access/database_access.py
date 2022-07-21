import pyodbc
import pandas as pd

conn = pyodbc.connect('DRIVER= {PatoBI-FA};'
			'HOST = RGHPATSYSDBP001;'
                        'DATABASE=patobi;' 
                        'UID=CPHOPT;'
                        'PWD=cph16opt;'
			'port=26076')

df = pd.read_sql_query("SELECT Rekvnr, Modtdat, Modtklk, Team, Kategori, Prioritet, Svinddat,Svindklk, Godkdat, Godkklk, GodkINI, Fsvuddat, Fsvudklk, UndersogINI,Antalblokke, Antalglas, Antalmat FROM PATOBI.PUB.AktivRekv",conn)

print(df.head(n=5))