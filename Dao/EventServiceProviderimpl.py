from Entity.venue import Venue

class EventServiceProviderRepositoryImpl(IEventServiceProviderRepository):
    def __init__(self):
        # For simplicity, using a dictionary to store events
        self.events_dict = {}

    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: str, venue: Venue) -> bool:
        """
        Create a new event.
        """
        # Generate a unique event ID (you might want to use a more robust method in a real application)
        event_id = len(self.events_dict) + 1

        # Create the event dictionary
        event_details = {
            "event_name": event_name,
            "date": date,
            "time": time,
            "total_seats": total_seats,
            "available_seats": total_seats,
            "ticket_price": ticket_price,
            "event_type": event_type,
            "venue": venue,
        }

        # Add the event to the dictionary with the event ID as the key
        self.events_dict[event_id] = event_details

        return True

    def delete_event(self, event_id) -> bool:
        """
        Delete an event.
        """
        if event_id in self.events_dict:
            del self.events_dict[event_id]
            return True
        return False

    def get_event_details(self, event_id) -> dict:
        """
        Get details of a specific event.
        """
        return self.events_dict.get(event_id, {})

    def get_available_no_of_tickets(self, event_id) -> int:
        """
        Get the available number of tickets for a specific event.
        """
        event_details = self.get_event_details(event_id)
        if event_details:
            return event_details.get("available_seats", 0)
        return 0

    def get_all_events(self) -> list:
        """
        Get details of all events.
        """
        return list(self.events_dict.values())
