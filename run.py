#from flight_parent_class import *
#from people_class import *
from passenger_class import *

# Passenger section
passanger1 = Passenger("EK456", "Dubai", "London", "12:00", "Pass741", "Miles","Eastwood","Board123")
passanger2 = Passenger("EK787", "Ibiza", "UK", "16:00", "Pass333", "Sam","Forestter","Board321")
passanger3 = Passenger("EK456", "Dubai", "London", "12:00", "Pass783", "Jack", "Wallace", "Board356")
passanger4 = Passenger("EK456", "Dubai", "London", "12:00", "Pass020", "Katie", "Mackenzie", "Board466")
passanger5 = Passenger("EK787", "Ibiza", "UK", "16:00", "Pass111", "Anthony", "Moorcroft", "Board797")
passanger6 = Passenger("EK787", "Ibiza", "UK", "16:00", "Pass999", "Sebastian", "Hill", "Board963")


# Flight section
flight1 = Flight("EK456", "Dubai", "London","12:00",)
flight2 = Flight('EK787',"Ibiza", "UK", "16:00")

# Section for adding passengers to a flight
## Flight 1 section
flight1.add_passanger(passanger1)
flight1.add_passanger(passanger3)
flight1.add_passanger(passanger4)

## Flight 2 section
flight2.add_passanger(passanger2)
flight2.add_passanger(passanger5)
flight2.add_passanger(passanger6)


list_of_flights =  [flight1,flight2]
capacity = 0
print('Welcome to London Gatwick International Airport! ' )
for flight in list_of_flights:
     if flight_num == 1:

    passangers = flight1.getPassenger_list()


    print(passangers)

    # for passanger in passangers:
    #
    #     print(passanger)


# print(list_of_flights[1])
# print(flight1.passenger_list[1])

# for flight in list_of_flights:
#     print(flight.getPassenger_list())


