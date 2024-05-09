class InstallsClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: https://docs.enerflo.io/reference/get-a-list-of-installs
    def get_all(self, per_page=25, page=1, sort_by=Sentinel(), filter_logic=Sentinel(), filter_filters_field=Sentinel(), 
                filter_filters_operator=Sentinel(), filter_filters_value=Sentinel(), report_id=Sentinel(), params={}):
        default_params = {'per_page':per_page, 'page':page, 'sort_by':sort_by, 'filter[logic]':filter_logic, 
                          'filter[filters][0][field]':filter_filters_field, 'filter[filters][0][operator]':filter_filters_operator,
                          'filter[filters][0][value]':filter_filters_value, 'report_id':report_id}
        default_params = {key:val for key,val in default_params.items() if val!='<Sentinel_val>'}
        params = {**default_params, **params}
        return self.api_client.get(f'api/v3/installs', params)

    # Reference: https://docs.enerflo.io/reference/v3installsid
    def get_details(self, install_id, params=None):
        install_endpoint = f'api/v3/installs/{install_id}'
        return self.api_client.get(install_endpoint, params)

    # Reference: https://docs.enerflo.io/reference/get-all-install-statuses
    def get_install_statuses(self, company_id=Sentinel(), params=None):
        default_params = {'company_id':company_id}
        default_params = {key:val for key,val in default_params.items() if val!='<Sentinel_val>'}
        params = {**default_params, **params}
        return self.api_client.get(f'api/v3/install-statuses', params)
