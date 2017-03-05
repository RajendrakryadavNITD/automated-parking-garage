import queries
from sqlalchemy.sql import text
from sqlalchemy import exc
from excel_reader import status_vo
from excel_reader.dal import dbcondao
class ParkingGarageDao(dbcondao.DbConDao):
    def checking_for_parking_space_availability(self):
        try:
            query = text(queries.Queries.checking_for_parking_space_availability)
            conn = super(ParkingGarageDao, self).getconnection()
            values = {'status': 0}
            result = conn.execute(query, values).fetchall()
            parking_slot_list = []
            for row in result:
                parking_slot = row['slotno']
                parking_slot_list.append(parking_slot)
            return parking_slot_list
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def create_parking_place(self, no_of_parking_slot):
        try:
            query = text(queries.Queries.create_parking_place)
            conn = super(ParkingGarageDao, self).getconnection()
            for value in range (no_of_parking_slot):
                values = {'slotno' :value+1}
                conn.execute(query, values)
        except exc.SQLAlchemyError:
            raise
        except:
            raise
    def get_a_parking_space(self,slot_id, vehicle_no, color):
        try:
            query = text(queries.Queries.get_a_parking_space)
            conn = super(ParkingGarageDao, self).getconnection()
            values = {'parkingslotid':slot_id, 'vehicleno': vehicle_no, 'color': color}
            conn.execute(query, values)
        except exc.SQLAlchemyError:
            raise
        except:
            raise



    def get_parking_slot_id_using_slot_no(self, slot_no):
        slot_id =None
        try:
            query = text(queries.Queries.get_parking_slot_id_using_slot_no)
            conn = super(ParkingGarageDao, self).getconnection()
            values = {'slotno' :int(slot_no)}
            result = conn.execute(query, values)
            for row in result:
                slot_id = row['id']
            return slot_id
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def update_parking_slot(self, slot_id):
        try:
            query = text(queries.Queries.update_parking_slot)
            conn = super(ParkingGarageDao, self).getconnection()
            values = {'status' : 1,'id': slot_id}
            conn.execute(query, values)
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def leaving_parking_slot(self, slot_no):
        try:
            query = text(queries.Queries.leaving_parking_slot)
            conn = super(ParkingGarageDao, self).getconnection()
            values = {'status': 0,'slotno': slot_no}
            conn.execute(query, values)
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def get_parking_garage_status(self):
        parking_garage_status_list = []
        try:
            query = text(queries.Queries.get_parking_garage_status)
            conn = super(ParkingGarageDao, self).getconnection()
            result = conn.execute(query)
            for row in result:
                parking_garage_status = status_vo.StatusVo()
                parking_garage_status.slot_no = row['slotno']
                parking_garage_status.vehicle_no = row['vehicleno']
                parking_garage_status.color = row['color']
                parking_garage_status_list.append(parking_garage_status)
            return parking_garage_status_list

        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def get_registration_numbers_of_cars_with_color(self, color_of_car):
        registration_number_list = []
        try:
            query = text(queries.Queries.get_registration_numbers_of_cars_with_color)
            conn = super(ParkingGarageDao, self).getconnection()
            values = {'color': color_of_car}
            result = conn.execute(query, values)
            for row in result:
                registration_no = row['vehicleno']
                registration_number_list.append(registration_no)
            return registration_number_list
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def get_slots_for_cars_with_color(self, color_of_car):
        slot_number_list = []
        try:
            query = text(queries.Queries.get_slots_for_cars_with_color)
            conn = super(ParkingGarageDao, self).getconnection()
            values = {'color': color_of_car}
            result = conn.execute(query, values)
            for row in result:
                slot_number = row['slotno']
                slot_number_list.append(slot_number)
            return slot_number_list
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def get_slot_for_registration_number(self, registration_number):
        slot_number_list = []
        try:
            query = text(queries.Queries.get_slot_for_registration_number)
            conn = super(ParkingGarageDao, self).getconnection()
            values = {'vehicleno': registration_number}
            result = conn.execute(query, values)
            for row in result:
                slot_number = row['slotno']
                slot_number_list.append(slot_number)
            return slot_number_list
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def get_slot_for_registration_number_and_color(self, registration_number, color):
        slot_number_list = []
        try:
            query = text(queries.Queries.get_slot_for_registration_number_and_color)
            conn = super(ParkingGarageDao, self).getconnection()
            values = {'vehicleno': registration_number, 'color': color}
            result = conn.execute(query, values)
            for row in result:
                slot_number = row['slotno']
                slot_number_list.append(slot_number)
            return slot_number_list
        except exc.SQLAlchemyError:
            raise
        except:
            raise
