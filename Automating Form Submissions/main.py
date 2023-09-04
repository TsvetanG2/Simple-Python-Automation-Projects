import requests


def submit_form(url, form_data):
    res = requests.post(url, data=form_data)

    if res.status_code == 200:
        pass
    