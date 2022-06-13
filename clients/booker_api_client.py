from clients.rest_client import RestClient


class BookerApiClient:
    def __init__(self):
        self.rest_client = RestClient("https://restful-booker.herokuapp.com")

    def get_booking_id_sally_brown(self):
        response = self.get_booking_ids_filtered_by_name("Sally", "Brown")
        return response

    def get_booking_ids(self, headers=None):
        if headers is None:
            headers = {}
        response = self.rest_client.get("/booking", headers)
        return response

    def get_booking_ids_filtered_by_name(self, first_name, last_name):
        response = self.rest_client.get(f"/booking?firstname={first_name}&lastname={last_name}")
        return response

    def get_booking_ids_filtered_by_date(self, checkin, checkout):
        response = self.rest_client.get(f"/booking?checkin={checkin}&checkout={checkout}")
        return response
