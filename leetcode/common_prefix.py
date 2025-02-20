def longest_common_prefix(strs: list[str]) -> str:
    shortest_str = min(strs, key=len)
    prefix = ""
    for i in range(len(shortest_str)):
        for string in strs:
            if string[i] != shortest_str[i]:
                return prefix

        prefix += shortest_str[i]

    return prefix


strs = input().split()
print(longest_common_prefix(strs))
