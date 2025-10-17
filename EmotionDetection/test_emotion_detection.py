from emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def _test_emotion(self, statement: str, expected_dominant_emotion: str):
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_detection(self):
        self._test_emotion("I am glad this happened", "joy")
        self._test_emotion("I am really mad about this", "anger")
        self._test_emotion("I feel disgusted just hearing about this", "disgust")
        self._test_emotion("I am so sad about this", "sadness")
        self._test_emotion("I am really afraid that this will happen", "fear")

unittest.main()
