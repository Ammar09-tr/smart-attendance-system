import face_recognition
import cv2
import os
from datetime import datetime

known_encodings = []
known_names = []

for filename in os.listdir("known_faces"):
    img = face_recognition.load_image_file(f"known_faces/{filename}")
    encoding = face_recognition.face_encodings(img)[0]
    known_encodings.append(encoding)
    known_names.append(filename.split(".")[0])

print(f"Loaded {len(known_names)} known faces")

video = cv2.VideoCapture(0)
marked_today = set()

while True:
    ret, frame = video.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for encoding, location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"

        if True in matches:
            name = known_names[matches.index(True)]

            if name not in marked_today:
                marked_today.add(name)
                with open("attendance_log.csv", "a") as f:
                    f.write(f"{name},{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                print(f"Marked: {name}")

        top, right, bottom, left = location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()