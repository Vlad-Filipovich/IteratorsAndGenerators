# Infinite process

# def create_patterns():
#     max_patterns_number = 100
#     patterns = ('First pattern', 'Second pattern', 'Third pattern', 'Forth pattern')
#     count = 0
#     result_list = []
#
#     while len(result_list) < max_patterns_number:
#         if count >= len(patterns):
#             count = 0
#         result_list.append(patterns[count])
#         count += 1
#
#     return result_list
#
#
# print(create_patterns())


def get_current_pattern():
    patterns = ('First pattern', 'Second pattern', 'Third pattern', 'Forth pattern')
    count = 0
    while True:
        if count >= len(patterns):
            count = 0
        yield patterns[count]
        count += 1


current_pattern = get_current_pattern()