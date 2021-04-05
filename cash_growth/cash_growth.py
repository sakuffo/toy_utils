# %%
import sys
import json

# %%
def grow_cash(st_amt, gw_pct, num_rota):
  computed_amount = st_amt
  return computed_amount * gw_pct**num_rota

# %%
def growth_predictions(args):
  starting_amount = int(args["st_amt"])
  growth_percentage = float(args["gw_pct"])
  num_of_rotations = int(args["num_rota"])

  return grow_cash(starting_amount, growth_percentage, num_of_rotations)

# %%

def load_file(json_file='./test.json'):
  with open(json_file) as f:
    data=json.loads(f.read())
    f.close()
    return data

# %%

data = load_file()
result = growth_predictions(data)
print(result)

# %%
