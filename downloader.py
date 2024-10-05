import requests

def download_file(url: str, save_path: str) -> bool:
    """
    Description
    -----------
    Download and save a file to the specified path.

    Parameters
    ----------
    url : str
    save_path : str

    Returns
    -------
    bool
    """
    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False
