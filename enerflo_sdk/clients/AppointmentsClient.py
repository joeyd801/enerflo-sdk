class AppointmentsClient:
    def __init__(self, api_client):
        self.api_client = api_client

    # Reference: https://docs.enerflo.io/reference/get-all-appointments-for-a-customer
    def get_all_for_customer(self, customer_id, params=None):
        all_appointment_endpoint = f'api/v3/customers/{customer_id}/appointments'
        return self.api_client.get(all_appointment_endpoint, params)
    
    # Reference: https://docs.enerflo.io/reference/get-appointment-details
    def get_details(self, customer_id, appointment_id, params=None):
        single_appointment_endpoint = f'api/v3/customers/{customer_id}/appointments/{appointment_id}'
        return self.api_client.get(single_appointment_endpoint, params)
