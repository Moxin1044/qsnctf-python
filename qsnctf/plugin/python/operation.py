try:
    import requests
except ImportError:
    requests = None
import base64
import urllib.parse


def send_get_json(url, proxy="", timeout=10, params=None):
    if requests is None:
        raise ImportError("HTTP operations require the optional 'requests' dependency")
    if proxy == "":
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()
    else:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
        response = requests.get(url, params=params, proxies=proxies, timeout=timeout)
        response.raise_for_status()
        return response.json()


def get_base64(text):
    return base64.b64encode(text.encode()).decode()


def get_base64_url(text):
    return urllib.parse.quote(base64.b64encode(text.encode()).decode())