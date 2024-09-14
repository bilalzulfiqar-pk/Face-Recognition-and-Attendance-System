This project is a face recognition-based attendance system built using Python, OpenCV, and the face_recognition library. It captures images from a webcam, recognizes faces by comparing them with pre-saved images, and marks attendance in a CSV file. The system allows you to add new records by capturing a face and associating it with an ID and name, then later it can automatically recognize the person and mark their attendance when detected.

Features:

1. Capture and save face images for new records.
2. Identify faces in real-time from webcam footage.
3. Mark attendance in a CSV file with a timestamp.
4. Provides feedback when attendance is successfully marked.
5. Recognizes both known and unknown faces.

Usage:
1. Press q to quit the webcam.
2. Press t to capture and save a face when adding a new record.

File Structure:

1. Images/: Folder where all face images are stored.
2. Attendance/: Folder where attendance CSV files are saved.

Notes:
1. Ensure that no extra files or subfolders are present in the Images/ folder, as this may cause errors.
2. I used Python 3.9
3. The system compares faces based on a threshold of 0.5 for accurate recognition.
