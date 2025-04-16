import unittest 
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector(self):
        emotion1 = emotion_detector('I am glad this happened')['dominant_emotion']
        self.assertEqual(emotion1,'joy')

        emotion2 = emotion_detector('I am really mad about this')['dominant_emotion']
        self.assertEqual(emotion2,'anger')

        emotion3 = emotion_detector('I feel disgusted just hearing about this')['dominant_emotion']
        self.assertEqual(emotion3,'disgust')

        emotion4 = emotion_detector('I am so sad about this')['dominant_emotion']
        self.assertEqual(emotion4,'sadness')

        emotion5 = emotion_detector('I am really afraid that this will happen')['dominant_emotion']
        self.assertEqual(emotion5,'fear')

if __name__ == "__main__":

    unittest.main()