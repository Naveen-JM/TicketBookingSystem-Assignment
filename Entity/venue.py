class Venue:
    def __init__(self, venue_id, venue_name, address):
        self._venue_id = venue_id
        self._venue_name = venue_name
        self._address = address

    @property
    def venue_id(self):
        return self._venue_id

    @venue_id.setter
    def venue_id(self, value):
        self._venue_id = value

    @property
    def venue_name(self):
        return self._venue_name

    @venue_name.setter
    def venue_name(self, value):
        self._venue_name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

