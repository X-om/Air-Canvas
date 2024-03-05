import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingerCoordinates = [(8,6),(12,10),(16,14),(20,18)]
thumbCordinates = [(4,2)]

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

def getHandPoints(img,multiLandMark):
    mode = None
    handPoints = []
    if multiLandMark:    
        for handLms in multiLandMark:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            for landmark_Id,land_Mark in enumerate(handLms.landmark):
                # print(landmark_Id,land_Mark)
                h , w , c = img.shape
                cx,cy = int(land_Mark.x * w),int(land_Mark.y * h)
                # print(landmark_Id,cx,cy)
                handPoints.append((cx,cy))
        
    
    
        mode = detect_mode(handPoints)


        
    
    return mode,handPoints

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
        return "Drawing Mode Activated !"
                    
    elif (fingers[2] and fingers[3]) and (not fingers[0] and not fingers[1]):
        return "Selection Mode Activated !"

    elif ((fingers[3]) and (not fingers[0] and not fingers[1] and not fingers[2])):
        return "Menu Activated ! "
                    
    elif fingers[0] and fingers[1] and fingers[2] and fingers[3]:
        return "All closed !"

    elif fingers[0] == False and fingers[1] == False and fingers[2] == False and fingers[3] == False:
        return "All opened !"

def displayScreen(img):
    cv2.imshow("Air Canvas",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()
        return True
    return False

def start():
    while True:       
        img ,  multiLandMark = detctHands()
        mode,handPoints = getHandPoints(img,multiLandMark)
        if mode != None:
            print(mode)
        draw_coordinates(img,handPoints)
        if displayScreen(img):
            break


