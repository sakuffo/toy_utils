import json


def grow_cash(json_data):
    starting_amount = int(json_data["st_amt"])
    growth_percentage = float(json_data["gw_pct"])
    num_of_rotations = int(json_data["num_rota"])
    return starting_amount * growth_percentage ** num_of_rotations


def growth_predictions(args):
    all_results = []
    for x in args:
        all_results.append(grow_cash(x))
    return all_results


def load_file(json_file):
    with open(json_file) as f:
        data = json.loads(f.read())
        f.close()
        return data
