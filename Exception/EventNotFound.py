class EventNotFoundException(Exception):
    def __init__(self, event_id):
        super().__init__(f"Event with ID {event_id} is not listed in the menu.")
        self.event_id = event_id