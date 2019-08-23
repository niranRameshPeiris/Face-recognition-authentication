import face_recognition
from PIL import Image,ImageDraw

obama_image = face_recognition.load_image_file("./known/obama-known.jpg")
shehan_image = face_recognition.load_image_file("./known/shehan-known.jpeg")

obama_encoding = face_recognition.face_encodings(obama_image)[0]
shehan_encoding = face_recognition.face_encodings(shehan_image)[0]

known_face_encodings = [
    obama_encoding,
    shehan_encoding
]

known_face_names = [
    "Obama",
    "Shehan"
]

test_image = face_recognition.load_image_file('./unknown/shehan-unknown.jpeg')

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches =  face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    text_with, text_height = draw.textsize(name)

    draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))

    draw.text((left+6, bottom - text_height -5), name, fill=(255,255,255,255))

del draw

pil_image.show()