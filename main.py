# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from facelib import FaceClassifier

# 웹캠을 열기 위해 VideoCapture 객체 생성
cap = cv2.VideoCapture(0)

# FaceClassifier 객체 생성
face_classifier = FaceClassifier()

# 웹캠 프레임을 반복적으로 처리
while True:
    # 웹캠에서 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 얼굴 분류 수행
    face_labels = face_classifier.classify(frame)

    # 분류 결과를 화면에 표시
    for label in face_labels:
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 화면에 프레임 표시
    cv2.imshow('Unknown Face Classifier', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠과 윈도우 창 해제
cap.release()
cv2.destroyAllWindows()