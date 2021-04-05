
import sys
import cash_money as cm

if len(sys.argv) > 1:
    raw_data = sys.argv[1]
    loaded_data = cm.load_file(raw_data)
    result = cm.growth_predictions(loaded_data)
    print(result)
else:
    print('Please supply a json')
