class UsersClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: https://docs.enerflo.io/reference/get-all-users
    def get_all(self, company_id=Sentinel(), user_role=Sentinel(), page_size=Sentinel(), page=Sentinel(), params={}):
        default_params = {'company_id':company_id, 'user_role':user_role, 'pageSize':page_size, 'page':page}
        default_params = {key:val for key,val in default_params.items() if val!='<Sentinel_val>'}
        params = {**default_params, params}
        return self.api_client.get('api/v3/users', params)
    
    # Reference: https://docs.enerflo.io/reference/get-user-info
    def get_details(self, user_id, params=None):
        user_details_endpoint = f'api/v3/users/{user_id}'
        return self.api_client.get(user_details_endpoint, params)
