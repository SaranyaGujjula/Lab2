def get_unique_labels(data):
    return list(set(data))


def label_encoding(data, labels):
    label_mapping = {label: index for index, label in enumerate(labels)}
    encoded_data = [label_mapping[value] for value in data]
    return encoded_data


def categorical_to_numeric(data):
    unique_labels = get_unique_labels(data)
    numeric_data = label_encoding(data, unique_labels)
    return numeric_data


categorical_data = input("Enter categorical data (comma-separated values): ").split(',')

numeric_data = categorical_to_numeric(categorical_data)

print(f"Original Categorical Data: {categorical_data}")
print(f"Numeric Data: {numeric_data}")
