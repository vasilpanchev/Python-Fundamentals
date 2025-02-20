strings_to_find = input().split(', ')
strings_to_search = input().split(', ')
found = [sf for sf in strings_to_find if any(ss for ss in strings_to_search if sf in ss)]
# for sf in strings_to_find:
#     for ss in strings_to_search:
#         if sf in ss:
#             found.append(sf)
#             break

print(found)
