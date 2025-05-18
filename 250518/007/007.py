secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Info:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time
    
    def print_info(self):
        print(f"secret code : {self.secret_code}")
        print(f"meeting point : {self.meeting_point}")
        print(f"time : {self.time}")

info = Info(secret_code, meeting_point, time)
info.print_info()