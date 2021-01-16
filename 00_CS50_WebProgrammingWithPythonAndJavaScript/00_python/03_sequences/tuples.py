coordinate = (10.0, 20.0)

print(f"Coordinate: {coordinate}")
print(f"X: {coordinate[0]}\nY: {coordinate[1]}")

print("\nChanging values...")
#coordinate[0] = coordinate[1] - coordinate[0]
#coordinate[1] -= coordinate[0]
#coordinate[0] += coordinate[1] ## --> It doesn't works bc tuples are inmutables
coordinate = (coordinate[1], coordinate[0])
print(f"Coordinate: {coordinate}")
print(f"X: {coordinate[0]}\nY: {coordinate[1]}")
