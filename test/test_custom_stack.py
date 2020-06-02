from basic_data_structures.stack_queues.custom_stack import CustomStack
import unittest
# run with: python -m unittest test.test_custom_stack


class TestCustomStack(unittest.TestCase):
    """Testing CustomStack class"""

    def setUp(self):
        self.custom_stack = CustomStack()
        self.custom_stack.push(1)
        
    def test_push(self):
        self.custom_stack.push(2)
        self.assertEqual(self.custom_stack.peek(), 2)
        self.assertNotEqual(self.custom_stack.peek(), 99)
        
    def test_peek(self):
        self.assertEqual(self.custom_stack.peek(), 1)
        self.assertNotEqual(self.custom_stack.peek(), 99)
       
    def test_pop(self):
        val = self.custom_stack.pop()
        self.assertEqual(val, 1)  
        self.assertNotEqual(val, 99)  
