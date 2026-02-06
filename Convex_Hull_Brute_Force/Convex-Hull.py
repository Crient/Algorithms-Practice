# List of points (x, y) on the plane
points = [
    (1, 1),
    (1, 4),
    (4, 4),
    (4, 1),
    (2, 2),
    (3, 2),
    (2, 3)
]

# Store valid convex hull edges as pairs of points
result = set()

# Choose the first point of the potential edge
for i in range(len(points)):
    # Choose the second point of the potential edge (avoid duplicates and i == j)
    for j in range(i + 1, len(points)):
        
        # Unpack coordinates of the two endpoints
        x1, y1 = points[i]
        x2, y2 = points[j]
      
        # Compute line coefficients for ax + by = c
        a = y2 - y1
        b = x1 - x2
        c = (x1 * y2) - (y1 * x2)
         
        # Flags to track whether points appear on both sides of the line
        foundProblem = False
        pos = 0  # count of points on the positive side
        neg = 0  # count of points on the negative side
      
        # Check all other points
        for k in range(len(points)):
            # Skip the endpoints of the line
            if k == i or k == j:
                continue
                
            # Unpack the coordinates of the test point
            x, y = points[k]
            
            # Evaluate which side of the line the point lies on
            check = a * x + b * y - c
            
            # Track sign of the result
            if check > 0: 
                pos = pos + 1
            if check < 0:
                neg = neg + 1
            
            # If points exist on both sides, this edge is invalid
            if pos > 0 and neg > 0:
                foundProblem = True
                break
            
        # Add edge only if:
        # 1) No points were found on both sides
        # 2) All points are on one side (or collinear)
        # 3) At least one point is strictly on one side (not all collinear)
        if foundProblem == False and (pos == 0 or neg == 0) and (pos + neg > 0):
            result.add((points[i], points[j]))

# Output the convex hull boundary edges
print(result)
