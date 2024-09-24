from Scrappers.scrapped_country import SrappedCountry
from Scrappers.scrapped_sports import ScrappedSport
from Scrappers.utils import get_request
from pymongo import MongoClient


if __name__ == "__main__":
    site_countries = "https://www.olympedia.org/countries"
    countries_content = get_request(url=site_countries)
    country_obj = SrappedCountry(html_content=countries_content)
    list_countries = country_obj.list_content()

    site_sports = "https://www.olympedia.org/sports"
    sports_content = get_request(url=site_sports)
    sport_obj = ScrappedSport(html_content=sports_content)
    list_sports = sport_obj.list_content()
    myclient = MongoClient('mongodb://mongo:senha@localhost:27017/')
    
    mydb = myclient["olympic_dataset"]
    mycollection = mydb["sports"]
    for content in list_sports:
        try:
            mycollection.insert_one(content)
        except Exception as e:
            print(f"Erro na inserção do esporte: {content['esporte']}")
            print(f"Erro: {e}")
    print("Todos esportes inseridos corretamente!")

    mydb = myclient["olympic_dataset"]
    mycollection = mydb["countries"]
    for content in list_countries:
        try:
            mycollection.insert_one(content)
        except Exception as e:
            print(f"Erro na inserção do país: {content['pais']}")
            print(f"Erro {e}")
    print("Todos os países foram inseridos com sucesso!")
    myclient.close()