
def can_attend_all(events):
    events = sorted(events)

    for i in range(1, len(events)):
        if events[i][0] < events[i - 1][1]:
            return False
    return True


def min_rooms_required(events):
    if not events:
        return 0

    # Every event must have a positive duration
    for start, end in events:
        if start >= end:
            raise ValueError("each event must satisfy start < end")

    starts = sorted(start for start, end in events)
    ends = sorted(end for start, end in events)

    start_ptr = 0
    end_ptr = 0
    active_rooms = 0
    max_rooms = 0

    while start_ptr < len(events):
        if starts[start_ptr] < ends[end_ptr]:
            active_rooms += 1
            max_rooms = max(max_rooms, active_rooms)
            start_ptr += 1
        else:
            active_rooms -= 1
            end_ptr += 1

    return max_rooms


# Tests
assert can_attend_all([(9, 10), (10, 11), (11, 12)]) is True
assert can_attend_all([(9, 11), (10, 12)]) is False
assert can_attend_all([]) is True

assert min_rooms_required([(9, 10), (10, 11), (11, 12)]) == 1
assert min_rooms_required([(9, 11), (10, 12), (10, 13)]) == 3
assert min_rooms_required([(9, 11), (9, 11)]) == 2
assert min_rooms_required([]) == 0

# Check that zero-duration events are rejected
try:
    min_rooms_required([(5, 5)])
    assert False, "should have raised ValueError"
except ValueError:
    pass

print("All Event Scheduler tests passed!")
