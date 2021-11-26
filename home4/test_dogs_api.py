import pytest
import requests
from jsonschema import validate
import random


def test_random_image_by_schema(dog_url):
    res = requests.get(dog_url + "/breeds/image/random")

    schema = {
        "message": "string",
        "status": "string",
        "required": ["message", "status"]
    }

    validate(instance=res.json(), schema=schema)


@pytest.mark.parametrize("count", [1, 5, 25, 50])
def test_valid_count_random_image(dog_url, count):
    res = requests.get(dog_url + f"/breeds/image/random/{count}")
    res_json = res.json()
    assert res_json['status'] == 'success'
    assert len(res_json['message']) == count


@pytest.mark.parametrize("count , expected_count", [
                                                    (-1, 1),
                                                    (0, 1),
                                                    ('a', 1),
                                                    (51, 50),
                                                    ('$', 1),
                                                    (None, 1),
                                                    ])
def test_not_valid_count_random_image(dog_url, count, expected_count):
    res = requests.get(dog_url + f"/breeds/image/random/{count}")
    res_json = res.json()
    assert len(res_json['message']) == expected_count
    assert res_json['status'] == 'success'


def test_random_breed(dog_url):
    req_list = requests.get(dog_url + f"/breeds/list/all")
    list_breed = req_list.json()
    res = requests.get(dog_url + f"/breed/{random.choice(list(list_breed['message'].keys()))}/images/random/")
    res_json = res.json()
    assert res.status_code == 200
    assert res_json['status'] == 'success'


def test_not_exist_breed(dog_url):
    res = requests.get(dog_url + f"/breed/absd/images/random/")
    res_json = res.json()
    assert res.status_code == 404
    assert res_json['status'] == 'error'
