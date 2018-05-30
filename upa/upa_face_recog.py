import face_recognition
import cv2

# upa face recognition program
# user andrea

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.

import os

imagesKnownEncodings = []
imagesKnownNames = []

for root, dirs, files in os.walk("./images"):
    for filename in files:
        print(filename)
        imageLoaded = face_recognition.load_image_file("./images/" + filename)
        imageEncode = face_recognition.face_encodings(imageLoaded)[0]
        imagesKnownEncodings.append(imageEncode)
        imagesKnownNames.append(filename[0:len(filename)-4])
        

#obama_image = face_recognition.load_image_file("images/obama.jpg")
#obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
#andrea_image = face_recognition.load_image_file("images/andrea.jpg")
#andrea_face_encoding = face_recognition.face_encodings(andrea_image)[0]
#ethan_image = face_recognition.load_image_file("images/ethan.jpg")
#ethan_face_encoding = face_recognition.face_encodings(ethan_image)[0]
#dany_image = face_recognition.load_image_file("images/dany.jpg")
#dany_face_encoding = face_recognition.face_encodings(dany_image)[0]

# Load a second sample picture and learn how to recognize it.
#biden_image = face_recognition.load_image_file("images/biden.jpg")
#biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names

#known_face_encodings = [
  #  obama_face_encoding,
  #  biden_face_encoding,
  #  andrea_face_encoding,
  #  ethan_face_encoding,
  #  dany_face_encoding
#]
#known_face_names = [
 #   "Barack Obama",
 #   "Joe Biden" ,
 #   "Andrea",
 #   "Ethan",
 #   "Dany"
#]

faces_already_detected = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(imagesKnownEncodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = imagesKnownNames[first_match_index]
            personInArray = False
            for x in faces_already_detected:
                if (name == x):
                    personInArray = True

            if (personInArray == False):
                print ("Person detected: " + name)
                faces_already_detected.append(name)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()