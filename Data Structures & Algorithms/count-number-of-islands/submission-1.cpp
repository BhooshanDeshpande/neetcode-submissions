class Solution {
public:
    template <typename T>
    void printVec(vector<vector<T>> vec)
    {
        for (auto row : vec)
        {
            for (auto col : row)
            {
                cout << col << " ";
            }
            cout << "\n"; 
        }
    }

    vector<vector<int>> findNbrs(vector<vector<char>>& grid, vector<vector<bool>>& visited, int r, int c)
    { 
        vector<int> dl = {0, -1};
        vector<int> dr = {0, 1};
        vector<int> du = {-1, 0};
        vector<int> dd = {1, 0};

        vector<vector<int>> dirs = {dl, dr, du, dd};
        vector<vector<int>> valid_nbr = {};

        for (auto dir : dirs)
        { 
            auto rnew = r + dir[0];
            auto cnew = c + dir[1];

            if (rnew >= 0 && rnew != grid.size() && cnew >= 0 &&
            cnew != grid[0].size() && visited[rnew][cnew] != true 
            && grid[rnew][cnew] != '0')
            {
                valid_nbr.push_back({rnew, cnew});
            }
        }
        return valid_nbr; 
    }

    void dfs(vector<vector<char>>& grid,  vector<vector<bool>>& visited,  int r, int c)
    {
        // mark visited
        visited[r][c] = true;
        // findNbrs (grid, r, c) --> nbrs vector<vector<int>>
        auto nbrs = findNbrs(grid, visited, r, c);
        if (nbrs.size() == 0) return;
        // push to stack 
        stack<vector<int>> st;
        for (auto nbr : nbrs) 
        {
            st.push(nbr);
        }
        // pop from stack 
        while (!st.empty())
        {
            vector<int> nbr = st.top();
            st.pop();
            dfs(grid, visited, nbr[0], nbr[1]);
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        vector<vector<bool>> visited(grid.size(), vector<bool>(grid[0].size(), false));
        int numIslands = 0;
        for (int r = 0; r < grid.size(); r++)
        {
            for (int c = 0; c < grid[0].size(); c++)
            {
                auto elem = grid[r][c]; 
                if (elem == '1' && visited[r][c] == false)
                {
                    dfs(grid, visited, r, c);
                    numIslands++;
                    printVec(visited);
                    cout << " - " << endl;
                }
            }
        }

        return numIslands;
    }
};
