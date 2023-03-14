import datetime


class Truck:
    def __init__(self, truck_num, max_items=16):
        self.truck_id = truck_num
        self.max_items = max_items
        self.truck_avg_speed = 18
        self.packages_onboard = []
        self.packages_delivered = []
        self.daily_miles_traveled = 0
        self.num_items_on_truck = 0    # item counter for items on board
        self.time_of_departure = datetime.timedelta(hours=0)
        self.current_time = datetime.timedelta(hours=0)
        self.time_of_return = datetime.timedelta(hours=0)
        self.truck_status = 'AT HUB'
