from abc import ABC, abstractmethod
from Entity.venue import Venue

class IEventServiceProviderRepository(ABC):
    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: str, venue: str) -> bool:
        pass
    @abstractmethod
    def delete_event(self, event_id) -> bool:
        pass
    @abstractmethod
    def get_event_details(self, event_id) -> dict:
        pass
    @abstractmethod
    def get_available_no_of_tickets(self, event_id) -> int:
        pass
    @abstractmethod
    def get_all_events(self) -> list:
        pass

