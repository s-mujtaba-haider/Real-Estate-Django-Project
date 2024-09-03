import time

class DataTracker:
    def __init__(self, max_data_size_per_hour):
        self.max_data_size_per_hour = max_data_size_per_hour
        self.data_usage_per_hour = 0.0
        self.hour_start_time = time.time()

    def update_data_usage(self, data_size):
        current_time = time.time()
        if current_time - self.hour_start_time >= 3600:
            self.hour_start_time = current_time
            self.data_usage_per_hour = 0
        else:
            self.data_usage_per_hour += data_size

    def check_data_usage(self):
        print("Data Downloaded so far ",self.data_usage_per_hour)
        return self.data_usage_per_hour<= self.max_data_size_per_hour