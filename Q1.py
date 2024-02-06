def euclidean_distance(vector1, vector2):
    assert len(vector1) == len(vector2), "Vectors must have the same dimension"
    sum_squared_diff = sum((v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2))
    return sum_squared_diff


def manhattan_distance(vector1, vector2):
    assert len(vector1) == len(vector2), "Vectors must have the same dimension"
    sum_absolute_diff = sum((v1 - v2) if v1 >= v2 else (v2 - v1) for v1, v2 in zip(vector1, vector2))
    return sum_absolute_diff

vector_a = [float(x) for x in input("Enter vector A (comma-separated values): ").split(',')]
vector_b = [float(x) for x in input("Enter vector B (comma-separated values): ").split(',')]

euclidean_result = euclidean_distance(vector_a, vector_b)
manhattan_result = manhattan_distance(vector_a, vector_b)

print(f"Euclidean Distance: {euclidean_result}")
print(f"Manhattan Distance: {manhattan_result}")
