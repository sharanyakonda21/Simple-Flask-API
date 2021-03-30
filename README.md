# SQL INJECTION DETECTOR

## To run application

- create virtual environment

    `python3 -m venv venv`

- activate the virtual environment

    `source venv/bin/activate`

- install dependencies

    ``` shell
    pip install --upgrade pip
    pip install -r requirements.py
    ```

- run app

    `flask run`

- to run test

    `pytest`

## Notes

### Problem

Create a simple API in flask framework

### Functionality

API that takes POST JSON payload

### URL Path

/v1/sanitized/input/

### POST Payload Example

{
“payload”: “input"
}

### Result

The API should return if the payload input has any characters that could be used to do SQL injection

Result 1:
{
“result”: “sanitized"
}

Result 2:
{
“result”: “unsanitized"
