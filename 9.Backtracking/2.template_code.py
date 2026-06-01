def backtrack(path,choices):
    if is_solution(path):
        process_solution(path)
        return
    
    for choice in choices:
        if is_valid(choice,path):
            path.append(choice)
            backtrack(path,next_choices(choice,path))
            path.pop()