import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=2)


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    #print(len(hands))
    #hands = detector.findHands(img, draw=False)

    #Hand - dict (-lmList - bbox -center -type)

    if hands:
    # hand1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #list of 21 landmarks points
        bbox1 = hand1["bbox"] #boundingbox info of x, y, z, y
        centerPoint1 = hand1["center"] #center of the hands cx, cy
        handType1 = hand1["type"] # hand type - left or right

        fingers1 = detector.fingersUp(hand1)

        #displaying distance btw fingers->
        #length, info, img = detector.findDistance(lmList1[8], lmList1[12], img)

        #print(len(lmList1),lmList1)
        #print(bbox1)
        #print(centerPoint1)
        #print(handType1)

        # to check the second hand
        if len(hands)==2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # list of 21 landmarks points
            bbox2 = hand2["bbox"]  # boundig box info of x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hands cx, cy
            handType2 = hand2["type"]  # hand type - left or right

            fingers2 = detector.fingersUp(hand2)
            #print(handType1,handType2)
            #print(fingers1, fingers2)
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)


    cv2.imshow("Image", img)
    cv2.waitKey(1)