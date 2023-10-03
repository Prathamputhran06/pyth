class electronics:
    analog='ac'
    digital='dc'
    def __init__(self,power,efficiency):
        self.power=power
        self.efficiency=efficiency
    def dlj(self):
        print(self.analog,self.efficiency)
transistor=electronics(100,7)
resistor=electronics(200,50)
transistor.dlj()
resistor.dlj()
