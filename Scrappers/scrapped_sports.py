from Scrappers.base_scrape import BaseScrape


class ScrappedSport(BaseScrape):
    
    def list_content(self) -> list[dict]:
        self.my_list = []
        for row in self.table.find_all("tr"):
            col = row.find_all("td")
            if col:
                sigla = str(col[0]).replace("<td>", "").replace("</td>", "")
                esporte = str(col[1]).replace(f"""<td><a href="/sports/{sigla}">""", "").replace("</a></td>", "")
                estacao = str(col[3]).replace("<td>", "").replace("</td>", "")
                self.my_list.append({"sigla": sigla, "esporte": esporte, "estação": estacao})
        return self.my_list


if __name__ == "__main__":
    from utils import get_request
    #import ipdb
    #ipdb.set_trace()
    site = "https://www.olympedia.org/sports"
    html_content = get_request(site)
    scrapped_sport_obj = ScrappedSport(html_content=html_content)
    print(f"List Content: {scrapped_sport_obj.list_content()}")