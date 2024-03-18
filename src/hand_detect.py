import cv2
import mediapipe as mp
import numpy as np
xp, yp = 0, 0

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingerCoordinates = [(8,6),(12,10),(16,14),(20,18)]
thumbCordinates = [(4,2)]

width = 1280
height = 720

canvas = np.zeros((height,width,3),np.uint8)

drawcolor = (0,0,255)
brushThickness = 5


def detctHands():
    while True:
        success , img = cap.read()
        if success:
            img = cv2.flip(img,1)
        
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = hands.process(img)
        multiLandMark = results.multi_hand_landmarks
        # handPoints = getHandPoints(img,multiLandMark)
        # displayScreen(img)
        return img,multiLandMark

def getHandPoints(img, multiLandMark):
    mode = None
    cord = None
    handPoints = []
    if multiLandMark:    
        for handLms in multiLandMark:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for landmark_Id, land_Mark in enumerate(handLms.landmark):
                # print(landmark_Id, land_Mark)
                h, w, c = img.shape
                cx, cy = int(land_Mark.x * w), int(land_Mark.y * h)
                # print(landmark_Id,cx,cy)
                handPoints.append((cx, cy))
                
        mode, cord = detect_mode(handPoints)

    return mode, cord if cord else (0, 0), handPoints

def draw_coordinates(img,handPoints):
    for points in handPoints:
        cv2.circle(img,points,7,(255,0,255),cv2.FILLED)
        
def detect_mode(hand_points):
    fingers = [False] * len(fingerCoordinates)
    for i in range(len(fingerCoordinates)): 
        coordinates = fingerCoordinates[i]
        if hand_points[coordinates[0]][1] > hand_points[coordinates[1]][1]:
            fingers[i] = True
                
    if (fingers[1] and fingers[2] and fingers[3]) and (not fingers[0]):
        points = fingerCoordinates[0]
        cord = [hand_points[points[0]][0], hand_points[points[0]][1]]
        return 1 , cord
                    
    elif (fingers[2] and fingers[3]) and (not fingers[0] and not fingers[1]):
        points = fingerCoordinates[0]
        cord = [hand_points[points[0]][0], hand_points[points[0]][1]]
        return 2 , cord

    elif ((fingers[3]) and (not fingers[0] and not fingers[1] and not fingers[2])):
        return "Menu Activated ! " , None
                    
    elif fingers[0] and fingers[1] and fingers[2] and fingers[3]:
        return "All closed !" , None

    elif fingers[0] == False and fingers[1] == False and fingers[2] == False and fingers[3] == False:
        return "All opened !" , None
    else:
        return 0 , None

def displayScreen(img):
    imgGray = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)
    _ , imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_or(img,canvas)

    cv2.imshow("Air Canvas",img)
    # cv2.imshow("canvas" , canvas)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()
        return True
    return False

def start():
    global xp, yp

    while True:
        img, multiLandMark = detctHands()
        mode, cord, handPoints = getHandPoints(img, multiLandMark)
       
        if mode == 1:
            drawcolor = (0,0,255)
            x1, y1 = cord[0], cord[1]
            if xp != 0 and yp != 0:
                cv2.line(canvas, (xp, yp), (x1, y1), drawcolor, brushThickness)
            xp, yp = x1, y1

        elif mode == 2:
            drawcolor = (0,0,0)
            x1, y1 = cord[0], cord[1]
            if xp != 0 and yp != 0:
                cv2.line(canvas, (xp, yp), (x1, y1), drawcolor, 50)
            xp, yp = x1, y1

        elif mode != 0 and mode != 1:
            xp, yp = 0 , 0
            print(mode)

        else:
            xp, yp = 0 , 0


        draw_coordinates(img, handPoints)
        if displayScreen(img):
            break

       


