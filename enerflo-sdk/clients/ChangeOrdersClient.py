class ChangeOrdersClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: Not in documentation
    def get_all(self, params=None):
        return self.api_client.get('api/v3/change-orders', params)

    # Reference: https://docs.enerflo.io/reference/get-details-about-a-change-order
    def get_details(self, change_order_id, params=None):
        single_change_order_endpoint = f'api/v3/change-orders/{change_order_id}'
        return self.api_client.get(single_change_order_endpoint, params)
