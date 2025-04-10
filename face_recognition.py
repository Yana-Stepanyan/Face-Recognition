import cv2 
import face_recognition 
import os
import pickle

def draw_rectangles(frame, face_locations):
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

def register_faces():
    faces_directory = 'registered_faces'

    if not os.path.exists(faces_directory):
        os.makedirs(faces_directory)
 
    name = input("Enter the name of the person: ")
    access_rooms = input("Enter the room(s) the person has access to (comma-separated): ").split(',')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        face_locations = face_recognition.face_locations(frame)

        draw_rectangles(frame, face_locations)

        cv2.imshow('Register Faces - Press S to Capture', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('s'):
            print(f"Capture complete!")
            print(face_locations)
            
            if len(face_locations) == 1:
                face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
                data = {'name': name, 'access_rooms': access_rooms, 'encoding': face_encoding}
                with open(os.path.join(faces_directory, f'{name}.pkl'), 'wb') as f:
                    pickle.dump(data, f)
                print(f"Face registered for {name} with access to {', '.join(access_rooms)}")
                break
           

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    register_faces()
