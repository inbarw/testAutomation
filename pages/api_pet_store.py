from pages.api_base import APIBase

class APIPetStore(APIBase):
    def __init__(self, base_url, headers=None):
        super().__init__(base_url, headers)

    def add_new_pet(self, pet_data: dict, headers=None):
        return self.request_api("POST", data=pet_data, headers=headers or self.headers)

    def update_pet_data(self, pet_data: dict, headers=None):
        return self.request_api("PUT", data=pet_data, headers=headers or self.headers)

    def find_pet_by_status(self, endpoint, headers):
        return self.request_api("GET", endpoint, headers=headers)

    def validate_pet_status(self, pets_list, expected_status):
        for pet in pets_list:
            assert pet['status'] == expected_status, f"pet has unexpected status: {pet['status']}"