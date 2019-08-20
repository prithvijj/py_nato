import unittest
import py_nato

class TestNato(unittest.TestCase):

	# Test for valid input
	def test_valid_input(self):
		test_input_string = "abc"
		actual_value = py_nato.convert_str_to_nato(test_input_string)
		expected_value = "Alpha Bravo Charlie"
		self.assertEqual(expected_value, actual_value)

	# Test for no input
	def test_no_input(self):
		test_input_string = ""
		actual_value = py_nato.convert_str_to_nato(test_input_string)
		expected_value = ""
		self.assertEqual(expected_value, actual_value)


if __name__ == '__main__':
	unittest.main()