class TasksClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: https://docs.enerflo.io/reference/get-v3-tasks-all
    def get_all(self, order_by=Sentinel(), order_dir=Sentinel(), page_size=25, page=Sentinel(), filter_logic=Sentinel(),
                filter_field=Sentinel(), filter_operator=Sentinel(), filter_value=Sentinel(), params={}):
        default_params = {'orderBy':order_by, 'orderDir':order_dir, 'pageSize':page_size, 'page':page, 'filter[logic]':filter_logic,
                          'filter[filters][0][field]':filter_field, 'filter[filters][0][operator]':filter_operator,
                          'filter[filters][0][value]':filter_value}
        default_params = {key:val for key,val in default_params.items() if val!='<Sentinel_val>'}
        params = {**default_params, params}
        return self.api_client.get('api/v1/tasks/all', params)

    # Reference: https://docs.enerflo.io/reference/retrieve-a-list-of-tasks
    def get_all_for_customer(self, customer_id, params=None):
        customer_task_endpoint = f'api/v1/tasks/{customer_id}'
        return self.api_client.get(customer_task_endpoint, params)
