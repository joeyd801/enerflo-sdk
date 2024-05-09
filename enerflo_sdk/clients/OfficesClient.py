class OfficesClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: https://docs.enerflo.io/reference/get-details-about-all-offices
    def get_all(self, params=None):
        return self.api_client.get(f'api/v3/offices', params)

    # Reference: https://docs.enerflo.io/reference/get-details-about-an-office
    def get_details(self, office_id, params=None):
        office_endpoint = f'api/v3/offices/{office_id}'
        return self.api_client.get(office_endpoint, params)
