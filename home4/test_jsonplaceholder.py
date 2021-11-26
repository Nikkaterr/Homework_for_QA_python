import pytest
import requests
from jsonschema import validate


def test_getting_resource_by_schema(jsonholder_url):
    res = requests.get(jsonholder_url + f"/1")

    schema = {
        "userId": int,
        "id": int,
        "title": "string",
        "body": "string",
        "required": ["userId", "id", "title", "body"]
    }

    validate(instance=res.json(), schema=schema)


@pytest.mark.parametrize("user_id , result", [
                                                    (3, 10),
                                                    (0, 0),
                                                    ('a', 0),
                                                    (11, 0),
                                                    ('$', 0),
                                                    (None, 0),
                                                    ])
def test_filter_post_by_user_id(jsonholder_url, user_id, result):
    res = requests.get(jsonholder_url + f"?userId={user_id}")
    res_json = res.json()
    assert len(res_json) == result
    assert res.status_code == 200


def test_create_resource(jsonholder_url):
    res = requests.post(jsonholder_url, json={'userId': 2, 'title': 'test_title', 'body': 'test_body'})
    res_json = res.json()
    assert res.status_code == 201
    assert res_json['id'] == 101


def test_delete_resource(jsonholder_url):
    res = requests.delete(jsonholder_url + f"/1")
    res_json = res.json()
    assert res.status_code == 200
    assert len(res_json) == 0


@pytest.mark.parametrize("key , value", [
                                                    ('userID', 10),
                                                    ('id', 123),
                                                    ('title', 'test_title_2'),
                                                    ('body', 'test_body'),
                                                    ])
def test_filter_post_by_user_id(jsonholder_url, key, value):
    res = requests.patch(jsonholder_url + f"/3", json={key: value})
    res_json = res.json()
    assert res.status_code == 200
    assert res_json[key] == value
