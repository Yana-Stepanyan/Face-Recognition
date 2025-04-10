import cv2 
import face_recognition 
import pickle
import os

def draw_rectangles(frame, face_locations, recognized_names, access_rooms):
    for idx, (top, right, bottom, left) in enumerate(face_locations):
        recognized = recognized_names[idx] != 'Unknown' and 'room' in access_rooms[idx]
        color = (0, 255, 0) if recognized else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        text = f"{recognized_names[idx]} - {'Access Granted' if recognized else 'Access Denied'} - {'room'}"
        (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
        text_x = left + (right - left - text_width) // 2
        text_y = top - 10 

        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

def load_database():
    faces_directory = 'registered_faces'
    database = {}
    for file_name in os.listdir(faces_directory):
        if file_name.endswith('.pkl'):
            with open(os.path.join(faces_directory, file_name), 'rb') as f:
                data = pickle.load(f)
                if isinstance(data, dict):
                    name = data.get('name')
                    access_rooms = data.get('access_rooms')
                    encoding = data.get('encoding')
                    if name is not None and access_rooms is not None and encoding is not None:
                        database[name] = {
                            'name': name,
                            'access_rooms': access_rooms,
                            'encoding': encoding
                        }
    return database

def recognize_faces(database):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        face_locations = face_recognition.face_locations(frame)
        recognized_names = ['Unknown'] * len(face_locations)
        access_rooms = ['N/A'] * len(face_locations)

        for idx, (top, right, bottom, left) in enumerate(face_locations):
            face_encoding = face_recognition.face_encodings(frame, [(top, right, bottom, left)])[0]
            for name, data in database.items():
                if face_recognition.compare_faces([data['encoding']], face_encoding)[0]:
                    recognized_names[idx] = data['name']
                    access_rooms[idx] = data['access_rooms']

        draw_rectangles(frame, face_locations, recognized_names, access_rooms)

        cv2.imshow('Face Recognition - Press Q to Quit', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    database = load_database()
    recognize_faces(database)
