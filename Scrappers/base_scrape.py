from bs4 import BeautifulSoup


class BaseScrape:
    
    def __init__(self, html_content:bytes) -> None:
        self.html_content = html_content
        self.soup = self.parse_html()
        self.table = self.soup.find("table", attrs={"class": "table table-striped sortable"})
        self.tr = self.table.find_all("tr")

    
    def parse_html(self) -> BeautifulSoup:
        return BeautifulSoup(self.html_content, "html.parser")
    

    def list_content(self) -> list[dict]:
        raise NotImplementedError("Método não implementado!")