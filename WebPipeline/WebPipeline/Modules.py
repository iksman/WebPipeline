import mockeries
class Module:
  def __init__(self,name,data,description):
    self.data = data
    self.name = name
    self.description = description
  def find(self,name):
    for item in self.data:
      if item.name == name:
        return item
    return False

class Assignment:
  def __init__(self,data,name,desc):
    self.data = data
    self.name = name
    self.description = desc

class ModuleDispenser:
  def __init__(self):
    self.module = []
  def add(self,module):
    self.module += [module]
  def find(self,name):
    for item in self.module:
      if item.name == name:
        return item
    return False

class Grader:
  def __init__(self,injector):
    self.injector = injector

  def grade(self,cur,inp):
    #print(cur)
    if self.injector.getModule().find(cur[0]).find(cur[1]).data[cur[2]][1].lower() == inp.lower():
      return True
    else:
      return False

class Injector: #Allows mockdispensers to go into flask
  def __init__(self,Module):
    self.module = Module
  def overrideModule(self,Module):
    self.module = Module
  def getModule(self):
    return self.module


#Put your assignments here
A1Vocab1 = Assignment(
  [["book","boek"],
   ["egg","ei"],
   ["football","voetbal"],
   ["box","doos"],
   ["photograph","foto"],
   ["newspaper","krant"],
   ["chocolate","chocolade"],
   ["card","kaart"],
   ["cupboard","kast"],
   ["beach","strand"],
   ["police","politie"],
   ["pig","varken"],
   ["cup","beker"]],

   "vocab 1", 
   ["English","Dutch"])

A1Grammar1 = Assignment(
  [["The lost fish _____[zijn] found yesterday","was"],
   ["In december, I skip town to ____[bezoeken] my nephew.","visit"],
   ["My nickname used to be Beefboy, nowadays it ____[zijn] Teflon","is"]],
   
   "grammar 1",
   ["Sentence with dutch hint","Word"])

#A2
A2Vocab1 = Assignment(
  [["singular","enkel"],
   ["introduction","introductie"],
   ["chemicals","chemicaliën"],
   ["business card","visitekaartje"],
   ["clothing iron","strijkbout"],
   ["leek","prei"],
   ["starch","zetmeel"],
   ["banknotes","briefgeld"],
   ["departmentstore","warenhuis"],
   ["lighter","aansteker"],
   ["savory","hartig"],
   ["lump","brok"]],

   "vocab 1", 
   ["English","Dutch"])

A2Grammar1 = Assignment(
  [["In the old times, we ____[gewend om] roam the lands of winter.","used to"],
   ["Your hair looks bad, but mine looks ____[slechter]","worse"],
   ["A delightful summer's eve is all I've ever ____[willen]","wanted"]],
   
   "grammar 1",
   ["Sentence with dutch hint","Word"])

#Assignment implementation ends here
#Module creation begins here

modules = ModuleDispenser()#[A1Vocab1,A1Grammar1]
modules.add(Module("A1",[A1Vocab1,A1Grammar1],"Entry level assignments, essentials of the english language. Assignments of this level include vocabulary and grammar exercises"))
modules.add(Module("A2",[A2Vocab1, A2Grammar1],"Intermediate level assignments for the experienced english language practicioner. Assignments of this level include: vocabulary and grammar exercises"))
#Module creation ends here

#print(modules.find("test").name)

injector = Injector(modules)
#injector.overrideModule(mockeries.MockDispenser())
grader = Grader(injector)
