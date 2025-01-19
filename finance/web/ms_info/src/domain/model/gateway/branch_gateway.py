from abc import ABCMeta, abstractmethod



class BranchGateway(metaclass=ABCMeta):
    @abstractmethod
    def get_bancolombia_branches(self, latitude, longitude) -> str:
        "Deseralizator bancolombia_branches"