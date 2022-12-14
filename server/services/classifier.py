import tensorflow as tf
from config import CLASS_LABELS, INPUT_SHAPE, MODEL_PATH

HEIGHT, WIDTH, CHANNELS = INPUT_SHAPE


class Classifier:
    def __init__(self):
        self.model = tf.keras.models.load_model(MODEL_PATH)

    def predict(self, images):
        tensors = map(lambda img: tf.convert_to_tensor(img), images)
        resized = map(lambda tensor: tf.image.resize(tensor, (HEIGHT, WIDTH)), tensors)
        scaled = map(lambda tensor: tf.divide(tensor, 255), resized)
        reshaped = map(lambda tensor: tf.reshape(tensor, (1, HEIGHT, WIDTH, CHANNELS)), scaled)
        batch = tf.concat([*reshaped], 0)
        predictions = self.model.predict(batch).tolist()
        labeled = map(lambda probs: dict(zip(CLASS_LABELS, probs)), predictions)
        return labeled
