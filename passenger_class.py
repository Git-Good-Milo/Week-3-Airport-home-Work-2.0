#from flight_parent_class import *
from people_class import *
class Passenger(People):

    def __init__(self, flight_number, destination, origin, time, pass_port_num,f_name, l_name, boarding_num):
        super().__init__(flight_number, destination, origin, time, pass_port_num,  f_name, l_name)
        self.f_name = f_name
        self.l_name = l_name
        self.ticket_num = boarding_num


    def show(self):
        print(self.f_name,self.l_name,self.ticket_num)


    def getF_name(self):
        return self.f_name

    def get_lastname(self):
        return self.l_name
    def get_ticketnum(self):
        return self.ticket_num

