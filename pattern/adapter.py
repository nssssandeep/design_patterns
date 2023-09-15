class OldSystem:
    def old_method(self):
        print("Old System Method") # Assume it returns XML

class NewSystemInterface:
    def new_method(self): # returns json
        pass

class Adapter(NewSystemInterface):
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        self.old_system.old_method() # get Json from XML and return JSON

old_system = OldSystem()
adapter = Adapter(old_system)

adapter.new_method()  # This will call old_method from OldSystem, convert to JSON and return
