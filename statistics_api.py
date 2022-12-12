from flask import Blueprint, jsonify, request, json
import re
import numpy as np
import statistics as st

statistics_api = Blueprint('statistics_api', __name__)


@statistics_api.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        data = json.loads(request.data)
        temp_numbers = data['numbers']
        numbers = [eval(x) for x in re.split(r'[\s]+|[\t]+|,',
                   temp_numbers.strip()) if len(x) != 0]
        np_numbers = np.array(numbers)

        data = {
            'Sorted Array': convert_to_string(sorted(numbers)),
            'Mean': convert_to_string(np_numbers.mean()),
            'Median': convert_to_string(np.median(np_numbers)),
            'Mode': convert_to_string(st.multimode(np_numbers)),
            'Range': convert_to_string(find_range(numbers)),
            'Sample Standard Deviation': convert_to_string(np_numbers.std(ddof=1)),
            'Sample Variance': convert_to_string(np_numbers.var(ddof=1)),
            'Population Standard Deviation': convert_to_string(np.std(np_numbers)),
            'Population Variance': convert_to_string(np.var(np_numbers)),
            }
        return jsonify(data)
    else:
        return 'Bad Request!'

def convert_to_string(value):
    value_to_print = "%0.3f" % value if type(
        value) != list else str(value)[1:-1]
    return value_to_print

def find_range(numbers):
    range = max(numbers) - min(numbers)
    return range
