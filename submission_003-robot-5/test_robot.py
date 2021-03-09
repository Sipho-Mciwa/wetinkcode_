import unittest
import robot

class MyTestCases(unittest.TestCase):

    def test_split_command_input_fwd_10(self):
        command = "forward 10"
        self.assertEqual(robot.split_command_input(command), ("forward", '10'))

    def test_split_command_input_bck_5(self):
        command = "back 5"
        self.assertEqual(robot.split_command_input(command), ("back", '5'))
    
    def test_split_command_input_left(self):
        command = "left"
        self.assertEqual(robot.split_command_input(command), ("left", ''))

    def test_split_command_input_right(self):
        command = "right"
        self.assertEqual(robot.split_command_input(command), ("right", ''))

    def test_is_int_invalid(self):
        value = "five"
        self.assertFalse(robot.is_int(value))

    def test_is_int_string_int(self):
        value = "15"
        self.assertTrue(robot.is_int(value))
    
    def test_is_int_valid_fwd_10(self):
        value = 10
        self.assertTrue(robot.is_int(value))

    def test_is_valid_command_fwd_10(self):
        command = "ForWaRd 10"
        self.assertTrue(robot.valid_command(command))

    def test_is_valid_command_bck_5(self):
        command = "BaCk 5"
        self.assertTrue(robot.valid_command(command))

    def test_do_help(self):
        self.assertTupleEqual(robot.do_help(), (True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
MAZERUN - this command let's the robot figure out what commands to use to get to the top of the screen.
"""))


if __name__ == "__main__":
    unittest.main()