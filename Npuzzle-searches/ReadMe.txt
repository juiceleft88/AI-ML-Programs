In this program, I use informed and uninformed searches to solve various sizes of N-Puzzles. Depth-First Search, Breadth-First Search, A* search,
and A* with Heuristic are used to not only try and solve the puzzles, but to compare which was fastest and most efficient. My findings are below. 

Which algorithm performed the fastest?
        Depth-First Search was the fastest algorithm for ex1, breadth-first search was fastest for ex2 and ex3 test, 
        and A*1 for ex4. ex5 and ex6 just froze and would not run. All the times were relativiely close/short for ex1.

Which took up the most memory?
        DFS consistently took up the most memory (except in the case of ex1, where BFS and DFS were tied, and A*1 took up most memory.)
        It was interesting to see that A*1 was so consistent in the amount of memory it took, but not in performance time.
    
Which gave the best solution?
        I believe A*1 gave the best solution, since as the move counts increased, the time performance stayed similar to BFS, but often used less memory.

    Some of the cases took way too computational resources for my machine, and would just freeze. Therefore, I tried to implement a depth limit.
