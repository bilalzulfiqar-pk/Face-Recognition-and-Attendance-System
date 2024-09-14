import cv2
import face_recognition


def add_record(id, name):
    # print(id,name)

    if id == '' or name == '':  # Check if the Text Fields are empty
        print('Text Fields Cannot be Empty..')
    elif not id.isnumeric():  # To Check that the ID Field contain only Numeric Values
        print('Only Numeric Values are Allowed in ID Field')
    # To Check that the name Field contain only Alphabets
    elif not all(char.isalpha() or char.isspace() for char in name):
        print('Only Alphabets and Spaces are Allowed in name Field')
    else:
        print('Opening WebCam....')
        cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)

        while True:
            success, frame = cap.read()  # return a single frame in variable `frame`

            frame2 = frame.copy()
            faces_locations = face_recognition.face_locations(frame2)  # Get face-locations from frame2
            for face_loc in faces_locations:
                y1, x2, y2, x1 = face_loc
                cv2.rectangle(frame2, (x1, y1), (x2, y2), (0, 255, 0),
                              2)  # draw Rectangle around faces in frame2 with face locations

            cv2.imshow('WebCam', frame2)  # display the Frame with box around faces
            key = cv2.waitKey(1)
            if key == ord('t'):  # save on pressing "t"
                cv2.imwrite(f'Images/{id}.{name}.jpg', frame)  # will overwrite file if already exists
                print('Image Saved Successfully')
                cv2.destroyAllWindows()
                break
            elif key == ord('q'):  # quit on pressing 'q'
                cv2.destroyAllWindows()
                break

        cap.release()
        print('WebCam Closed')
