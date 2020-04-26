def insertInCache(memoryCache, startIndex, initialSpeed, isSpike=None):
    memoryCache[startIndex] = {initialSpeed: isSpike}


def canStop(runway, initialSpeed, startIndex=0, memoryCache=None):
    if memory_cache is None:
        memory_cache = {}

    if (startIndex in memoryCache and initialSpeed in memoryCache[startIndex]):
        return memoryCache[startIndex][initialSpeed]

    if startIndex < 0 or startIndex >= len(runway) or initialSpeed < 0 or not runway[startIndex]:
        insertInCache(memoryCache, startIndex, initialSpeed, False)
        return False

    if initial_speed == 0:
        insertInCache(memoryCache, startIndex, initialSpeed, True)
        return True

    for adjustedSpeed in [initialSpeed - 1, initialSpeed, initialSpeed + 1]:
        if canStop(runway, adjustedSpeed, startIndex + adjustedSpeed):
            insertInCache(memoryCache, startIndex, initialSpeed, True)
            return True
    insertInCache(memoryCache, startIndex, initialSpeed, False)
    return False


if __name__ == '__main__':
    runway = [True, False, True, True, True, False, True, True, False, True, True]
    test1 = canStop(runway, 2)
    print(test1)
