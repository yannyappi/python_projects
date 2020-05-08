def ground_shipping_cost(weight):
  if weight <= 2:
    return weight * 1.5 + 20
  elif weight <= 6:
    return weight * 3 + 20
  elif weight <= 10:
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20
  
print(ground_shipping_cost(8.4))

premium_ground_cost = 125

def drone_shipping_cost(weight):
  if weight <= 2:
    return weight * 4.5
  elif weight <= 6:
    return weight * 9
  elif weight <= 10:
    return weight * 12
  else:
    return weight * 14.25
  
print(drone_shipping_cost(1.5))

def cheapest_shipping_option(weight):
  ground = ground_shipping_cost(weight)
  premium = premium_ground_cost
  drone = drone_shipping_cost(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone
  
  print("You should ship using "+method+" shipping, it will cost $"+str(cost))
 
    
  
print(cheapest_shipping_option(4.8))
print(cheapest_shipping_option(41.5))