"""
Test for file utils/video.py
"""

import sys
sys.path.append('..')

import unittest
from utils.video import get_extension


class TestVideo(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.path = '~/Vídeos/video.mp4'


    def tearDown(self):
        print('tearDown')


    def test_get_extension(self):
        """
        Test for when getting
        the extension
        """

        print('Test get_extension')

        expeted = 'mp4'
        extension = get_extension(self.path)
        self.assertEqual(expeted, extension)


        extension = get_extension('~/Vídeos/other.mp4')
        self.assertEqual(expeted, extension)



if __name__ == '__main__':
    unittest.main()
