import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingerCordinates = [(8,6),(12,10),(16,14),(20,18)]
thumbCordinates = [(4,2)]

def activateAndReturnCord():
    while True:
        success , img = cap.read()
        if success:
            img = cv2.flip(img,1)
        
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = hands.process(img)
        multiLandMark = results.multi_hand_landmarks
        if multiLandMark:
            handPoints = []
            for handLms in multiLandMark:
                mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
                for landmark_Id,land_Mark in enumerate(handLms.landmark):
                    # print(landmark_Id,land_Mark)
                    h , w , c = img.shape
                    cx,cy = int(land_Mark.x * w),int(land_Mark.y * h)
                    # print(landmark_Id,cx,cy)
                    handPoints.append((cx,cy))
                
            
            for point in handPoints:
                # print(point)
                cv2.circle(img,point,3,(0,0,0),cv2.FILLED)

            fingers = [False,False,False,False]
            
            for i in range(4): 
                coordinates = fingerCordinates[i]
                if handPoints[coordinates[0]][1] > handPoints[coordinates[1]][1]:
                    fingers[i] = True
            
            if (fingers[1] and fingers[2] and fingers[3]) and (fingers[0] == False):
                print("Drawing Mode Activated !")
                
            elif (fingers[2] and fingers[3]) and (fingers[0] == False and fingers[1] == False):
                print("Selection Mode Activated !")

            elif ((fingers[3]) and (fingers[0] == False and fingers[1] == False and fingers[2] == False)):
                print("Menu Activated ! ")
                
            elif fingers[0] and fingers[1] and fingers[2] and fingers[3]:
                print("None !")
            

            # for coordinates in fingerCordinates:
            #     if handPoints[coordinates[0]][1] < handPoints[coordinates[1]][1]:
            #         print("all opened")
            #     else:
            #         print("Index and Middle open !")
            
        cv2.imshow("Detecting hands",img)
        cv2.waitKey(1)
