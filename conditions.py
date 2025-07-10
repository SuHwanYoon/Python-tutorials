is_raining = False
distance_to_office = 3  # 거리 (킬로미터 단위)

if is_raining or distance_to_office > 5:
    print("Take an umbrella and drive to the office.")
elif distance_to_office <= 5 and not is_raining:
    print("You can walk to the office.")
else:
    print("You can ride a bike to the office.")
 

print("Enjoy your day!")    