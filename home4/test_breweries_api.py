import pytest
import requests
from jsonschema import validate


def test_autocomplete_by_schema(brewer_url):
    res = requests.get(brewer_url + f"/autocomplete?query=company")

    schema = {
        "id": "string",
        "name": "string",
        "required": ["id", "name"]
    }

    validate(instance=res.json(), schema=schema)


@pytest.mark.parametrize("id_brewer", ['1234', 12432, 'a', '$$%'])
def test_get_brewer_by_id(brewer_url, id_brewer):
    res = requests.get(brewer_url + f"/{id_brewer}")
    res_json = res.json()
    assert res.status_code == 404
    assert res_json['message'] == "Couldn't find Brewery"


@pytest.mark.parametrize("filters , value, result_value", [
                                                    ('city', 'san_diego', 'San Diego'),
                                                    ('postal', '44107_4020', '44107_4020'),
                                                    ('type', 'bar', 'bar'),
                                                    ])
def test_search_brewers_by_filters(brewer_url, filters, value, result_value):
    res = requests.get(brewer_url + f"?by_{filters}={value}")
    res_json = res.json()
    assert res.status_code == 200
    for i in range(len(res_json)):
        key_dict = res_json[i].keys()
        key = [k for k in key_dict if filters in k]
        assert res_json[i][key[0]] == result_value


@pytest.mark.parametrize("value, part_of_value1, part_of_value2", [('dog', 'do', 'og')])
def test_brewer_search(brewer_url, value, part_of_value1, part_of_value2):
    res = requests.get(brewer_url + f"/search?query={value}")
    res_json = res.json()
    assert res.status_code == 200
    for i in range(len(res_json)):
        assert part_of_value1 in res_json[i]['id'] or part_of_value2 in res_json[i]['id']


@pytest.mark.parametrize("value, count", [
    (1, 1),
    (0, 0),
    (50, 50),
    (51, 50)
])
def test_count_per_page_valid_value(brewer_url, value, count):
    res = requests.get(brewer_url + f"?per_page={value}")
    res_json = res.json()
    assert res.status_code == 200
    assert len(res_json) == count

