def get_unique_labels(data):
    return list(set(data))


def one_hot_encoding(data, unique_labels):
    one_hot_matrix = [[1 if value == label else 0 for label in unique_labels] for value in data]
    return one_hot_matrix


def categorical_to_numeric_one_hot(data):
    unique_labels = get_unique_labels(data)
    one_hot_matrix = one_hot_encoding(data, unique_labels)
    return one_hot_matrix

categorical_data = input("Enter categorical data (comma-separated values): ").split(',')

one_hot_matrix = categorical_to_numeric_one_hot(categorical_data)

print(f"Original Categorical Data: {categorical_data}")
print(f"One-Hot Encoded Matrix: {one_hot_matrix}")
