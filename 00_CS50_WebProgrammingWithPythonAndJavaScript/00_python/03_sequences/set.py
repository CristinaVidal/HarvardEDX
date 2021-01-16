# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # Duplicate element, it will not show at console

print(f"\nElements of list: {s}")

print("\nDeleting '2' element...")
s.remove(2)
print(f"Elements of list: {s}")

print(f"\nThe set has {len(s)} elements.")
