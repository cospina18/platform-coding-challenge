from finance.web.ms_info.src.infrastructure.entry_points.route_rest import init_app
from finance.web.ms_info.src.infrastructure.driven_adapters.rest.branch_info_bancol import Branches
from finance.web.ms_info.src.infrastructure.driven_adapters.rest.localization_geocode import CityCoordinates
from finance.web.ms_info.src.infrastructure.driven_adapters.rest.suggestion_ms import Investment

#test
#from finance.web.ms_suggestion.src.infrastructure.entry_points.route_rest_ms_suggestion import init_app_suggestion

def runner_ms_info():
     branch = Branches()
     city = CityCoordinates()
     investment = Investment()
     return init_app(branch, city, investment)


if __name__ == "__main__":
     runner_ms_info()
     #init_app_suggestion()

