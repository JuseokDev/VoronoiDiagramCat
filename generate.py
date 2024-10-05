#  ________  _______   ________   _______   ________  ________  _________  _______      
# |\   ____\|\  ___ \ |\   ___  \|\  ___ \ |\   __  \|\   __  \|\___   ___\\  ___ \     
# \ \  \___|\ \   __/|\ \  \\ \  \ \   __/|\ \  \|\  \ \  \|\  \|___ \  \_\ \   __/|    
#  \ \  \  __\ \  \_|/_\ \  \\ \  \ \  \_|/_\ \   _  _\ \   __  \   \ \  \ \ \  \_|/__  
#   \ \  \|\  \ \  \_|\ \ \  \\ \  \ \  \_|\ \ \  \\  \\ \  \ \  \   \ \  \ \ \  \_|\ \ 
#    \ \_______\ \_______\ \__\\ \__\ \_______\ \__\\ _\\ \__\ \__\   \ \__\ \ \_______\
#     \|_______|\|_______|\|__| \|__|\|_______|\|__|\|__|\|__|\|__|    \|__|  \|_______|
                                                                                      
                                                                                      
                                                                                      
# 필요한 모듈
import json
import numpy as np
from PIL import Image

# 꼭짓점 좌표를 저장한 파일 읽어와서 data에 저장
with open("data.json", "r") as f:
    data = json.load(f)

# 원본 이미지 읽어오기
image = Image.open("./Downloads/Download.png")
np_array = np.array(image)

def get_centroid_coordinates(vertices: list[tuple[float, float]]) -> tuple[float, float]:
    """
    Description
    -----------
    꼭짓점의 좌표로 무게중심의 좌표를 계산

    Parameters
    ----------
    vertices : list
        꼭짓점의 좌표가 들어있는 리스트

    Returns
    -------
    tuple
        무게중심의 좌표
    """

    # 무게중심 좌표 계산
    num_vertices = len(vertices)

    if num_vertices == 0:
        return (0, 0)
    
    sum_x, sum_y = 0, 0
    for x, y in vertices:
        sum_x += x
        sum_y += y
    
    centroid_x = sum_x / num_vertices
    centroid_y = sum_y / num_vertices

    return centroid_x, centroid_y

def get_color(array: np.ndarray, x: int, y: int) -> tuple[int, int, int]:
    return [int(item) for item in array[y][x]][0:3]

done = []

for d in data:
    x, y = get_centroid_coordinates(d) # 무게중심의 좌표를 꼭짓점들로 계산
    x, y = round(x), round(y) # 실수(부동소수점)을 정수로 변환
    r, g, b = get_color(np_array, x, y)
    done.append(d + [[r, g, b]])

with open("done.json", "w") as f:
    json.dump(done, f, indent=4)
