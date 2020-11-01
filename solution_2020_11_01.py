
def each_segment(segment_len, prev_results, n):
    # segment_len = 3
    # prev_results = {1: [1, 2, 3, 4], 2: [1.5, 2.5, 3.5]}
    # n = 4

    max_mean_for_segments = []
    for segment_idx in range(n - segment_len + 1):
        # segment_idx range = [0, 1]
        max_mean_for_segment = None
        for split_size in range(1, segment_len / 2 + 1):
            # split_size range = [1]

            first_split_prefix = prev_results[split_size][segment_idx]  # 1, 2
            first_split_suffix = prev_results[segment_len - split_size][segment_idx + split_size]  # 2.5, 3.5
            second_split_prefix = prev_results[segment_len - split_size][segment_idx]  # 1.5, 2.5
            second_split_suffix = prev_results[split_size][segment_idx + segment_len - split_size]  # 3, 4

            max_mean_for_split_size = max(
                (first_split_prefix + first_split_suffix) / 2.,
                (second_split_prefix + second_split_suffix) / 2.
            )

            max_mean_for_segment = max(
                max_mean_for_split_size,
                max_mean_for_segment if max_mean_for_segment is not None else max_mean_for_split_size
            )
        max_mean_for_segments.append(max_mean_for_segment)

    return max_mean_for_segments


def find_max(numbers):
    n = len(numbers)
    if n == 1:
        return numbers[0]
    results = {1: numbers}
    for segment_len in range(2, n + 1):
        results[segment_len] = each_segment(segment_len, results, n)
    return results[n][0]
