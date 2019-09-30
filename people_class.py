from flight_parent_class import *
class People(Flight):

    def __init__(self, flight_number, destination, origin, time, pass_port_num,  f_name, l_name):
        super().__init__(flight_number, destination, origin, time)
        self.f_name = f_name
        self.l_name = l_name
        self.pass_port = pass_port_num
