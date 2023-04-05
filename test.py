import cv2 as cv

cap = cv.VideoCapture("Training (13).mp4")

_, frame1 = cap.read()
_, frame2 = cap.read()


# _, frame3 = cap.read()
# _, frame4 = cap.read()


# resized1 = cv.resize(frame1, (920, 650))
# resized2 = cv.resize(frame2, (920, 650))

# print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# cap.set(3, 800)
# cap.set(4, 600)
# print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))


while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv.threshold(blur, 10, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=2)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    for c in contours:
        (x,y,w,h) = cv.boundingRect(c)

        if cv.contourArea(c) < 17700:
            continue
        
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv.putText(frame1, "Status: Car Movement Detected", (10,30), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)


    # gray2 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    # blur2 = cv.GaussianBlur(gray2, (5,5), 0)
    # _, thresh2 = cv.threshold(blur2, 10, 255, cv.THRESH_BINARY)
    # dilated2 = cv.dilate(thresh2, None, iterations=2)
    # contours2, _ = cv.findContours(dilated2, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    # for c in contours2:
    #     (x,y,w,h) = cv.boundingRect(c)

    #     if cv.contourArea(c) < 17700:
    #         continue
        
    #     # cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)

    #     ##TEST##
    #     approx = cv.approxPolyDP(c, 0.*cv.arcLength(c, True),True)
    #     cv.drawContours(frame1, [approx], 0, (0,255,0), 2)

    cv.imshow('window', frame1)
    frame1 = frame2
    _, frame2 = cap.read()

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()