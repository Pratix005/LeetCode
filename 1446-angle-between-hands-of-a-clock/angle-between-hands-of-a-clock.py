class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourangle = (hour % 12) * 30 + minutes * 0.5
        minutesangle = minutes * 6

        angles = abs(hourangle - minutesangle)
        return min(angles, 360 - angles)