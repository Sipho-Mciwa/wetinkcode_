import unittest
import world.text.world

class MyTestCases(unittest.TestCase):

    """def test_show_position(self):
        position_x = 0
        position_y = 0
        robot_name = "HAL"
        self.assertEqual(world.text.world.show_position(robot_name), ' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    """
    def test_is_position_allowed_invalid_X(self):
        self.assertFalse(world.text.world.is_position_allowed(-101, 55))

    def test_is_position_allowed_invalid_Y(self):
        self.assertFalse(world.text.world.is_position_allowed(-10, 255))

    def test_is_position_allowed_valid_X_and_Y(self):
        self.assertTrue(world.text.world.is_position_allowed(10, 25))

    def test_do_forward_valid(self):
        steps = 15
        robot_name = "HAL"
        self.assertEqual(world.text.world.do_forward(robot_name, steps), (True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'))
    
    def test_do_forward_invalid(self):
        steps = 215
        robot_name = "HAL"
        self.assertEqual(world.text.world.do_forward(robot_name, steps), (True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'))
    
    def test_do_back_valid(self):
        steps = 10
        robot_name = "HAL"
        self.assertEqual(world.text.world.do_back(robot_name, steps), (True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'))
    
    def test_do_back_invalid(self):
        steps = 250
        robot_name = "HAL"
        self.assertEqual(world.text.world.do_back(robot_name, steps), (True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'))

    def test_do_right_turn(self):
        robot_name = "HAL"
        self.assertEqual(world.text.world.do_right_turn(robot_name), (True, ' > '+robot_name+' turned right.'))

    def test_do_left_turn(self):
        robot_name = "HAL"
        self.assertEqual(world.text.world.do_left_turn(robot_name), (True, ' > '+robot_name+' turned left.'))
    
    

if __name__ == "__main__":
    unittest.main()