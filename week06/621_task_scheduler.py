# Idea:
# The minimal total time is bound by the highest frequency task.
#
# e.g. n = 2, job A has highest frequency 5, the total time must be at least (5 - 1) * (2 + 1) + 1 = 13.
# Since there needs (5 - 1) cool down intervals between each task A. That creates 4 segments, each start with 1 unit time for A and followed by 2 idle unit time. The final task A doesn't need cool down time.
#
# e.g. n = 2, both job A and B have highest frequency 5.
# Start by considering job A, it needs 4 cool down intervals, at least 2 unit time each.
# Since job B needs the same amount of cool down time, placing B right after each A will work.
# The last job B must be after the last job A, therefore the last segment is 2 unit time.
# The minimal total time plan looks like "A..A..A..A..AB"
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        d = collections.defaultdict(list)

        f_max = 0
        for k, freq in c.items():
            d[freq] += [k]
            f_max = max(freq, f_max)
        n_max = len(d[f_max])

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)