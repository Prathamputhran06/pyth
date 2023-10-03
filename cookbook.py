EXPECTED_COOKING_TIME=40
Com=int(input("enter the completion time"))
def cooking_time_remaining(A):
  return A-C
numofpiece=int(input("enter the number of piece required"))
def preparation_time_required_in_minutes(numofpiece):
  return int((numofpiece/10)*5)
def remaining_time_in_minutes(numofpiece,elapsed_time):
  return EXPECTED_COOKING_TIME-(elapsed_time-preparation_time_required_in_minutes(numofpiece))
print(remaining_time_in_minutes(numofpiece,25))
