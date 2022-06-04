import cv2
# pipeline below worked
# cap = cv2.VideoCapture("thetauvcsrc \
#     ! decodebin \
#     ! autovideoconvert \
#     ! video/x-raw,format=BGRx \
#     ! queue ! videoconvert \
#     ! video/x-raw,format=BGR ! queue ! appsink")

# pipeline suggestion thanks to nickel110
# attempt to force hardware acceleration
# tested with NVIDIA 510.73 with old GTX 950 on Ubuntu 22.04
cap = cv2.VideoCapture("thetauvcsrc \
    ! queue \
    ! h264parse \
    ! nvdec \
    ! gldownload \
    ! queue \
    ! videoconvert n-threads=0 \
    ! video/x-raw,format=BGR \
    ! queue \
    ! appsink")

if not cap.isOpened():
    raise IOError('Cannot open RICOH THETA')

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('frame', frame)


    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
