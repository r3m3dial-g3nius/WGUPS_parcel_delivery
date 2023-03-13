class Truck:
    def __init__(self, truck_num, max_items=16, loaded_items=0):
        self.truck_id = truck_num
        self.max_items = max_items
        self.num_items_on_truck = loaded_items    # item counter for items on board
        self.truck_avg_speed = 18
        self.packages_onboard = []
        self.packages_delivered = []
        self.daily_miles_traveled = 0
