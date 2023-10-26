"""
See Problem 056 on CSPLib

Example of Execution:
  python3 Sonet.py -data=Sonet_sonet1.json
"""

from pycsp3 import *

n, m, r, connections = data

# x[i][j] is 1 if the ith ring contains the jth node
x = VarArray(size=[m, n], dom={0, 1})

T = {tuple(1 if j // 2 == i else ANY for j in range(2 * m)) for i in range(m)}

satisfy(
    [(x[i][conn] for i in range(m)) in T for conn in connections],

    # respecting the capacity of rings
    [Sum(x[i]) <= r for i in range(m)],

    # tag(symmetry-breaking)
    LexIncreasing(x)
)

minimize(
    # minimizing the number of nodes installed on rings
    Sum(x)
)

"""
1) Note that
   [(x[i][conn] for i in range(m)) in T for conn in connections]
 is a shortcut for:
   [(x[i][j1 if k == 0 else j2] for i in range(m) for k in range(2)) in T
      for (j1, j2) in connections]
"""
