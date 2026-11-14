import json

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(
            f"JSON file not found: {file_path}"
        )
    except json.JSONDecodeError:
        raise ValueError(
            f"Invalid JSON file: {file_path}"
        )

def validate_json_data(flight_test_data):
    assert len(flight_test_data) > 0
    print('PASS: Json file contain atleast one data')

    for data in flight_test_data:
        assert 'departure' in data, f'Missing departure field'
        assert 'destination' in data, f'Missing destination field'
        assert 'expected_route' in data, f'Missing expected_route field'


        assert data['departure'].strip() != '', f'Departure value is empty'
        assert data['destination'].strip() != '', f'Destination value is empty'
        assert data['expected_route'].strip() != '', f'Expected route value is empty'

