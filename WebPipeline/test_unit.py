import unittest
from WebPipeline import Modules

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
    self.module = Modules.Grader(MockDispenser())
  
  def test_find(self):
    self.assertTrue(self.module.grade(["test","testcab1",0],"kaak"))

  def test_find_wrongValue(self):
    self.assertFalse(self.module.grade(["test","testcab1",0],"Verkeerde value"))

if __name__ == '__main__':
  unittest.main()

class MockAssignment:
  def __init__(self):
    self.data = [["koek","kaak"]]
    self.name = "testcab1"
    self.desc = "testen"

class MockModule:
  def __init__(self):
    self.name = "test"
    self.data = [MockAssignment()]
    self.description = "testing"
  def find(self,name):
    if name == "testcab1":
      return self.data[0]
    else:
      return False

class MockDispenser:
  def __init__(self):
    self.module = [MockModule()]
  def add(self,module):
    pass
  def find(self,name):
    if name == "test":
      return self.module[0]
    else:
      return False
  
