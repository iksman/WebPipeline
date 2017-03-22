class MockAssignment:
  def __init__(self):
    self.data = [["koek","kaak"]]
    self.name = "testcab1"
    self.description = ["test1","test2"]

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

class MockInjector:
  def __init__(self):
    self.module = MockDispenser()
  def getModule(self):
    return self.module