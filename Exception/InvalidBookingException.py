class InvalidBookingIDException(Exception):
    def __init__(self, booking_id):
        super().__init__(f"Invalid Booking ID {booking_id} entered.")
        self.booking_id = booking_id