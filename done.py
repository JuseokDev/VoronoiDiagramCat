import json
import downloader
import turtle as t
from pathlib import Path

def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def map_coordinate(coordinate: tuple[float, float], width: float, height: float) -> tuple[float, float]:
    """
    Description
    -----------
    주어진 좌표를 필요한 좌표계로 좌표 체계 변환(매핑) 및 Y 좌표 반전

    Parameters
    ----------
    coordinate : tuple

    Returns
    -------
    tuple
    """
    x: float = coordinate[0]
    y: float = coordinate[1]
    x = map(x, 0, 1635, -((width-1)/2), (width-1)/2)
    y = map(y, 0, 1920, -((height-1)/2), (height-1)/2)
    return x, -y


def draw_shape_by_vertices(vertices: list[tuple[float, float]], color_data: tuple[float, float, float]):
    t.color(color_data[0], color_data[1], color_data[2])
    t.goto(vertices[0])
    t.begin_fill()
    for vertex in vertices[1:]:
        t.goto(vertex)
    t.goto(vertices[0])
    t.end_fill()

def description():
    t.goto(0, -325)
    t.write("보로노이 다이어그램 고양이", align="center", font=("arial", 20, "bold"))
    t.goto(0, -355)
    t.write("JuseokDev", align="center", font=("arial", 15, "bold"))


data = [
    
]

if not Path("done.json").is_file():
    downloader.download("https://raw.githubusercontent.com/JuseokDev/VoronoiDiagramCat/main/done.json", "done.json")


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
    vertices = []
    for index, vertex in enumerate(d[:-1]):
        vertex = map_coordinate(vertex, width, height)
        vertex = tuple(sum(elem) for elem in zip(vertex, delta))
        vertices.append(vertex)
    draw_shape_by_vertices(vertices, d[-1])

description()

t.hideturtle()
t.done()
t.exitonclick()
