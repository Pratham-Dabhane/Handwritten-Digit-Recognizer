# test_app.py
import unittest
import tensorflow as tf
import os

class TestDigitModel(unittest.TestCase):
    def test_model_exists(self):
        self.assertTrue(os.path.exists("digit_model.h5"))

    def test_model_loads(self):
        model = tf.keras.models.load_model("digit_model.h5")
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
