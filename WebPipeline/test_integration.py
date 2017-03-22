import unittest

from WebPipeline import *
from mockeries import *

class Test_integration(unittest.TestCase):
  def setUp(self):
    self.injector = Modules.injector
    self.name = self.injector.getModule().module[0].name
    self.assignment = self.injector.getModule().module[0].data[0].name
    self.app = app.test_client()
    self.app.secret_key = os.urandom(24)
    self.app.testing = True

  def test_homepage_load(self):
    result = self.app.get('/')
    self.assertEqual(result.status_code,200)

  def test_correctmodule_load(self):
    result = self.app.get('/module/' + self.name)
    self.assertEqual(result.status_code,200)

  def test_wrongmodule_load(self):
    result = self.app.get('/module/Verkeerde value')
    self.assertEqual(result.location,"http://localhost/404")

  def test_check_correctValue(self):
    result = self.app.get("/check/" + self.name + "/" + self.assignment)
    self.assertEqual(result.location,"http://localhost/assignment")

  def test_check_wrongModName(self):
    result = self.app.get("/check/Verkeerde value/testcab1")
    self.assertEqual(result.location,"http://localhost/404")

  def test_check_wrongAssName(self):
    result = self.app.get("/check/test/Verkeerde value")
    self.assertEqual(result.location,"http://localhost/404")

  def test_assignment(self):
    with self.app.session_transaction() as session:
      session['currentAssignment'] = [self.name,self.assignment,0]
    result = self.app.get("/assignment")
    self.assertEqual(result.status_code, 200)

  def test_assignment_wrongValue(self):
    with self.app.session_transaction() as session:
      session['currentAssignment'] = ["Verkeerde value","Verkeerde value",0]
    result = self.app.get("/assignment")
    self.assertEqual(result.location, "http://localhost/")

  def test_assignment_result(self):
    with self.app.session_transaction() as session:
      session['currentAssignment'] = [self.name,self.assignment,0]
    result = self.app.get("/assignment/True/kaak")
    self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
