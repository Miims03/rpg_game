import unittest

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

from view.authentication_view import *

class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Create a single QApplication instance for the entire test suite
        if not QApplication.instance():
            self.app = QApplication()

    @classmethod
    def tearDownClass(self):
        # Destroy the QApplication instance after all tests are completed
        if QApplication.instance():
            self.app.exit()

    def setUp(self):
        
        self.dialog = AuthenticationView()
        self.dialog.start_button.clicked.connect(self.montring)

    def montring(self):
        print('icimdr')

    def test_view_player(self):
        self.dialog.show()
        self.app.exec()

if __name__ == '__main__':
    unittest.main()