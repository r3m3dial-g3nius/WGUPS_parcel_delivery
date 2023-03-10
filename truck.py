class Truck:
    def __init__(self, truck_num, max_items=16, loaded_items=0):
        self.truck_id = truck_num
        self.max_items = max_items
        self.loaded_items = loaded_items    # item counter for items on board
