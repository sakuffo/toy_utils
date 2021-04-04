import sys

def grow_cash(st_amt, gw_pct, num_rota):
  computed_amount = st_amt
  for x in range(num_rota):
    computed_amount = computed_amount * gw_pct

  return computed_amount

def growth_predictions(args):
  starting_amount = int(args[1])
  growth_percentage = float(args[2])
  num_of_rotations = int(args[3])

  return grow_cash(starting_amount, growth_percentage, num_of_rotations)

result = growth_predictions(sys.argv)
print(result)



