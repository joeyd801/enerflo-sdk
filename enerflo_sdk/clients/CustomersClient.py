class CustomersClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: https://docs.enerflo.io/reference/get-all-customers
    def get_all(self, search=Sentinel(), params={}):
        default_params = {'search':search}
        default_params = {key:val for key,val in default_params.items() if val!='<Sentinel_val>'}
        params = {**default_params, **params}
        return self.api_client.get('api/v1/customers', params)

    # Reference: https://docs.enerflo.io/reference/v3customersid
    def get_single_customer(self, customer_id, params=None):
        id_endpoint = f'api/v3/customers/{customer_id}'
        return self.api_client.get(id_endpoint, params)
