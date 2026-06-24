"""

Template 1:

def backtrack(params):

    if baseCase:
        result.append(copy of soln)
        return

    for each choice u can make:
        if choice violates constraint:
            continue
            
        makechoice
        backtrack(updated params)
        undo choice ---> this is where backtracking happens





Template 2:


Pick a starting point.
while(Problem is not solved)
    For each path from the starting point.
        check if selected path is safe, if yes select it
        and make recursive call to rest of the problem
        before which undo the current move.
    End For
If none of the move works out, return false, NO SOLUTON.



"""