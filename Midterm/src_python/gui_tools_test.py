import unittest
import gui_tools

class MyTestCase(unittest.TestCase):
    def test_validate_positive_float(self):
        test_true_strings = ["100", "1234", "1.0", "2.0", "2.", ".1", "0.1"]
        test_false_strings = ["-100", "-1234", "-1.0", "-2..0", "2..0", "", " ", "-.1", " 1", " .1", " 0.1", " -1.0"]

        for item in test_true_strings:
            self.assertTrue(gui_tools.validate_positive_float_input(item), msg="Failed string: " + item)

        for item in test_false_strings:
            self.assertFalse(gui_tools.validate_positive_float_input(item), msg="Failed string: " + item)

if __name__ == '__main__':
    unittest.main()
