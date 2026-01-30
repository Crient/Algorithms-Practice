points = [
  [1, 4],
  [2, 8],
  [5, 5],
  [6, 7],
  [3, 2],
  [9, 1],
  [4, 3]
]

def closestpair(points):
    distance = float('inf')
    point1 = None
    point2 = None

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            result = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
            if result < distance:
                distance = result
                point1 = points[i]
                point2 = points[j]

    return point1, point2, distance

p1, p2, d = closestpair(points)

print(f"Closest coordinate: {p1} and {p2}")
print(f"Squared distance: {d}")
