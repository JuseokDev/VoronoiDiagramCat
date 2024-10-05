#  ________  _______  _________  _______   ________ _________   
# |\   ___ \|\  ___ \|\___   ___\\  ___ \ |\   ____\\___   ___\ 
# \ \  \_|\ \ \   __/\|___ \  \_\ \   __/|\ \  \___\|___ \  \_| 
#  \ \  \ \\ \ \  \_|/__  \ \  \ \ \  \_|/_\ \  \       \ \  \  
#   \ \  \_\\ \ \  \_|\ \  \ \  \ \ \  \_|\ \ \  \____   \ \  \ 
#    \ \_______\ \_______\  \ \__\ \ \_______\ \_______\  \ \__\
#     \|_______|\|_______|   \|__|  \|_______|\|_______|   \|__|
                                                              
                                                              

import cv2
import json
from pathlib import Path

if not Path("division.png").is_file():
    raise FileNotFoundError(f"File not found.")

display = False

img = cv2.imread("division.png")

# 읽은 이미지를 그레이스케일(Greyscale)로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 임계값을 적용하여 회색조 이미지를 이진 이미지로 변환
ret,thresh = cv2.threshold(gray, 5, 255, 0)

# 윤곽선 찾기
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

approxs = []
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if 2 < len(approx) < 5:
        approx = [a[0] for a in approx]
        approxs.append(approx)
        img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
      

cv2.imwrite("done.png", img) # 처리된 파일 저장
if display:
    cv2.imshow("Shapes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

approxs = [[a.tolist() for a in approx] for approx in approxs]

with open("data.json", "w") as f:
    json.dump(approxs, f, indent=4)
