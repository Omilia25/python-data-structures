class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

centers = [2,7,9]
def getMinimumDays(parcels):
    centers = sorted(parcels)
    days = 1
    minimum = 0
    for center in centers:
       minimum = center
       centers.remove(center)
       days += 1
       for center in centers:
            center = center-minimum
    print(days)
getMinimumDays(centers)