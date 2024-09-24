from Scrappers.base_scrape import BaseScrape


class SrappedCountry(BaseScrape):

    def list_content(self) -> list[dict]:
        self.my_list = []
        for row in self.tr:
            col = row.find_all("td")
            if col:
                sigla = col[0].get_text(strip=True)
                nome_pais = col[1].get_text(strip=True)
                presente_nas_olimpiadas_modernas = True if "glyphicon glyphicon-ok" in str(col[2]) else False  
                self.my_list.append({"sigla": sigla, "pais": nome_pais, "presente": presente_nas_olimpiadas_modernas})
        return self.my_list
    

if __name__ == "__main__":
    from utils import get_request
    #import ipdb
    #ipdb.set_trace()
    site = "https://www.olympedia.org/countries"
    html_content = get_request(site)
    country = SrappedCountry(html_content=html_content)
    print(country.list_content())