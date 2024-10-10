#  ________  ___  ___      ___ ___  ________  ___  ________  ________      
# |\   ___ \|\  \|\  \    /  /|\  \|\   ____\|\  \|\   __  \|\   ___  \    
# \ \  \_|\ \ \  \ \  \  /  / | \  \ \  \___|\ \  \ \  \|\  \ \  \\ \  \   
#  \ \  \ \\ \ \  \ \  \/  / / \ \  \ \_____  \ \  \ \  \\\  \ \  \\ \  \  
#   \ \  \_\\ \ \  \ \    / /   \ \  \|____|\  \ \  \ \  \\\  \ \  \\ \  \ 
#    \ \_______\ \__\ \__/ /     \ \__\____\_\  \ \__\ \_______\ \__\\ \__\
#     \|_______|\|__|\|__|/       \|__|\_________\|__|\|_______|\|__| \|__|
#                                     \|_________|                         
                                                                         
                                                                         
import downloader
import numpy as np
from PIL import Image
from pathlib import Path

file_path = "./downloads/download.png"

Path("./downloads").mkdir(exist_ok=True)
if not Path(file_path).is_file():
    downloader.download("https://raw.githubusercontent.com/JuseokDev/VoronoiDiagramCat/main/downloads/download.png", file_path)

image = Image.open(file_path).convert("RGBA")
width, height = image.size

array = np.array(image)
result_array = array.copy()

def get_nearby(y: int, x: int, distance: int) -> list | None:
    """
    Description
    -----------
    (x, y) 좌표 주변에 있는 픽셀들을 반환 (주변 반경 distance)

    Parameters
    ----------
    y : int
    x : int
    distance : int

    Returns
    -------
    list
    """
    if distance < 0:
        return
    startY = y - distance if y - distance >= 0 else 0
    startX = x - distance if x - distance >= 0 else 0
    pixels_list = []
    for X in range(startX, x + distance + 1):
        for Y in range(startY, y + distance + 1):
            pixels_list.append((X, Y))

    return pixels_list

for h, y in enumerate(array):
    for w, data in enumerate(y):
        r: int = data[0]
        g: int = data[1]
        b: int = data[2]
        a: int = data[3]
        if a < 255:
            result_array[h][w] = (0, 0, 0, 255)
            for n in get_nearby(h, w, 2):
                if len(result_array) > n[1] and len(result_array[0]) > n[0]:
                    result_array[n[1]][n[0]] = (0, 0, 0, 255)

Image.fromarray(result_array).save("division.png")
