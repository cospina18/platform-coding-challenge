from finance.web.ms_info.src.infrastructure.entry_points.route_rest import init_app
from finance.web.ms_info.src.infrastructure.driven_adapters.channels.branch_info import Branches
from finance.web.ms_info.src.infrastructure.driven_adapters.channels.localization import CityCoordinates

def runner_ms_info():
     branch = Branches()
     city = CityCoordinates()
     return init_app(branch, city )


if __name__ == "__main__":
     runner_ms_info()

