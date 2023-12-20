class Customer:
    def __init__(self, customer_id, customer_name, email, phone_number, booking_id):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number
        self.booking_id = booking_id

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, value):
        self._booking_id = value