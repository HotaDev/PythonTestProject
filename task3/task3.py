import sys
import os
import json

dir = os.path.dirname(sys.argv[0])

with open(os.path.join(dir, sys.argv[1])) as f:
    test_json = f.read()
report = json.loads(test_json)

with open(os.path.join(dir, sys.argv[2])) as f:
    values_json = f.read()
value = json.loads(values_json)

def makeReport(report):
    for tests in report:
        for list_code in value['values']:
            if list_code['id'] == tests['id']:
                tests['value'] = list_code['value']
                break
        if 'values' in tests:
            makeReport(tests['values'])
    return report
      

report_json = json.dumps(makeReport(report['tests']))

with open(os.path.join(dir, "report.json"), "w") as f:
    f.write(report_json)

