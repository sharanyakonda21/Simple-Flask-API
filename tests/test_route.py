from flask import url_for

url = None
unsanitized = {"result": "unsanitized"}
sanitized = {"result": "sanitized"}


def run_request(client, json, is_sanitized=False):
    resp = client.post(url, json=json)
    assert resp.json == unsanitized if not is_sanitized else sanitized

def test_GET_not_allowed(client):
    # set url in request context
    global url
    url = url_for("check_sql_injection")

    assert client.get(url).status_code == 405

def test_ASCII_NUL_case(client):
    json = {"payload":"\0; SELECT * FROM users;"}
    run_request(client, json)

def test_single_quote(client):
    json = {"payload":"SELECT * FROM users;\'"}
    run_request(client, json)

def test_double_quote(client):
    json = {"payload":"SELECT * FROM users;\""}
    run_request(client, json)

def test_backspace(client):
    json = {"payload":"SELECT * FROM users\b;"}
    run_request(client, json)

def test_newline(client):
    json = {"payload":"SELECT * \n FROM users;"}
    run_request(client, json)

def test_carriage_return(client):
    json = {"payload":"\rSELECT * FROM users;"}
    run_request(client, json)

def test_tab(client):
    json = {"payload":"j;\tSELECT name FROM cities;"}
    run_request(client, json)

def test_ASCII_26(client):
    # \Z is an invalid escape sequence
    # will give warning
    json = {"payload":"j;\ZSELECT name FROM cities;"}
    run_request(client, json)

def test_back_slash(client):
    json = {"payload":"Enth;SELECT name FROM cities;\\;--"}
    run_request(client, json)
    
def test_modulus(client):
    # \% is an invalid escape sequence
    # will give warning
    json = {"payload":"Enth;SELECT\%Home;--"}
    run_request(client, json)

def test_bar(client):
    # \_ is an invalid escape sequence
    # will give warning
    json = {"payload":"Enth;_SELECT\_;--"}
    run_request(client, json)

def test_normal_input(client):
    json = {"payload":"John wick"}
    run_request(client, json, is_sanitized=True)