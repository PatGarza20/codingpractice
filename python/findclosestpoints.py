## Given a list of points as a tuple (x, y) and an integer k, 
## find the k closest points to the origin (0,0).

# Calculates a point's distance from the origin by
# adding up how many "steps" it would take to reach (0,0).
def distance(point):
    return abs(point[0]) + abs(point[1])

def closest_points(points, k):
    # Throws an error if the user asks for more points than are given.
    if len(points) < k:
        return "ERROR: Asking for {} closest points when only {} points exist.".format(k, len(points))

    # Closest is a dictionary, using distance: points (e.g 0: (0,0))
    closest = {}
    results = []

    # All points are added into Closest, sorted by distance from origin.
    for iter in range(len(points)):
        dist = distance(points[iter])

        if dist not in closest:
            closest[dist] = [points[iter]]
        else:
            closest[dist].append(points[iter])
    
    values = sorted(list(closest))
    
    # Using values for order, adds up to "k" items into results.
    for val in values:
        for items in closest[val]:
            results.append(items)
            
            if len(results) == k:
                return results

    return results

if __name__ == "__main__":
    print(closest_points([(0,0),(1,2), (-3, 4), (3, 1)], 2))