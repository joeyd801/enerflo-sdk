class ProductsClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: https://docs.enerflo.io/reference/get-products
    def get_all(self, company_id=Sentinel(), active=Sentinel(), is_battery=Sentinel(), params={}):
        default_params = {'company_id':company_id, 'active':active, 'is_battery':is_battery}
        default_params = {key:val for key,val in default_params.items() if val!='<Sentinel_val>'}
        params = {**default_params, **params}
        return self.api_client.get('api/v3/company/products', params)
