import pytest

from bdd_section import then, when, _and
from clients.booker_api_client import BookerApiClient


class TestBooking:

    def setup(self):
        self.client = BookerApiClient()

    def test_return_stat_code_200(self):
        when('get booking ids')
        response = self.client.get_booking_ids()
        then('status code is 200')
        assert response.status_code == 200

    def test_return_ids(self):
        when('get booking ids')
        response = self.client.get_booking_ids()
        then('return ids')
        assert len(response.json()) > 0

    def test_selected_name_return_ids(self):
        when('get booking ids Sally Brown')
        response = self.client.get_booking_ids_filtered_by_name("Sally", "Brown")
        then('status code is 200')
        assert response.status_code == 200
        _and('return ids')
        assert len(response.json()) > 0

    def test_selected_name_return_no_ids(self):
        when('get booking ids James Bond')
        response = self.client.get_booking_ids_filtered_by_name("James", "Bond")
        then('status code is 200')
        assert response.status_code == 200
        _and('return empty list')
        assert len(response.json()) == 0

    def test_selected_date_return_ids(self):
        when('get booking ids for selected dates 2006-05-13", "2021-05-21')
        response = self.client.get_booking_ids_filtered_by_date("2006-05-13", "2021-05-21")
        then('status code is 200')
        assert response.status_code == 200
        _and('return ids')
        assert len(response.json()) > 0

    @pytest.mark.parametrize("header", ["application/xml",
                                        "text/xml"])
    def test_not_acceptable_response(self, header):
        headers = {'Accept': header}
        when('get booking ids with modified headers')
        response = self.client.get_booking_ids(headers)
        then('status code is 406')
        assert response.status_code == 406
