from enerflo_sdk.APIClient import APIClient
from enerflo_sdk.Sentinel import Sentinel
from .clients import AppointmentsClient, ChangeOrdersClient, CustomersClient, EquipmentClient, InstallsClient, \
    LoanProductsClient, OfficesClient, ProductsClient, SurveysClient, TasksClient, UsersClient, UtilitiesClient


class EnerfloSDK:
    def __init__(self, api_key):
        self.api_client = APIClient('https://enerflo.io', api_key)

        self.appointments = AppointmentsClient(self.api_client)
        self.changeOrders = ChangeOrdersClient(self.api_client)
        self.customers = CustomersClient(self.api_client)
        self.equipment = EquipmentClient(self.api_client)
        self.installs = InstallsClient(self.api_client)
        self.loan_products = LoanProductsClient(self.api_client)
        self.offices = OfficesClient(self.api_client)
        self.products = ProductsClient(self.api_client)
        self.surveys = SurveysClient(self.api_client)
        self.tasks = TasksClient(self.api_client)
        self.users = UsersClient(self.api_client)
        self.utilities = UtilitiesClient(self.api_client)
