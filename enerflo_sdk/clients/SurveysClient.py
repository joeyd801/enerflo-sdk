class SurveysClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: Not in documentation, but is a working endpoint
    def get_all(self, params=None):
        return self.api_client.get('api/v3/surveys', params)

    # Reference: https://docs.enerflo.io/reference/get-deal-info-v3
    def get_details(self, survey_id, params=None):
        return self.api_client.get(f'api/v3/surveys/{survey_id}', params)
