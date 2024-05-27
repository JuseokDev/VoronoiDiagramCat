#  ________  ___  ___      ___ ___  ________  ___  ________  ________      
# |\   ___ \|\  \|\  \    /  /|\  \|\   ____\|\  \|\   __  \|\   ___  \    
# \ \  \_|\ \ \  \ \  \  /  / | \  \ \  \___|\ \  \ \  \|\  \ \  \\ \  \   
#  \ \  \ \\ \ \  \ \  \/  / / \ \  \ \_____  \ \  \ \  \\\  \ \  \\ \  \  
#   \ \  \_\\ \ \  \ \    / /   \ \  \|____|\  \ \  \ \  \\\  \ \  \\ \  \ 
#    \ \_______\ \__\ \__/ /     \ \__\____\_\  \ \__\ \_______\ \__\\ \__\
#     \|_______|\|__|\|__|/       \|__|\_________\|__|\|_______|\|__| \|__|
#                                     \|_________|                         
                                                                         
                                                                         
# 필요한 모듈 가져오기
import numpy as np
from PIL import Image
from pathlib import Path

filePath = "Downloads/black-cat-6944832_1920.png"

if not Path(filePath).is_file():
    raise FileNotFoundError("필요한 파일을 찾지 못했습니다.")

image = Image.open(filePath).convert("RGBA")
width, height = image.size

array = np.array(image)
resultArray = array.copy()

def get_nearby(y: int, x: int, distance: int) -> list | None:
    """
    x, y 좌표 주변(반경 distance)에 있는 픽셀들을 반환
    """
    if distance < 0:
        return
    startY = y - distance if y - distance >= 0 else 0
    startX = x - distance if x - distance >= 0 else 0
    done = []
    for X in range(startX, x + distance + 1):
        for Y in range(startY, y + distance + 1):
            done.append((X, Y))

    return done

for h, y in enumerate(array):
    for w, data in enumerate(y):
        r: int = data[0]
        g: int = data[1]
        b: int = data[2]
        a: int = data[3]
        if a < 255:
            resultArray[h][w] = (0, 0, 0, 255)
            for n in get_nearby(h, w, 2):
                if len(resultArray) > n[1] and len(resultArray[0]) > n[0]:
                    resultArray[n[1]][n[0]] = (0, 0, 0, 255)

Image.fromarray(resultArray).save("division.png")
print("done")
