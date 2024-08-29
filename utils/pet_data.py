def set_pet_data(id, category_id, category_name, name, photo_url, tag_id, tag_name, status):
    return {
            "id": id,
            "category": {
            "id": category_id,
            "name": category_name
            },
            "name": name,
            "photoUrls": [
            photo_url
            ],
            "tags": [
            {
            "id": tag_id,
            "name": tag_name
            }
            ],
            "status": status
        }