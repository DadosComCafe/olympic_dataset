from bs4 import BeautifulSoup
from utils import get_request


class ScrappedSport:
    def __init__(self, html_content) -> None:
        self.html_content = html_content
        self.soup = self.parse_html()
        self.my_table = self.soup.find("table", attrs={
            "class": "table table-striped sortable"}
        )


    def parse_html(self) -> BeautifulSoup:
        return BeautifulSoup(self.html_content, "html.parser")
    
    def list_content(self) -> list[dict]:
        self.my_list = []
        for row in self.my_table.find_all("tr"):
            col = row.find_all("td")
            if col:
                sigla = str(col[0]).replace("<td>", "").replace("</td>", "")
                esporte = str(col[1]).replace(f"""<td><a href="/sports/{sigla}">""", "").replace("</a></td>", "")
                estacao = str(col[3]).replace("<td>", "").replace("</td>", "")
                print(f"Sigla: {sigla}", f"Esporte: {esporte}", f"Estação: {estacao}")
                self.my_list.append({"sigla": sigla, "esporte": esporte, "estação": estacao})


if __name__ == "__main__":
    import ipdb
    ipdb.set_trace()
    site = "https://www.olympedia.org/sports"
    html_content = get_request(site)
    scrapped_sport_obj = ScrappedSport(html_content=html_content)
    print(f"List Content: {scrapped_sport_obj.list_content()}")