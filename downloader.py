import requests

def download_file(url: str, save_path: str) -> bool:
    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

download = download_file
