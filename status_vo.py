class StatusVo (object):
    def __init__(self):
        self._id=None
        self._slot_no = None
        self._vehicle_no = None
        self._color = None

        @property
        def id(self):
            self._id

        @id.setter
        def id(self, value):
            self._id = value


        @property
        def slot_no(self):
            self._slot_no

        @slot_no.setter
        def slot_no(self, value):
            self._slot_no = value

        @property
        def color(self):
            self._color

        @color.setter
        def color(self, value):
            self._color = value

        @property
        def vehicle_no(self):
            self._vehicle_no

        @vehicle_no.setter
        def vehicle_no(self, value):
            self._vehicle_no = value

    def serialize(self):
        d = dict()
        d['id'] = self._id
        d['slot_no'] = self._slot_no
        d['color'] = self._color
        d['vehicle_no'] = self._vehicle_no
        return d
