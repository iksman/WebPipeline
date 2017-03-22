import unittest
from flask import Flask
from WebPipeline import *
from mockeries import *

class Unittest_Dispenser(unittest.TestCase):
  def setUp(self):
    self.dispenser = Modules.ModuleDispenser()
    
  def test_add(self):
    self.dispenser.add(MockModule())
    self.assertEqual(self.dispenser.module[0].name, "test")

  def test_find_rightValue(self):
    self.dispenser.add(MockModule())
    self.assertEqual(self.dispenser.find("test"), self.dispenser.module[0])

  def test_find_wrongValue(self):
    self.dispenser.add(MockModule())
    self.assertEqual(self.dispenser.find("sest"), False)
 
class Unittest_Module(unittest.TestCase):
  def setUp(self):
    self.module = Modules.Module("testmodule",[MockAssignment()],"testdescription")
  
  def test_find(self):
    self.assertEqual(self.module.find("testcab1").name,"testcab1")

  def test_find_wrongValue(self):
    self.assertNotEqual(self.module.find("testcab1").name,"Verkeerde value")


class Unittest_Grader(unittest.TestCase):
  def setUp(self):
    self.module = Modules.Grader(MockInjector())
  
  def test_find(self):
    self.assertTrue(self.module.grade(["test","testcab1",0],"kaak"))

  def test_find_wrongValue(self):
    self.assertFalse(self.module.grade(["test","testcab1",0],"Verkeerde value"))

class Unittest_flask(unittest.TestCase):
  def setUp(self):
    Modules.injector.overrideModule(MockDispenser())
    self.app = app.test_client()
    self.app.testing = True

  def test_homepage_load(self):
      result = self.app.get('/')
      self.assertEqual(result.status_code,200)

  def test_correctmodule_load(self):
      result = self.app.get('/module/test')
      self.assertEqual(result.status_code,200)

  def test_wrongmodule_load(self):
      result = self.app.get('/module/Verkeerde value')
      self.assertNotEqual(result.status_code,200)

if __name__ == '__main__':
  unittest.main()


  
