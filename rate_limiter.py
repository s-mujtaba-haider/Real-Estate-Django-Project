import time

class RateLimiter:

    def __init__(self,max_requests, per_time_unit):

        self.max_requests=max_requests
        self.per_time_unit= per_time_unit
        self.request_tracker=[]

    
    def allow_request(self):
        current_time = time.time()

        self.request_tracker = [req_time for req_time in self.request_tracker if req_time >= current_time - self.per_time_unit]

        if len(self.request_tracker) < self.max_requests:
            self.request_tracker.append(current_time)
            return True
        else:
            return False