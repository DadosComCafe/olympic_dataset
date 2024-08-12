import requests
from bs4 import BeautifulSoup
from csv import DictWriter

def get_request(url: str="https://www.olympedia.org/sports") -> str:
    return requests.get(url).text

def parse_html(html_content: str) -> BeautifulSoup:
    return BeautifulSoup(html_content, "html.parser")

def export_to_csv(file_name: str, scrapped_data: dict):
    with open(file_name, "a", encoding="utf-8") as arquivo:
        my_writer = DictWriter(arquivo, fieldnames=scrapped_data.keys())
        #my_writer.writeheader()
        my_writer.writerow(scrapped_data)


if __name__ == "__main__":
    html_content = get_request()
    soup = parse_html(html_content=html_content)
    print(soup)

    my_table = soup.find("table", attrs={"class": "table table-striped sortable"})

    for row in my_table.find_all("tr"):
        col = row.find_all("td")
        if col:
            sigla = str(col[0]).replace("<td>", "").replace("</td>", "")
            esporte = str(col[1]).replace(f"""<td><a href="/sports/{sigla}">""", "").replace("</a></td>", "")
            estacao = str(col[3]).replace("<td>", "").replace("</td>", "")
            print(f"Sigla: {sigla}", f"Esporte: {esporte}", f"Estação: {estacao}")
            dict_content = {"sigla": sigla, "esporte": esporte, "estação": estacao}
            export_to_csv(file_name="esportes.csv", scrapped_data=dict_content)