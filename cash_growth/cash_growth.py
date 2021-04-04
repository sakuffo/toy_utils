starting_amount = 10000

def grow_cash(st_amt, gw_pct, num_rota):
  computed_amount = st_amt
  for x in range(num_rota):
    computed_amount = computed_amount * gw_pct

  return computed_amount

print(grow_cash(starting_amount, 1.1, 1))
