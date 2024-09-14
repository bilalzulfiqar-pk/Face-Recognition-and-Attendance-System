import face_recognition
import cv2
import os
import numpy as np
from datetime import datetime


def mark_attendance():
    path = 'Images'
    images = []
    class_full_names = []
    class_names = []
    class_id = []
    my_list = os.listdir(path)  # To Get All the items name (with Extension) inside that path Folder
    # print('Files in Images Folder\n', my_list)

    for cl in my_list:
        cur_img = cv2.imread(f'{path}/{cl}')  # To Read Images
        images.append(cur_img)

        # here splitext Removes the extension (like .jpg) from File Name
        class_full_names.append(os.path.splitext(cl)[0])

        # print(class_full_names)

    try:
        # print('List of Persons in DB:\n\nID\t\tName')
        for cl in class_full_names:
            full_name = cl.split('.')
            class_id.append(full_name[0])  # Append ID in ClassId Array
            class_names.append(full_name[1])  # Append Name in ClassNames Array
            # print(full_name[0] + '\t\t' + full_name[1])
    except:
        print('Error....')
        print('Error in Splitting Image Names....\nCheck Image File Names in Image Folder')
        print('Also Note that there should not be any other File/Folder in Images Folder.')
        print('Check the Folder and run again...')
        exit()

    def find_encodings(images):
        encode_list = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert Image Color From BGR to RGB
            encode = face_recognition.face_encodings(img)[0]  # Getting Encoding from Image
            encode_list.append(encode)
        return encode_list

    def save_attendance(id, name):
        now = datetime.now()  # Stores Current DateTime in 'now'
        # print(now)
        date = now.strftime('%d-%m-%Y')  # Storing Date in specific Format
        filename = 'Attendance ' + date + '.csv'
        folder = 'Attendance'

        if not os.path.exists(f'{folder}/{filename}'):  # Check if File don't exist
            with open(f'{folder}/{filename}', 'w') as nf:  # To Create New File
                nf.writelines('ID,Name,date,time')  # To Add Attributes
        with open(f'{folder}/{filename}', 'r+') as f:  # Opens File (CSV File)
            my_data_list = f.readlines()  # Stores All Lines of File into 'my_data_list'
            # print(my_data_list)
            id_list = []
            for line in my_data_list:
                entry = line.split(',')
                id_list.append(entry[0])  # Appends ID into 'id_list'
            if id not in id_list:  # To Check That if that ID's Attendance already Marked
                now = datetime.now()
                date = now.strftime('%d-%m-%Y')
                time = now.strftime('%H:%M:%S')
                f.writelines(f'\n{id},{name},{date},{time}')  # Marks Attendance (Writes Line in CSV File)
                print(f'Attendance Marked Successfully of ID: {id}   Name: {name}')

    # FOR CAPTURING SCREEN RATHER THAN WEBCAM
    # def captureScreen(bbox=(300,300,690+300,530+300)):
    #     capScr = np.array(ImageGrab.grab(bbox))
    #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    #     return capScr

    encode_list_known = find_encodings(images)
    print('Encoding Complete')

    print('Opening WebCam...')
    cap = cv2.VideoCapture(0)  # Video capture source camera (Here webcam of laptop)

    while True:
        success, img = cap.read()  # Return a single frame in variable `frame`
        # img = captureScreen()
        img_s = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Resize image into its 4th size (1/4)
        img_s = cv2.cvtColor(img_s, cv2.COLOR_BGR2RGB)  # Convert Image Color From BGR to RGB

        faces_cur_frame = face_recognition.face_locations(img_s)  # Getting Face Locations

        # Getting Face Encodings from Resized Image with Face Locations
        encodes_cur_frame = face_recognition.face_encodings(img_s, faces_cur_frame)

        # print(encodes_cur_frame);

        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):  # Using both Arrays for 'For Loop'

            # 'matches' get True or False Value after comparing known Face Encoding and Current Face Encoding
            matches = face_recognition.compare_faces(encode_list_known, encodeFace)

            # 'face_dis' get  Distance value which is difference between known Face Encoding and Current Face Encoding
            # (The lower is distance is, the more the face is matched)
            face_dis = face_recognition.face_distance(encode_list_known, encodeFace)

            # print(face_dis)
            match_index = np.argmin(face_dis)  # Stores the Index of Minimum Value(which is Distance) in 'match_index'

            if face_dis[match_index] < 0.50:  # If the lowest distance is less than 0.5 then marks attendance
                id = class_id[match_index]
                name = class_names[match_index]
                save_attendance(id, name)
            else:
                id = 'Unknown'  # If the lowest distance is even more than 0.5 then the face is Unknown
            # print(id)
            y1, x2, y2, x1 = faceLoc  # right, bottom, left, top

            # Multiplying by 4 because the image was reduced/resized by 4
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            # top, right, bottom, left  #Drawing Rectangle with face-locations #color is (0,255,0) and thickness is 2
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Other rectangle which is used as background for text(which is ID)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)

            # To Put Text inside second Rectangle
            cv2.putText(img, id, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('Webcam', img)  # Shows that 'img'(Image) in new window named WebCam
        # cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit on Pressing 'q'
            cv2.destroyAllWindows()
            break

    cap.release()
    print('WebCam Closed.')
