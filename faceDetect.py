import face_recognition
import mysql.connector
import sys

if len(sys.argv) < 2:
    print("No image specified !!")
else:
    #user list from database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mirror"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()

    #unknown image (from cmd argument one)
    #test_image = face_recognition.load_image_file(sys.argv[1])

    #test_image = face_recognition.load_image_file('./test/Niran.jpg')
    #test_image = face_recognition.load_image_file('./test/sachitha.jpeg')
    test_image = face_recognition.load_image_file('./test/samu.jpg')
    #test_image = face_recognition.load_image_file('./test/shehan.jpeg')

    test_encoding = face_recognition.face_encodings(test_image)[0]

    index = 0
    match = -1
    for image in myresult:
        known_image = face_recognition.load_image_file(image[2])
        known_encoding = face_recognition.face_encodings(known_image)[0]

        result = face_recognition.compare_faces([known_encoding], test_encoding)
        if result[0] == True:
            match = index
            break
        index += 1

    if match != -1:
        print(myresult[match][1])
    else:
        print("No user found !!")
