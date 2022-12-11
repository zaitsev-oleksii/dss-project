from flask import Flask, request
from werkzeug.utils import secure_filename
import PIL
from services.classifier import Classifier

app = Flask(__name__)

clf = Classifier()


@app.route("/classify", methods=['POST'])
def classify():
    files = request.files.getlist('images')
    filenames = map(lambda file: secure_filename(file.filename), files)
    images = map(lambda img: PIL.Image.open(img), files)
    predictions = clf.predict(images)
    return dict(zip(filenames, predictions))
