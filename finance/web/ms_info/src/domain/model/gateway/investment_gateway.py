from abc import ABCMeta, abstractmethod

class InvestmentGateway(metaclass=ABCMeta):
    @abstractmethod
    def get_investment_suggestion(self, name, city, age):
        "get_investment_suggestion"