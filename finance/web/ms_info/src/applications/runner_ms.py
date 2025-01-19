from finance.web.ms_info.src.infrastructure.entry_points.route_rest import init_app
from finance.web.ms_info.src.infrastructure.driven_adapters.channels.branch_info import Branches
from finance.web.ms_info.src.infrastructure.driven_adapters.channels.localization import CityCoordinates

#test
#from finance.web.ms_suggestion.src.infrastructure.entry_points.route_rest_ms_suggestion import init_app_suggestion

def runner_ms_info():
     branch = Branches()
     city = CityCoordinates()
     return init_app(branch, city )


if __name__ == "__main__":
     runner_ms_info()
     #init_app_suggestion()

