def sense_front_vehicle(frame_id, file):
    front_vehicle = file[
        (file["Vehicle_ID"] == file["Preceding"][frame_id]) &
        (file["Frame_ID"] == (file["Frame_ID"][frame_id]))]

    if not front_vehicle.empty:
        return front_vehicle
    else:
        return 0


def sense_vehicle_on_right(lane_id, frame_id, front_y_position, file):
    if front_y_position == 0:
        vehicle_sensed = file[
            (file["Lane_ID"] == (lane_id + 1)) &
            (file["Frame_ID"] == (file["Frame_ID"][frame_id])) &
            (file["Local_Y"] >= (file["Local_Y"][frame_id])) &
            (file["Local_Y"] <= (file["Local_Y"][frame_id] + 100))]
    else:
        vehicle_sensed = file[
            (file["Lane_ID"] == (lane_id + 1)) &
            (file["Frame_ID"] == (file["Frame_ID"][frame_id])) &
            (file["Local_Y"] >= (file["Local_Y"][frame_id])) &
            (file["Local_Y"] <= front_y_position) &
            (file["Local_Y"] <= (file["Local_Y"][frame_id] + 100))]

    if not vehicle_sensed.empty:
        return vehicle_sensed
    else:
        return 0


def sense_vehicle_on_left(lane_id, frame_id, front_y_position, file):
    if front_y_position == 0:
        vehicle_sensed = file[
            (file["Lane_ID"] == (lane_id - 1)) &
            (file["Frame_ID"] == (file["Frame_ID"][frame_id])) &
            (file["Local_Y"] >= (file["Local_Y"][frame_id])) &
            (file["Local_Y"] <= (file["Local_Y"][frame_id] + 100))]
    else:
        vehicle_sensed = file[
            (file["Lane_ID"] == (lane_id - 1)) &
            (file["Frame_ID"] == (file["Frame_ID"][frame_id])) &
            (file["Local_Y"] >= (file["Local_Y"][frame_id])) &
            (file["Local_Y"] <= front_y_position) &
            (file["Local_Y"] <= (file["Local_Y"][frame_id] + 100))]

    if not vehicle_sensed.empty:
        return vehicle_sensed
    else:
        return 0
