import sys
import os
import json

dir = os.path.dirname(sys.argv[0])

with open(os.path.join(dir, input('Введите название файла тестов '))) as f:
    test_json = f.read()
report = json.loads(test_json)

with open(os.path.join(dir, input('Введите название файла со значениями тестов '))) as f:
    values_json = f.read()
value = json.loads(values_json)

for tests in report['tests']:
    for list_code in value['values']:
        if list_code['id'] == tests['id']:
            tests['value'] = list_code['value']
            break
    if 'values' in tests:
        for add1 in tests['values']:
            for list_code in value['values']:
                if list_code['id'] == add1['id']:
                    add1['value'] = list_code['value']
                    break
            if 'values' in add1:
                for add2 in add1['values']:
                    if 'values' in add2:
                        for add3 in add2['values']:
                            for list_code in value['values']:
                                if list_code['id'] == add3['id']:
                                    add3['value'] = list_code['value']
                                    break

report_json = json.dumps(report)

with open(os.path.join(dir, "report.json"), "w") as f:
    f.write(report_json)

