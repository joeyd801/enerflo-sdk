class LoanProductsClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: https://docs.enerflo.io/reference/get-details-about-all-loan-products
    def get_all(self, params=None):
        return self.api_client.get('api/v3/loan-products', params)
