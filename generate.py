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

def get_centroid_coordinates(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> tuple[float, float]:
  """
  삼각형의 세 꼭짓점의 좌표로 무게중심의 좌표를 계산
  """

  # 무게중심 좌표 계산
  centroid_x = (x1 + x2 + x3) / 3
  centroid_y = (y1 + y2 + y3) / 3

  return centroid_x, centroid_y

def get_color(array: np.ndarray, x: int, y: int) -> tuple[int, int, int]:
   return [int(item) for item in array[y][x]][0:3]

done = []

for d in data:
    x1 = d[0][0]
    y1 = d[0][1]
    x2 = d[1][0]
    y2 = d[1][1]
    x3 = d[2][0]
    y3 = d[2][1]
    x, y = get_centroid_coordinates(x1, y1, x2, y2, x3, y3) # 
    x, y = round(x), round(y) # 실수(부동소수점)을 정수로 변환
    r, g, b = get_color(np_array, x, y)
    done.append([[x1, y1], [x2, y2], [x3, y3], [r, g, b]])

with open("done.json", "w") as f:
   json.dump(done, f, indent=4)

print("done")
