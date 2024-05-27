import turtle as t

def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def map_coordinate(coordinate: tuple[float, float], width: float, height: float) -> tuple[float, float]:
    """
    주어진 좌표를 필요한 좌표계로 좌표 체계 변환(매핑) 및 Y 좌표 반전
    """
    x: float = coordinate[0]
    y: float = coordinate[1]
    x = map(x, 0, 1635, -((width-1)/2), (width-1)/2)
    y = map(y, 0, 1920, -((height-1)/2), (height-1)/2)
    return x, -y


def draw_filled_triangle(vertex0: tuple[float, float], vertex1: tuple[float, float], vertex2: tuple[float, float], colorData: tuple[float, float, float]):
    t.color(colorData[0], colorData[1], colorData[2])
    t.goto(vertex0)
    t.begin_fill()
    t.goto(vertex1)
    t.goto(vertex2)
    t.goto(vertex0) # 다시 시작 지점으로 돌아와야 완성
    t.end_fill()

def description():
    t.goto(0, -325)
    t.write("보로노이 다이어그램 고양이", align="center", font=("arial", 20, "bold"))
    t.goto(0, -355)
    t.write("10616 김주석", align="center", font=("arial", 15, "bold"))


data = [
    
]

import downloader
from pathlib import Path
if not Path("done.json").is_file():
    downloader.download("https://raw.githubusercontent.com/JuseokDev/VoronoiDiagramCat/main/done.json", "done.json")

import json

with open("done.json", "r") as f:
    data = json.load(f)

width, height = 545, 640

t.clearscreen()
t.setup(width+160, height+160)
t.bgcolor("#1A2828")
t.colormode(255)
t.penup()

t.speed(0)
t.tracer(False)

delta = (0, 40)

for d in data:
    v0 = map_coordinate(d[0], width, height)
    v1 = map_coordinate(d[1], width, height)
    v2 = map_coordinate(d[2], width, height)
    v0 = tuple(sum(elem) for elem in zip(v0, delta))
    v1 = tuple(sum(elem) for elem in zip(v1, delta))
    v2 = tuple(sum(elem) for elem in zip(v2, delta))
    draw_filled_triangle(v0, v1, v2, d[3])

description()

t.hideturtle()
t.done()
t.exitonclick()
