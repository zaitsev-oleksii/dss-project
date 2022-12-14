from flask import Flask, request
from flask_cors import CORS
import PIL
from services.classifier import Classifier
from config import ALLOWED_MIME_TYPES

app = Flask(__name__)
CORS(app)

clf = Classifier()


def validate_file_types(files):
    filetypes = map(lambda file: file.content_type in ALLOWED_MIME_TYPES, files)
    return all(filetypes)


@app.route("/classify", methods=['POST'])
def classify():
    files = request.files.getlist('images')
    if not validate_file_types(files):
        return {'error': 'Wrong file types: only JPEG and PNG allowed'}, 400
    filenames = map(lambda file: file.filename, files)
    images = map(lambda img: PIL.Image.open(img), files)
    predictions = clf.predict(images)
    return dict(zip(filenames, predictions))
