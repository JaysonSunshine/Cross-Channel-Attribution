import unittest

from event_data import Event

def fileToString(filename):
	with open(filename, 'rb') as f:
		return f.read()

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Event('test/test1').deviceChannelPaths(), fileToString('test/output1'))
        self.assertEqual(Event('test/test1').commonPaths(), fileToString('test/output2'))
        self.assertEqual(Event('test/test1').userChannelPaths(), fileToString('test/output3'))
        self.assertEqual(Event('test/test2').deviceChannelPaths(), fileToString('test/output4'))
        self.assertEqual(Event('test/test2').commonPaths(), fileToString('test/output5'))
        self.assertEqual(Event('test/test2').userChannelPaths(), fileToString('test/output6'))

unittest.main()