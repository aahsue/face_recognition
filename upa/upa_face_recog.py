import face_recognition
import cv2
import sys
tolerance = sys.argv[1]

# upa face recognition program
# user andrea

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.

import os
import time

imagesKnownEncodings = []
imagesKnownNames = []
attendance = []
start = time.time()

runTime = (int)(input("How long would you like to take attendance for? (in minutes) "))
runTime *= 60

print("\nExpected students:")
for root, dirs, files in os.walk("./images"):
    for filename in files:
        theFilename = filename.replace("_"," ")
        theFilename = theFilename.title()
        print("\t" + theFilename[0:len(theFilename)-4])
        imageLoaded = face_recognition.load_image_file("./images/" + filename)
        try:
            imageEncode = face_recognition.face_encodings(imageLoaded)[0]
            imagesKnownEncodings.append(imageEncode)
            imagesKnownNames.append(theFilename[0:len(theFilename)-4])
        except:
            print ("error with " + filename)
    
print("\nDetecting faces...")

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
        matches = face_recognition.compare_faces(imagesKnownEncodings, face_encoding, float(tolerance))

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = imagesKnownNames[first_match_index]
            personInArray = False
            for x in attendance:
                if (name == x):
                    personInArray = True

            if (personInArray == False):
                print ("\t"+ name)
                attendance.append(name)

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
    if time.time() > start + runTime : break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

print("\nAttendance Record")
print("People present: ")
for x in attendance:
    print("\t" + x)
print("People absent: ")
for x in imagesKnownNames:
    if x not in attendance:
        print("\t" + x)
