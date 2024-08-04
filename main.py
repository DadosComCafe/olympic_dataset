import requests
from bs4 import BeautifulSoup

site = "https://www.olympedia.org/sports"
response = requests.get(site)

soup = BeautifulSoup(response.text, "html.parser")

my_table = soup.find("table", attrs={"class": "table table-striped sortable"})

for row in my_table.find_all("tr"):
    col = row.find_all("td")
    if col:
        sigla = str(col[0]).replace("<td>", "").replace("</td>", "")
        
        esporte = str(col[1]).replace(f"""<td><a href="/sports/{sigla}">""", "").replace("</a></td>", "")

        estacao = str(col[3]).replace("<td>", "").replace("</td>", "")
        print(f"Sigla: {sigla}", f"Esporte: {esporte}", f"Estação: {estacao}")