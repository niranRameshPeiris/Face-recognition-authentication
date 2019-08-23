import face_recognition
import sys

if len(sys.argv) < 2:
    print("No file specified !!")
else:
    #known data set
    obama_image = face_recognition.load_image_file("./known/obama-known.jpg")
    shehan_image = face_recognition.load_image_file("./known/shehan-known.jpeg")

    #encoding
    obama_encoding = face_recognition.face_encodings(obama_image)[0]
    shehan_encoding = face_recognition.face_encodings(shehan_image)[0]
    
    known_face_encodings = [
        obama_encoding,
        shehan_encoding
    ]
    #labels of the images
    known_face_names = [
        "Obama",
        "Shehan"
    ]

    #unknown image (from cmd argument one)
    test_image = face_recognition.load_image_file(sys.argv[1])
    test_encoding = face_recognition.face_encodings(test_image)[0]

    index = 0
    match = -1
    for image in known_face_encodings:
        result = face_recognition.compare_faces([image], test_encoding)
        if result[0] == True:
            match = index
        index += 1

    if match != -1:
        print(known_face_names[match])
    else:
        print("No user found !!")

