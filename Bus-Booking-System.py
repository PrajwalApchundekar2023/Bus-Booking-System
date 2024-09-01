# BUS TICKET BOOKING SYSTEM :
# Creating classes of # Bus
                                 # Road
                                 # Booking
                                 # main()


class Bus:
    #for assinging the bus details
    
    def __init__(self, bus_number, capacity):
        self.bus_number = bus_number
        self.capacity = capacity
        self.road = None

    def assign_road(self, road):
        self.road = road

    def __str__(self):
        road_info = f"Road: {self.road.road_name}" if self.road else "No road assigned"
        return f"Bus Number: {self.bus_number}, Capacity: {self.capacity}, {road_info}"



class Road:
    # For assigning road details
    
    def __init__(self, road_name, stops):
        self.road_name = road_name
        self.stops = stops

    def __str__(self):
        return f"Road: {self.road_name}, Stops: {', '.join(self.stops)}";


class Booking:

    # For bboking details and about the bus and road and passenger and passengers seat

    def __init__(self, booking_id, bus,passenger_name,seat_num):

        self.booking_id=booking_id;
        self.bus=bus;
        self.passenger_name=passenger_name;
        self.seat_num=seat_num;

    def __str__(self):
        return f"Booking ID : {self.booking_id}\n Bus : {self.bus}\n Passenger Name : {self.passenger_name}\n Seat Number : {self.seat_num}"; 


def main():

    buses=[];
    roads=[];
    bookings=[];
    booking_id_counter=1;

    while True:
        print("\n--------Bus Booking System-------")
        print("1. Add Bus")
        print("2. View Buses")
        print("3. Add Road")
        print("4. View Roads")
        print("5. Assign Road to Bus")
        print("6. Create Booking")
        print("7. View Bookings")
        print("8. Exit")

        choice = input("\nEnter your choice: ");

        if choice == '1':
            bus_number = input("Enter Bus Number: ")
            capacity = int(input("Enter Bus Capacity: "))
            buses.append(Bus(bus_number, capacity))
            print("Bus added successfully......")

        elif choice == '2':
            if not buses:
                print("No buses found.")
            else:
                for bus in buses:
                    print(bus)

        elif choice == '3':
            road_name = input("Enter Road Name: ")
            stops = input("Enter Stops (comma separated): ").split(',')
            roads.append(Road(road_name.strip(), [stop.strip() for stop in stops]))
            print("Road added successfully......")

        elif choice == '4':
            if not roads:
                print("No routes found.")
            else:
                for road in roads:
                    print(road)

        elif choice == '5':
            bus_number = input("Enter Bus Number: ")
            road_name = input("Enter Road Name: ")
            bus = next((bus for bus in buses if bus.bus_number == bus_number), None)
            road = next((road for road in roads if road.road_name == road_name), None)
            if bus and road:
                bus.assign_road(road)
                print("Road assigned to bus successfully.....")
            else:
                print("Bus or Road not found.")


        elif choice == '6':
            bus_number = input("Enter Bus Number: ")
            passenger_name = input("Enter Passenger Name: ")
            seat_num = int(input("Enter Seat Number: "))
            bus = next((bus for bus in buses if bus.bus_number == bus_number), None);

            if bus and bus.road:
                if seat_num > bus.capacity:
                    print("Invalid seat number.")
                elif any(booking.bus == bus and booking.seat_num == seat_num for booking in bookings):
                    print("Seat already booked.")
                else:
                    bookings.append(Booking(booking_id_counter, bus, passenger_name, seat_num))
                    booking_id_counter += 1
                    print("Booking created successfully!")
            else:
                print("Bus not found or not assigned to a route.......sry")
                
        elif choice == '7':
            if not bookings:
                print("No bookings found.")
            else:
                for booking in bookings:
                    print(booking)

        elif choice == '8':
            print("Thank You for visiting.....system")
            break
        
        else:
            print("Invalid choice, please try again......")


if __name__ == "__main__":
    main()

        
    

                    
            

            
        

        

     






                                 
