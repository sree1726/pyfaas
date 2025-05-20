from cloudevents.http import CloudEvent
import unittest
 
func = __import__("func")
 
class TestFunc(unittest.TestCase):
    def test_func(self):
        attributes = {
            "type": "dev.knative.function",
            "source": "https://knative.dev/python.event",
        }
        data = {"otp": "77878787"}
        event = CloudEvent(attributes, data)
 
        result = func.main(event)
        self.assertEqual(result, {"status": "OTP processed"})
 
if __name__ == "__main__":
    unittest.main()