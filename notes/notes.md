## Algorithm design pattern:

- Sorting: Uncover some structure by sorting the input.
- Recursion: If the structure of the input is defined in a recursive manner, design a recursive algorithm that 
follows the input definition.
- Divide-and-conquer: Divide the problem into two or more smaller independent subproblems and solve the original problem using solutions to the subproblems.
- Dynamic programming: Compute solutions for smaller instances of a given problem and use these solutions to construct a solution to the problem. Cache for performance.
- Greedy algorithms: Compute a solution in stages, making choices that are locally optimum at step; these choices are never undone.
- Invariants: Identify an invariant and use it to rule out potential solutions that are suboptimal/dominated by other solutions.

#### System design pattern:
- Decomposition Split the functionality, architecture, and code into manageable, reusable components.
- Parallelism Decompose the problem into subproblems that can be solved independently on different machines.
- Caching Store computation and later look it up to save work, (dynamic programming, recursion).