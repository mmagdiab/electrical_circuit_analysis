class Branch(object):
    def __init__(self, sequence, starting_node, ending_node, voltage_source=0, current_source=0, resistance=0):
        self.sequence = int(sequence)
        self.starting_node = int(starting_node)
        self.ending_node = int(ending_node)
        self.voltage_source = int(voltage_source)
        self.current_source = int(current_source)
        self.resistance = int(resistance)

    def __str__(self):
        return 'Branch ' + chr(65+self.sequence) + ': ' +\
               'Starting node: ' + str(self.starting_node) +\
               ' ,Ending node: ' + str(self.ending_node) + \
               ' ,Voltage Source: ' + str(self.voltage_source) + \
               ' ,Current Source: ' + str(self.current_source) + \
               ' ,Resistance: ' + str(self.resistance)


