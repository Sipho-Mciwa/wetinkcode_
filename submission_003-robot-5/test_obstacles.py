import unittest
import maze.obstacles as obstacles

class MyTestCases(unittest.TestCase):

    def test_get_obstacles(self):
        self.assertIsInstance(obstacles.get_obstacles(), list, "This is not a list")
    

    def test_is_path_blocked_false(self):
        x1, x2 = 10, 20
        y1, y2 = 15, 25
        self.assertFalse(obstacles.is_path_blocked(x1,y1,x2,y2))


    def test_is_path_blocked_True(self):
        x1, x2 = 10, 10
        y1, y2 = 15, 15
        self.assertFalse(obstacles.is_path_blocked(x1,y1,x2,y2))

if __name__ == "__main__":
    unittest.main()