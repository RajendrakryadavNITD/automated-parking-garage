from excel_reader.dal import connection_factory
from excel_reader.dao import dao_factory


class PakingGarageHelper(object):
    def get_connection(self, existing_conn=None):
        is_new_connection = False
        conn = None
        try:
            if existing_conn is None:
                myconn = connection_factory.ConnectionFactory.create()
                conn = myconn.getconnection()
                is_new_connection = True
            else:
                conn = existing_conn
            return conn
        except:
            raise

    def create_parking_place(self, no_of_parking_slot, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.parking_garage_dao(conn)
            dao.create_parking_place(no_of_parking_slot)
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def get_a_parking_space(self, vehicle_no, color, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.parking_garage_dao(conn)
            slot_list = dao.checking_for_parking_space_availability()
            if slot_list is not None and len(slot_list) > 0:
                slot = slot_list[0]
                slot_id = dao.get_parking_slot_id_using_slot_no(slot)
                slot_number = dao.get_a_parking_space(slot_id, vehicle_no, color)
                dao.update_parking_slot(slot_id)
                return slot_number
            else:
                print 'Sorry, parking garage is full'
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def leaving_parking_slot(self, slot_no, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.parking_garage_dao(conn)
            dao.leaving_parking_slot(slot_no)
            print  'Slot number', slot_no,'is free'
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()


    def get_parking_garage_status(self, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.parking_garage_dao(conn)
            parking_garage_status_list = dao.get_parking_garage_status()
            if parking_garage_status_list is not None:
                return parking_garage_status_list
            else:
                print 'parking garage is empty'
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def get_registration_numbers_of_cars_with_color(self, color_of_car, existing_conn =None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.parking_garage_dao(conn)
            registration_number_list = dao.get_registration_numbers_of_cars_with_color(color_of_car)
            if registration_number_list is not None and len(registration_number_list) > 0:
                return registration_number_list
            else:
                print 'not found'
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def get_slots_for_cars_with_color(self, color_of_car, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.parking_garage_dao(conn)
            slot_number_list = dao.get_slots_for_cars_with_color(color_of_car)
            if slot_number_list is not None and len(slot_number_list) > 0:
                return slot_number_list
            else:
                print 'not found'
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def get_slot_for_registration_number(self, registration_number, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.parking_garage_dao(conn)
            slot_number_list = dao.get_slot_for_registration_number(registration_number)
            if slot_number_list is not None and len(slot_number_list) > 0:
                return slot_number_list
            else:
                print 'not found'
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()


    def get_slot_for_registration_number_and_color(self, registration_number, color, existing_conn=None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.parking_garage_dao(conn)
            slot_number_list = dao.get_slot_for_registration_number_and_color(registration_number, color)
            if slot_number_list is not None and len(slot_number_list) > 0:
                return slot_number_list
            else:
                print 'not found'

        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()
