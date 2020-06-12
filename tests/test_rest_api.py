import requests
import json

base_url = 'http://localhost:5000/'
def test_search():
    url = base_url + "search"

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = dict(ids=[0, 1, 2])
    print(url)
    # convert dict to json by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    # Validate response headers and body contents, e.g. status code.
    print(resp.status_code)
    assert resp.status_code == 200
    resp_body = resp.json()
    #assert resp_body['url'] == url

    # print response full body as text
    print(resp.text)

test_search()