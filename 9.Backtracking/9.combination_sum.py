def combinationSum(candidates, target):
    res = []

    def backtrack(i, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return

        for j in range(i, len(candidates)):
            path.append(candidates[j])
            backtrack(j, path, total + candidates[j])
            path.pop()

    backtrack(0, [], 0)
    return res