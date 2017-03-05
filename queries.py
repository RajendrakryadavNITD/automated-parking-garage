class Queries (object):
    get_last_inserted_id = "select last_insert_id() as id"

    checking_for_parking_space_availability = "select slotno from parkingslot where status = :status and slotno > 0"

    get_parking_slot_id_using_slot_no = "select id from parkingslot where slotno = :slotno"

    create_parking_place = "insert into parkingslot (slotno) values (:slotno)"

    leaving_parking_slot = "update parkingslot set status = :status where slotno= :slotno"

    get_a_parking_space = "insert into vehicle (parkingslotid, vehicleno, color) values (:parkingslotid, :vehicleno, :color)"

    get_parking_garage_status = "select ps.slotno, v.vehicleno, v.color from vehicle v inner join parkingslot ps on v.parkingslotid = ps.id "

    get_registration_numbers_of_cars_with_color = "select vehicleno from vehicle where color = :color"

    get_slots_for_cars_with_color = "select ps.slotno from parkingslot ps inner join vehicle v on ps.id = v.parkingslotid where color = :color"

    get_slot_for_registration_number = "select ps.slotno from parkingslot ps inner join vehicle v on ps.id = v.parkingslotid where vehicleno = :vehicleno"

    get_slot_for_registration_number_and_color = "select ps.slotno from parkingslot ps inner join vehicle v on ps.id = v.parkingslotid where v.vehicleno = :vehicleno and v.color = :color"

    update_parking_slot = "update parkingslot set status = :status where id = :id"
