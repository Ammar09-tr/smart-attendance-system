# smart-attendance-system

A real-time face recognition based attendance system built with Python, 
OpenCV, and dlib. Detects registered faces via webcam and automatically 
logs attendance with timestamps to prevent duplicate entries.

## Features
- Real-time face detection and recognition via webcam
- Automatic CSV-based attendance logging with timestamps
- Duplicate-entry prevention (one mark per person per day)
- Live bounding-box display with identified names

## Tech Stack
- Python
- OpenCV (video capture & display)
- face_recognition / dlib (face detection & encoding)
- Pandas (data logging)
- Power BI (attendance analytics dashboard)

## How It Works
1. Known faces are registered as images and converted into face encodings
2. Live webcam feed is scanned frame-by-frame for faces
3. Detected faces are compared against known encodings
4. On match, attendance is logged to `attendance_log.csv` with timestamp

## Setup
\`\`\`bash
pip install opencv-python numpy pandas face_recognition
python recognize.py
\`\`\`

## Screenshots
(add a screenshot or short GIF here)

## Future Improvements
- Database integration instead of CSV
- Mobile app for viewing attendance remotely
- Multi-camera support
