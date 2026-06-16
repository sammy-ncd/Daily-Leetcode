"""

Problem:
https://leetcode.com/problems/process-string-with-special-operations-i/description/?envType=daily-question&envId=2026-06-16


"""



"""

Approach:
code the simulation as is using built in functions


"""



def processStr(s):
    st = []

    for c in s:

        if c == "*":
            if st:
                st.pop()
        elif c == "#":
            st.extend(st)
        elif c == "%":
            st.reverse()
        else:
            st.append(c)

    return "".join(st)




"""

Let n = length of the string after every op

Time complexity:

overall ---> O(n)

Space complextiy:

overall ---> O(n)


"""