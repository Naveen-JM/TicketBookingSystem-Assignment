class Event:
    def __init__(self, event_id, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, booking_id):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_id = venue_id
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
        self.booking_id = booking_id
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value

    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, value):
        self._event_date = value

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value

    @property
    def venue_id(self):
        return self._venue_id

    @venue_id.setter
    def venue_id(self, value):
        self._venue_id = value

    @property
    def total_seats(self):
        return self._total_seats

    @total_seats.setter
    def total_seats(self, value):
        self._total_seats = value

    @property
    def available_seats(self):
        return self._available_seats

    @available_seats.setter
    def available_seats(self, value):
        self._available_seats = value

    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        self._ticket_price = value

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value

    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, value):
        self._booking_id = value


