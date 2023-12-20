from event_service_provider_impl import EventServiceProviderImpl
from booking_system_service_provider import IBookingSystemServiceProvider

class BookingSystemServiceProviderImpl(EventServiceProviderImpl, IBookingSystemServiceProvider):
    def __init__(self, event_manager):
        super().__init__(event_manager)
        # Add additional attributes specific to BookingSystemServiceProviderImpl if needed

    def create_event(self, event):
        event_id = super().create_event(event)  # Use the create_event method from the base class
        # Add additional logic specific to booking system event creation
        print(f"Event created successfully. Event ID: {event_id}")
        return event_id

    def book_tickets(self, event_id, num_tickets):
        event = super().get_event_details(event_id)  # Use the get_event_details method from the base class
        if event:
            available_seats = event.get("available_seats", 0)
            if available_seats >= num_tickets:
                # Deduct booked tickets from available seats
                self.event_manager.update_available_seats(event_id, available_seats - num_tickets)
                print(f"Successfully booked {num_tickets} tickets for Event ID {event_id}")
                return True
            else:
                print(f"Not enough available seats for booking {num_tickets} tickets.")
        else:
            print(f"Event with ID {event_id} not found.")
        return False

    def cancel_tickets(self, event_id, num_tickets):
        event = super().get_event_details(event_id)  # Use the get_event_details method from the base class
        if event:
            booked_seats = event.get("booked_seats", 0)
            if booked_seats >= num_tickets:
                # Add canceled tickets back to available seats
                self.event_manager.update_available_seats(event_id, event["available_seats"] + num_tickets)
                print(f"Successfully canceled {num_tickets} tickets for Event ID {event_id}")
                return True
            else:
                print(f"Not enough booked seats to cancel {num_tickets} tickets.")
        else:
            print(f"Event with ID {event_id} not found.")
        return False

    def get_available_seats(self, event_id):
        event = super().get_event_details(event_id)  # Use the get_event_details method from the base class
        if event:
            available_seats = event.get("available_seats", 0)
            print(f"Available seats for Event ID {event_id}: {available_seats}")
            return available_seats
        else:
            print(f"Event with ID {event_id} not found.")
            return 0

    def get_event_details(self, event_id):
        event = super().get_event_details(event_id)  # Use the get_event_details method from the base class
        if event:
            print(f"Event Details for Event ID {event_id}:\n{event}")
        else:
            print(f"Event with ID {event_id} not found.")

# Usage Example
if __name__ == "__main__":
    from EventServiceProviderimpl import EventManagementImpl  # Replace with your actual implementation class

    event_manager = EventManagementImpl()
    booking_system_provider = BookingSystemServiceProviderImpl(event_manager)

    # Create an event
    event_data = {"name": "Concert", "date": "2023-12-31", "available_seats": 100}
    event_id = booking_system_provider.create_event(event_data)

    # Book tickets
    booking_system_provider.book_tickets(event_id, 5)

    # Get available seats
    booking_system_provider.get_available_seats(event_id)

    # Cancel tickets
    booking_system_provider.cancel_tickets(event_id, 3)

    # Get event details
    booking_system_provider.get_event_details(event_id)
