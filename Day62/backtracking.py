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




note to self:
draw the decision/recursion tree if you're struggling
and think about base cases

READ: https://leetcode.com/problems/combination-sum/solutions/16502/a-general-approach-to-backtracking-quest-dexx/


think about info we need to always have and it may be a backtracking param

"""