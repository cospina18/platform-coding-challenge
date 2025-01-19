from finance.web.ms_info.src.domain.model.gateway.city_gateway import CityGateway
from finance.web.ms_info.src.domain.model.gateway.branch_gateway import BranchGateway

class InfoBancol:
    def __init__(self, branch: BranchGateway, city: CityGateway ):
        self.city = city
        self.branch = branch
        # Ejemplo de uso
        city_name = "Rionegro"
        country_code = "CO"  # Código de país para Colombia

        latitude, longitude = self.city.get_city_coordinates(branch)

        branches_data = self.branch.get_bancolombia_branches(latitude, longitude)
        print(branches_data)

        #branch_info = extract_branch_info(branches_data)



    def extract_branch_info(data):
        if 'data' in data and 'channels' in data['data']:
            branches = data['data']['channels']
            branch_info = []
            
            for branch in branches:
                info = {
                    'channelName': branch.get('channelName'),
                    'address': branch.get('address'),
                    'schedules': branch.get('schedules')
                }
                branch_info.append(info)
            
            return branch_info
        else:
            return 'Oficina no encontrada cerca.'



    