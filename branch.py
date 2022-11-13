class Branch(object):
    def __init__(self, starting_node, ending_node, voltage_source=0, current_source=0, resistance=0):
        self.starting_node = starting_node
        self.ending_node = ending_node
        self.voltage_source = voltage_source
        self.current_source = current_source
        self.resistance = resistance

    def __str__(self):
        return 'Branch: Starting node: ' + str(self.starting_node) + ' ,Ending node: ' + str(self.ending_node)
