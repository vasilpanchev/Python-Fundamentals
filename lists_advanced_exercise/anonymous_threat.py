strings = input().split()

while True:
    command = input().split()
    if command[0] == "3:1":
        print(' '.join(strings))
        break

    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index < 0:
            start_index = 0
        if end_index >= len(strings):
            end_index = len(strings) - 1

        work_string = strings[start_index:end_index + 1]
        merged_element = ''.join(work_string)
        for i in range(start_index, end_index + 1):
            if len(strings) > 0:
                strings.pop(start_index)
        strings.insert(start_index, merged_element)

    if command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        word_to_split = strings.pop(index)
        split_word = []
        characters_per_partition = len(word_to_split) // partitions

        if characters_per_partition % 2 == 0:
            for i in range(0, len(word_to_split), characters_per_partition):
                split_word.append(word_to_split[i:(i + characters_per_partition)])
        else:
            for i in range(0, len(word_to_split) - characters_per_partition - 1, characters_per_partition):
                split_word.append(word_to_split[i:(i + characters_per_partition)])
            split_word.append(word_to_split[len(word_to_split) - characters_per_partition - 1:])

        for i in range(len(split_word) - 1, -1, -1):
            strings.insert(index, split_word[i])
