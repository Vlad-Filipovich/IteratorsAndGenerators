# def get_number_from_range():
#     for number in range(5):
#         yield number
#
#
# counter1 = get_number_from_range()
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))

counter2 = (number for number in range(5))
print(next(counter2))
print(next(counter2))
print(next(counter2))