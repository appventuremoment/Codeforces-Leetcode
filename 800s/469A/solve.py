print((lambda target, arr1, arr2: len(set(arr1 + arr2).remove(0)) == target and "I become the guy." or "Oh, my keyboard!")(int(input()), list(map(int, input().split(' '))), list(map(int, input().split(' ')))))