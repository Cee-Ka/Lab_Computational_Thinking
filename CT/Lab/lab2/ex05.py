class Robot:
    active_count = 0

    def __init__(self, name):
        self.name = name
        Robot.active_count += 1
    def remove(self):
        if Robot.active_count > 0:
            Robot.active_count -= 1
    @classmethod
    def number_active(cls):
        print(f"Active robots: {cls.active_count}")

r1 = Robot("Alpha")
r2 = Robot("Beta")

Robot.number_active()   
r1.remove()
Robot.number_active()

r2.remove()
Robot.number_active()
