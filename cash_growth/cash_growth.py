# %%
import sys
import json

# %%
def grow_cash(json_data):
  starting_amount = int(json_data["st_amt"])
  growth_percentage = float(json_data["gw_pct"])
  num_of_rotations = int(json_data["num_rota"])
  return starting_amount * growth_percentage ** num_of_rotations

# %%
def growth_predictions(args):
  if len(args) == 1:
    return grow_cash(args[0]["st_amt"], args[0]["gw_pct"], args[0]["num_rota"])
  else:
    all_results= []
    for x in args:
      all_results.append(grow_cash(x))
    return all_results

# %%

def load_file(json_file):
  with open(json_file) as f:
    data=json.loads(f.read())
    f.close()
    return data

# %%

data = load_file(sys.argv[1])
result = growth_predictions(data)
print(result)

# %%

# %%
