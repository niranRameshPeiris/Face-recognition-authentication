import face_recognition

#known data set
samudya_image = face_recognition.load_image_file("./known/known.jpg")

#encoding
samudya_encoding = face_recognition.face_encodings(samudya_image)[0]

#test cases
test_image1 = face_recognition.load_image_file("./unknown/1.jpg")
test_encoding1 = face_recognition.face_encodings(test_image1)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding1)
if result[0] == True:
    print("Matching 1")
else:
    print("Not Matching")

test_image2 = face_recognition.load_image_file("./unknown/2.jpg")
test_encoding2 = face_recognition.face_encodings(test_image2)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding2)
if result[0] == True:
    print("Matching 2")
else:
    print("Not Matching")

test_image3 = face_recognition.load_image_file("./unknown/3.jpg")
test_encoding3 = face_recognition.face_encodings(test_image3)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding3)
if result[0] == True:
    print("Matching 3")
else:
    print("Not Matching")

test_image4 = face_recognition.load_image_file("./unknown/4.jpg")
test_encoding4 = face_recognition.face_encodings(test_image4)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding4)
if result[0] == True:
    print("Matching 4")
else:
    print("Not Matching")

test_image5 = face_recognition.load_image_file("./unknown/5.jpg")
test_encoding5 = face_recognition.face_encodings(test_image5)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding5)
if result[0] == True:
    print("Matching 5")
else:
    print("Not Matching")

test_image6 = face_recognition.load_image_file("./unknown/6.jpg")
test_encoding6 = face_recognition.face_encodings(test_image6)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding6)
if result[0] == True:
    print("Matching 6")
else:
    print("Not Matching")

test_image7 = face_recognition.load_image_file("./unknown/7.jpg")
test_encoding7 = face_recognition.face_encodings(test_image7)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding7)
if result[0] == True:
    print("Matching 7")
else:
    print("Not Matching")

test_image8 = face_recognition.load_image_file("./unknown/8.jpg")
test_encoding8 = face_recognition.face_encodings(test_image8)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding8)
if result[0] == True:
    print("Matching 8")
else:
    print("Not Matching")

test_image9 = face_recognition.load_image_file("./unknown/9.jpg")
test_encoding9 = face_recognition.face_encodings(test_image9)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding9)
if result[0] == True:
    print("Matching 9")
else:
    print("Not Matching")

test_image10 = face_recognition.load_image_file("./unknown/10.jpg")
test_encoding10 = face_recognition.face_encodings(test_image10)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding10)
if result[0] == True:
    print("Matching 10")
else:
    print("Not Matching")

test_image11 = face_recognition.load_image_file("./unknown/11.jpg")
test_encoding11 = face_recognition.face_encodings(test_image11)[0]

result = face_recognition.compare_faces([samudya_encoding], test_encoding11)
if result[0] == True:
    print("Matching 11")
else:
    print("Not Matching")
