class Booking:
    def __init__(self, booking_id, customer_id, event_id, num_tickets, total_cost, booking_date):
        self._booking_id = booking_id
        self._customer_id = customer_id
        self._event_id = event_id
        self._num_tickets = num_tickets
        self._total_cost = total_cost
        self._booking_date = booking_date

    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, value):
        self._booking_id = value

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value

    @property
    def num_tickets(self):
        return self._num_tickets

    @num_tickets.setter
    def num_tickets(self, value):
        self._num_tickets = value

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, value):
        self._total_cost = value

    @property
    def booking_date(self):
        return self._booking_date

    @booking_date.setter
    def booking_date(self, value):
        self._booking_date = value