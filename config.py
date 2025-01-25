
class ScheduleConfig:
    def __init__(self, working_days=None, shifts_per_day=3, hours_per_shift=8, constructions_per_hour=17, num_kettles=12):
        self.working_days = working_days or ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.shifts_per_day = shifts_per_day
        self.hours_per_shift = hours_per_shift
        self.constructions_per_hour = constructions_per_hour
        self.num_kettles = num_kettles

    @property
    def constructions_per_shift(self):
        return self.hours_per_shift * self.constructions_per_hour

    @property
    def total_shifts(self):
        return len(self.working_days) * self.shifts_per_day
    
