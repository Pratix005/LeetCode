class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0

        for i in gain:
            altitude += i
            highest = max(altitude, highest)
        return highest