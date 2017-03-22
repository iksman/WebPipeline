import unittest

from WebPipeline import *
from mockeries import *

class Test_integration(unittest.TestCase):
    def setUp(self):
      WebPipeline.Modules.injector.overrideModule(MockDispenser())
      self.app = app.test_client()
      self.app.testing = True

    def test_A(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code,200)

if __name__ == '__main__':
    unittest.main()
