import cv2
import mediapipe
import webbrowser
import time

cap = cv2.VideoCapture(0)  #accessing webcam through opencv
initHand = mediapipe.solutions.hands  #mediapipe hand module initialization
mainHand = initHand.Hands(max_num_hands=1, min_detection_confidence=0.9, min_tracking_confidence=0.9)
# Minimum confidence value (between 0 and 1) for the hand detection to be considered successful and
# hand landmarks to be considered tracked successfully.
draw = mediapipe.solutions.drawing_utils
# For convenience, we will also access the drawing_utils from mediapipe,
# so we don’t need to use the complete path every time we want to use a functionality they expose.


#mediapipe hand utility to show hand lines and dots
def handLandmarks(colorImg):
    landmarkList = []
    landmarkPositions = mainHand.process(colorImg)
    landmarkCheck = landmarkPositions.multi_hand_landmarks
    if landmarkCheck:
        for hand in landmarkCheck:
            for index, landmark in enumerate(hand.landmark):     #enumerate() allows us to iterate through a sequence
                draw.draw_landmarks(img, hand, initHand.HAND_CONNECTIONS)
                h, w, c = img.shape
                centerX, centerY = int(landmark.x * w), int(landmark.y * h)  # retrieve the x, y, coordinates and place them into a vector for processing.

    return landmarkList

#defining fingers indexes
def fingers(landmarks):
    fingerTips = []
    tipIds = [4, 8, 12, 16, 20]

    # Check if thumb is up
    if landmarks[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingerTips.append(1)
    else:
        fingerTips.append(0)

    for id in range(1, 5):
        if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 3][2]:
            fingerTips.append(1)
        else:
            fingerTips.append(0)

    return fingerTips


while True:
    check, img = cap.read()   #for continious capturing of video
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #Convert BGR and RGB with OpenCV function cvtcolor
    lmList = handLandmarks(imgRGB)
    results = mainHand.process(img)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        finger = fingers(lmList)



        if finger[0] == 0 and finger[1] == 1 and finger[2] == 0 and finger[3] == 0 and finger[4] == 0:
            webbrowser.open("https://google.com")
            time.sleep(3)
        elif finger[0] == 0 and finger[1] == 1 and finger[2] == 1 and finger[3] == 0 and finger[4] == 0:
            webbrowser.open("https://youtube.com/")
            time.sleep(3)

        elif finger[0] == 0 and finger[1] == 1 and finger[2] == 1 and finger[3] == 1 and finger[4] == 0:
            webbrowser.open("https://www.linkedin.com/feed/")
            time.sleep(3)
        elif finger[0] == 0 and finger[1] == 1 and finger[2] == 1 and finger[3] == 1 and finger[4] == 1:
            webbrowser.open("https://github.com/")
            time.sleep(3)
        elif finger[0] == 1 and finger[1] == 1 and finger[2] == 1 and finger[3] == 1 and finger[4] == 1:
            webbrowser.open("https://learn.ineuron.ai/")
            time.sleep(3)



    cv2.imshow("Webcam", img) #for showing camera feed in window
    k = cv2.waitKey(1)  #for refresh rate 1 milliseconds

cap.release()  # release software / hardware resource
cv2.destroyAllWindows()