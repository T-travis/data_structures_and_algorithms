from basic_data_structures.stack_queues.custom_queue import CustomQueue
import unittest 
# run with: python -m unittest test.test_custom_queue


class TestCustomQueue(unittest.TestCase):
    """Testing CustomQueue class"""
    
    def setUp(self):
        self.custom_queue = CustomQueue()
        self.custom_queue.enqueue(1)
        
    def test_enqueue(self):
        self.custom_queue.enqueue(2)
        self.assertEqual(self.custom_queue.peek(), 2)
        self.assertNotEqual(self.custom_queue.peek(), 99)
        
    def test_dequeue(self):
        val = self.custom_queue.dequeue()
        self.assertEqual(val, 1)
        self.assertNotEqual(val, 99)
        
    def test_peek(self):
        self.assertEqual(self.custom_queue.peek(), 1)
        self.assertNotEqual(self.custom_queue.peek(), 99)
