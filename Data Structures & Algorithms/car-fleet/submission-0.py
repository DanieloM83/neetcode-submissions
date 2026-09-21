class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # carPos1 > carPos2 and carSpeed1 >= carSpeed2 -> no fleet
        # concat pos, speed into [pos, speed] and sort by pos.
        # iterate from the farest (from 0 miles) to nearest (to 0 miles) car, and calculate if it will collide into a fleet.
        N = len(position)

        fleets = N
        cars = []
        for i in range(N):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda x: -x[0])
        
        for i in range(N - 1):
            if (target - cars[i][0]) / cars[i][1] >= (target - cars[i + 1][0]) / cars[i + 1][1]:
                fleets -= 1
                cars[i + 1][0] = cars[i][0]
                cars[i + 1][1] = cars[i][1]

        return fleets