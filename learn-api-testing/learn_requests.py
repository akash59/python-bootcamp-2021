import requests
from requests.exceptions import HTTPError


# it will evaluate to True if the status code was between 200 and 400, and False otherwise.
def verify_response_exist(response):
    if response:
        print('Success !!')
    else:
        print('An error has occurred.')


def verify_request_status(urls):
    for url in urls:
        try:
            response = requests.get(url)
            response.encoding = 'utf-8'
            print(f'Status code for {url} is - {response.status_code}')
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')


def verify_request_content(urls):
    content = {}
    for url in urls:
        try:
            response = requests.get(url)
            print(response.json())
            response.encoding = 'utf-8'
            response.raise_for_status()
            if response.ok:
                content[url] = response.text
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
    return content


if __name__ == '__main__':
    BASE_URL = "https://api.github.com"
    resp = requests.get(BASE_URL)
    print(resp)
    print(resp.status_code)
    print(resp.json())
    verify_response_exist(resp)
    api_urls = [BASE_URL, BASE_URL+'/invalid']
    # verify_request_status(api_urls)
    url_contents = verify_request_content(api_urls)
    print(url_contents)
