class EquipmentClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: https://docs.enerflo.io/reference/get-details-about-all-inverters
    def get_inverters(self, company_id=Sentinel(), active=Sentinel(), params={}):
        default_params = {'company_id':company_id, 'active':active}
        default_params = {key:val for key,val in default_params.items() if val!='<Sentinel_val>'}
        params = {**default_params, **params}
        return self.api_client.get('epc/equipment/inverters', params)

    # Reference: https://docs.enerflo.io/reference/get-details-about-all-panels
    def get_panels(self, company_id=Sentinel(), active=Sentinel(), params={}):
        default_params = {'company_id':company_id, 'active':active}
        default_params = {key:val for key,val in default_params.items() if val!='<Sentinel_val>'}
        params = {**default_params, **params}
        return self.api_client.get('epc/equipment/panels', params)
