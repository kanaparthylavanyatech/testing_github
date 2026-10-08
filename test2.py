def delivery_fee(amount, fee=40):
  if amount >=300:
    return 0
  return fee
print(delivery_fee(200))