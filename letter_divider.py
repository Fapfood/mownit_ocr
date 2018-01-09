from skimage import measure

SPACE = 'SPACE'


def maximum_intervals(intervals, with_grouping=False):
    intervals = sorted(intervals, key=lambda i: (i[0], -i[1]))

    maximum_intervals = []
    current_interval = intervals[0]
    groups = []
    current_group = [current_interval]

    for interval in intervals[1:]:
        if current_interval[1] >= interval[0]:
            end = current_interval[1] if current_interval[1] > interval[1] else interval[1]
            current_interval = (current_interval[0], end)
            current_group.append(interval)
        else:
            maximum_intervals.append(current_interval)
            current_interval = interval
            groups.append(current_group)
            current_group = [current_interval]

    maximum_intervals.append(current_interval)
    groups.append(current_group)

    if with_grouping:
        return maximum_intervals, groups

    return maximum_intervals


def divide(img, with_spaces=False):
    neg = 255 - img
    neg[neg > 128] = 255
    neg[neg <= 128] = 0

    label = measure.label(neg, background=0)
    props = measure.regionprops(label)

    # divide text into lines
    intervals = [(p.bbox[0], p.bbox[2]) for p in props]
    intervals = maximum_intervals(intervals)
    for i in reversed(range(len(intervals)-1)):
        if intervals[i][1] + 1 == intervals[i + 1][0]:
            intervals[i] = (intervals[i][0], intervals[i + 1][1])
            intervals.remove(intervals[i + 1])

    lines = []
    start_index = 0
    for interval in intervals:
        current_line = []
        for prop in props[start_index:]:
            if interval[0] <= prop.bbox[0] <= interval[1]:
                current_line.append(prop)
                start_index += 1
            else:
                break
        current_line = sorted(current_line, key=lambda p: p.bbox[1])
        lines.append(current_line)

    # connect two parts letter into one and get indexes of letter borders
    result_lines = []
    for line in lines:
        h_intervals = [(p.bbox[1], p.bbox[3]) for p in line]
        _, groups = maximum_intervals(h_intervals, True)

        group_index = 0
        in_group_index = 1
        min_a, min_b, max_c, max_d = float('inf'), float('inf'), float('-inf'), float('-inf')

        result_line = []
        for letter in line:
            a, b, c, d = letter.bbox
            min_a, min_b, max_c, max_d = min(a, min_a), min(b, min_b), max(c, max_c), max(d, max_d)

            if len(groups[group_index]) == in_group_index:
                result_line.append((min_a, min_b, max_c, max_d))
                group_index += 1
                in_group_index = 1
                min_a, min_b, max_c, max_d = float('inf'), float('inf'), float('-inf'), float('-inf')
            else:
                in_group_index += 1

        result_lines.append(result_line)

    # add spaces between words
    if with_spaces:
        for line in result_lines:
            h_intervals = [(p[1], p[3]) for p in line]

            space_h_intervals = []
            for i, h_interval in enumerate(h_intervals[1:]):
                space_h_intervals.append((h_intervals[i][1] + 1, h_interval[0] - 1))

            space_length = [i[1] - i[0] + 1 for i in space_h_intervals]

            sorted_space_length = sorted(space_length)
            diff_in_space_length = []
            for i, space_len in enumerate(sorted_space_length[1:]):
                diff_in_space_length.append(space_len - sorted_space_length[i])

            index = diff_in_space_length.index(max(diff_in_space_length))
            spaces = sorted_space_length[index + 1:]

            real_space_indexes = [i + 1 for i, l in enumerate(space_length) if l in spaces]

            for index in reversed(real_space_indexes):
                line.insert(index, SPACE)

    # get real arrays with letters
    new_result_lines = []
    for line in result_lines:
        new_result_line = []
        for letter in line:
            if letter == SPACE:
                new_result_line.append(letter)
            else:
                a, b, c, d = letter
                part = img[a - 1:c + 1, b - 1:d + 1]
                new_result_line.append(part)
        new_result_lines.append(new_result_line)

    return new_result_lines
