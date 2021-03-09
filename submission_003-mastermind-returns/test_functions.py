import unittest
from unittest.mock import patch
import random
import mastermind
from io import StringIO


class MyTestCase(unittest.TestCase):

    def test_create_code(self):
        """
            This method test weather the code
            created by the CPU i 4-digit long
            and that the numbers in the code 
            are between 1 and 8.
        """
        for i in range(101):
            code = mastermind.create_code()
            self.assertEqual(len(code), 4)          #tests if the code is 4-digit long
            for k in range(len(code)):
                self.assertIn(code[k], range(1, 9)) #tests if the numbers in code are in range 1-8

    def test_check_correctness(self):
        """
            This method will get different
            inputs abd it will display a
            message based on those inputs.
        """
        correct_Position = [1,5,3,2,4]
        turns = 0
        for number in correct_Position:
            if number != 4:
                #check_correctness() should return False
                self.assertFalse(mastermind.check_correctness(number, turns))
                turns += 1
            else:
                #check_correctness() should return True
                self.assertTrue(mastermind.check_correctness(number, turns))
    
    @patch("sys.stdin", StringIO("123\n12345\n1234"))
    def test_get_answer_input(self):
        """
            This method tests get_answer_input()
            to see how it behave, when given 
            various inputs.
        """
        
        print()
        self.assertEqual(mastermind.get_answer_input(), "1234")

    @patch("sys.stdin", StringIO("2786\n8245\n6785\n1234"))   
    def test_take_turn(self):
        print()
        code = [1,2,3,4]
        self.assertEqual(mastermind.take_turn(code), (0, 1))
        self.assertEqual(mastermind.take_turn(code), (1, 1))
        self.assertEqual(mastermind.take_turn(code), (0, 0))
        self.assertEqual(mastermind.take_turn(code), (4, 0))



if __name__ == "__main__":
    unittest.main()