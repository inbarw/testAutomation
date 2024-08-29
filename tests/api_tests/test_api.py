from config.config_api import Config
from pages.api_pet_store import APIPetStore
from utils.pet_data import set_pet_data

def test_create_new_pet():
    api_pet_store = APIPetStore(Config.BASE_URL, Config.HEADERS)
    pet_data = set_pet_data(123, 1, "Dogs", "Buddy", "https://example.com/photo1.jpg", 1, "friendly",  "available")
    api_pet_store.add_new_pet(pet_data)
    updated_pet_data = set_pet_data(123, 1, "Dogs", "Buddy", "https://example.com/photo1.jpg", 1, "friendly",  "sold")
    api_pet_store.update_pet_data(updated_pet_data)

def test_find_pet_by_status():
  api_pet_store = APIPetStore(Config.BASE_URL, Config.HEADERS)
  pets_status = api_pet_store.find_pet_by_status(endpoint="findByStatus?status=available", headers={'Accept': 'application/json'})
  assert pets_status[4]["name"] == "fish"
  print(pets_status[4])

def test_find_pet_by_status_2():
  api_pet_store = APIPetStore(Config.BASE_URL, Config.HEADERS)
  pets_status = api_pet_store.find_pet_by_status(endpoint="findByStatus?status=sold", headers={'Accept': 'application/json'})
  api_pet_store.validate_pet_status(pets_status, "sold")