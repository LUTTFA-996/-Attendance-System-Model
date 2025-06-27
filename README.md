# Attendance-System-Model
Attendance System with Face Recognition and Emotion Detection (9:30 AM – 10:00 AM Window)
# Dataset Preparation
Face Dataset: I take Student picture (folders of alex, anjela, luttfa) each containing student face images (jpg)
# Face Recognition Model
- Load student face images
- Encode labels (student names)
- Train KNN classifier on face embeddings
# Emotion Detection Model
- Build and train CNN model
- Save model as **emotion_model.h5**
# Real-time Attendance Monitoring (Using Webcam)
- Start attendance window: 9:30 AM – 10:00 AM
- Detect faces from webcam
- Recognize student identity using trained KNN
- Detect student emotion using CNN model
- Avoid duplicate marking (one attendance per student)
- Allow manual stop ('q' or ESC key)
# Attendance Marking
- Mark "Present" with Name, Time, and Detected Emotion
- After time window closes, automatically mark non-detected students as "Absent"
- Save final attendance data as CSV file
# Model Accuracy & Evaluation
# Output Files
- Attendance CSV: 'C:\Users\Lutifah\Desktop\INTERSHIP\Attendance System Model\attendance_record.csv'
# Trained emotion model:
- emotion_model.h5
