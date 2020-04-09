


def can_stop(runway, initial_speed, start_index=0, memory_cache=None):
    # only done the first time to initialize the memory_cache
    if memory_cache is None:
        memory_cache = {}

    # first check is the result exists in memo
    if start_index in memory_cache and initial_speed in memory_cache[start_index]:
        return memory_cache[start_index][initial_speed]

    # negative base cases need to go first
    if (start_index < 0 or start_index >= len(runway) or initial_speed < 0 or not runway[start_index]):
        insert_into_memory_cache(
            memory_cache, start_index, initial_speed, False)
        return False

    # base case for a stoping condition
    if initial_speed == 0:
        insert_into_memory_cache(
            memory_cache, start_index, initial_speed, True)
        return True

    # Try all possible paths
    for adjusted_speed in [initial_speed - 1, initial_speed, initial_speed + 1]:
        # recurrence relation: if you can stop from any of the subproblems, you can stop from the main problem
        if can_stop(runway, adjusted_speed, start_index + adjusted_speed):
            insert_into_memory_cache(
                memory_cache, start_index, initial_speed, True)
            return True
    insert_into_memory_cache(memory_cache, start_index, initial_speed, False)
    return False


# test cases
runway = [True, False, True, True, True, False, True, True, False, True, True]
test1 = can_stop(runway, 2)
print(test1)
