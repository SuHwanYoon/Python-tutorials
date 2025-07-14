import json

shoe = {
    "brand": "Nike",
    "model": "Air Max",
    "size": 10,
    "color": ["Black", "White", "Red"],
    "price": 120.00
}




def serialize(obj):
    """Serialize an object to a JSON string."""
    return json.dumps(obj)
def deserialize(json_string):
    """Deserialize a JSON string to an object."""
    return json.loads(json_string)

# Example usage
if __name__ == "__main__":
    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    serialized_data = serialize(data)
    print(f"Serialized: {serialized_data}")
    
    deserialized_data = deserialize(serialized_data)
    print(f"Deserialized: {deserialized_data}")
    assert data == deserialized_data, "Deserialization did not return the original object."
    print("Serialization and deserialization successful.")
    # Output:
    # Serialized: {"name": "Alice", "age": 30, "city": "New York"}
    # Deserialized: {'name': 'Alice', 'age': 30, 'city': 'New York'}
    # Serialization and deserialization successful.
