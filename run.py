from flight_class import  *

from passenger_class import *

# Passenger section
passanger1 = Passenger("Miles","Eastwood","Board123")
passanger2 = Passenger("Sam","Forestter","Board321")
passanger3 = Passenger("Jack", "Wallace", "Board356")
passanger4 = Passenger("Katie", "Mackenzie", "Board466")
passanger5 = Passenger("Anthony", "Moorcroft", "Board797")
passanger6 = Passenger("Sebastian", "Hill", "Board963")


# Flight section
flight1 = Flight('EK454',"Turkey","UK","15:00")
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

print(flight1.getPassenger_list())


for flight in list_of_flights:
    passengers = flight.getPassenger_list()

    for passenger in passengers:
        print(passenger.show())
        # specific_passenger = passengers()
        # print(specific_passenger)

        #for passenger_details in passenger
