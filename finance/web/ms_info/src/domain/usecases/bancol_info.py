from finance.web.ms_info.src.domain.model.gateway.city_gateway import CityGateway
from finance.web.ms_info.src.domain.model.gateway.branch_gateway import BranchGateway

class InfoBancol:
    def __init__(self, branch: BranchGateway, city: CityGateway ):
        self.city = city
        self.branch = branch

        
    def local(self, city_name):
        country_code = "CO"  # Código de país para Colombia
        latitude, longitude = self.city.get_city_coordinates(city_name, country_code)
        return self.branch.get_bancolombia_branches(latitude, longitude)



    