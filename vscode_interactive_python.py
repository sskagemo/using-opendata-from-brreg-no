# In addition to full Jupyter Notebook support, VS Code offers a "hybrid" where you can write ordinary
# Python code (*.py) instead of the Notebook-format (*.ipynb), but still have the possibility to run
# individual cells in a Notebook-like way. The funcitionality requires the Jupyter package.
# For more information, see: https://code.visualstudio.com/docs/python/jupyter-support-py 
# %%
import pandas
import requests
# %%
# Formulating a search on Nace-code:
query_parametre = { 'naeringskode': ['91']}
# %%
# Downloading the search-result as xlsx
url = 'https://data.brreg.no/enhetsregisteret/api/enheter/lastned/regneark'
headers = {'Accept': 'application/vnd.brreg.enhetsregisteret.enhet+vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8'}
session = requests.Session() # establish a session that is kept open during the transfer, instead of performing separate requests
r = session.get(url, headers=headers, params=query_parametre, stream = True)
r.raise_for_status()
with open('er_nace91.xlsx','wb') as f:
    for chunk in r.iter_content(1024*1024*10): # approx 10 MB in each chunck
        f.write(chunk)
# %%
df = pandas.read_excel('enheter_sokeresultat.xlsx')
# %%
# The search-result returns a maximum of 10.000 organisations. If the number of rows 10.000 you have hit the limit.
df.info()
# %%
df['Siste innsendte årsregnskap'].describe()
# %%
