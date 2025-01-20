from finance.web.ms_info.src.domain.model.gateway.city_gateway import CityGateway
from finance.web.ms_info.src.domain.model.gateway.branch_gateway import BranchGateway
from finance.web.ms_info.src.domain.model.gateway.investment_gateway import InvestmentGateway

class InfoBancol:
    def __init__(self, branch: BranchGateway, city: CityGateway, investment: InvestmentGateway ):
        self.city = city
        self.branch = branch
        self.investment = investment

        
    def local(self,name, age, city_name):
        country_code = "CO"  # Código de país para Colombia
        latitude, longitude = self.city.get_city_coordinates(city_name, country_code)
        #investment = self.investment.get_investment_suggestion(name, city_name, age)
        branch = self.branch.get_bancolombia_branches(latitude, longitude)
        return branch



    