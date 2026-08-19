/*
    DSA Day 11
    Topic: Time Complexity and Space Complexity

    Topics covered:
    1. O(1) Time Complexity
    2. O(n) Time Complexity
    3. O(log n) Time Complexity
    4. O(n log n) Time Complexity
    5. O(n^2) Time Complexity
    6. Geometric Progression
    7. O(1) Auxiliary Space
    8. O(n) Auxiliary Space
    9. O(n^2) Auxiliary Space
    10. HashMap and HashSet Space
    11. Stack and Queue Space
    12. Recursion Stack Space
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>

using namespace std;


// ============================================================
// 1. O(1) TIME COMPLEXITY
// ============================================================

void constantTime(int n)
{
    int x = n + 10;

    cout << x << endl;
}


// ============================================================
// 2. O(n) TIME COMPLEXITY
// ============================================================

void linearTime(int n)
{
    for(int i = 0; i < n; i++)
    {
        cout << i << " ";
    }

    cout << endl;
}


// ============================================================
// 3. O(log n) TIME COMPLEXITY
// ============================================================

void logarithmicTime(int n)
{
    for(int i = 1; i <= n; i = i * 2)
    {
        cout << i << " ";
    }

    cout << endl;
}


// ============================================================
// 4. O(n log n) TIME COMPLEXITY
// ============================================================

void nLogNTime(int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 1; j <= n; j = j * 2)
        {
            cout << "Hello ";
        }

        cout << endl;
    }
}


// ============================================================
// 5. O(n^2) TIME COMPLEXITY
// ============================================================

void quadraticTime(int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cout << "* ";
        }

        cout << endl;
    }
}


// ============================================================
// 6. GEOMETRIC PROGRESSION EXAMPLE
//
// i = 1, 2, 4, 8, ...
//
// Inner loop runs i times.
//
// Total work:
//
// 1 + 2 + 4 + 8 + ... + n
//
// This is a Geometric Progression.
//
// Overall Time Complexity = O(n)
// ============================================================

void geometricProgression(int n)
{
    for(int i = 1; i <= n; i = i * 2)
    {
        for(int j = 1; j <= i; j++)
        {
            cout << "Hello ";
        }

        cout << endl;
    }
}


// ============================================================
// 7. O(1) AUXILIARY SPACE
//
// Only a fixed number of variables are used.
//
// Auxiliary Space = O(1)
// ============================================================

int sumArray(const vector<int>& arr)
{
    int sum = 0;

    for(int i = 0; i < arr.size(); i++)
    {
        sum += arr[i];
    }

    return sum;
}


// ============================================================
// 8. O(n) AUXILIARY SPACE
//
// Creating an extra array/vector of size n.
//
// Auxiliary Space = O(n)
// ============================================================

vector<int> createExtraArray(int n)
{
    vector<int> temp(n);

    for(int i = 0; i < n; i++)
    {
        temp[i] = i;
    }

    return temp;
}


// ============================================================
// 9. O(n^2) AUXILIARY SPACE
//
// Creating an n x n matrix.
//
// Auxiliary Space = O(n^2)
// ============================================================

vector<vector<int>> createMatrix(int n)
{
    vector<vector<int>> matrix(
        n,
        vector<int>(n)
    );

    return matrix;
}


// ============================================================
// 10. HASHMAP - O(n) AUXILIARY SPACE
// ============================================================

void createHashMap(int n)
{
    unordered_map<int, int> mp;

    for(int i = 0; i < n; i++)
    {
        mp[i] = i * 10;
    }

    cout << "HashMap size: "
         << mp.size()
         << endl;
}


// ============================================================
// 11. HASHSET - O(n) AUXILIARY SPACE
// ============================================================

void createHashSet(int n)
{
    unordered_set<int> st;

    for(int i = 0; i < n; i++)
    {
        st.insert(i);
    }

    cout << "HashSet size: "
         << st.size()
         << endl;
}


// ============================================================
// 12. STACK - O(n) AUXILIARY SPACE
// ============================================================

void createStack(int n)
{
    stack<int> st;

    for(int i = 0; i < n; i++)
    {
        st.push(i);
    }

    cout << "Stack contains "
         << n
         << " elements."
         << endl;
}


// ============================================================
// 13. QUEUE - O(n) AUXILIARY SPACE
// ============================================================

void createQueue(int n)
{
    queue<int> q;

    for(int i = 0; i < n; i++)
    {
        q.push(i);
    }

    cout << "Queue contains "
         << n
         << " elements."
         << endl;
}


// ============================================================
// 14. RECURSION STACK - O(n) SPACE
//
// Each recursive function call creates a stack frame.
//
// Recursion depth = n
//
// Auxiliary Space = O(n)
// ============================================================

void recursionExample(int n)
{
    if(n == 0)
    {
        return;
    }

    cout << n << " ";

    recursionExample(n - 1);
}


// ============================================================
// MAIN FUNCTION
// ============================================================

int main()
{
    int n = 8;

    // --------------------------------------------------------
    // O(1)
    // --------------------------------------------------------

    cout << "O(1) Time Complexity:" << endl;

    constantTime(n);


    // --------------------------------------------------------
    // O(n)
    // --------------------------------------------------------

    cout << "\nO(n) Time Complexity:" << endl;

    linearTime(n);


    // --------------------------------------------------------
    // O(log n)
    // --------------------------------------------------------

    cout << "\nO(log n) Time Complexity:" << endl;

    logarithmicTime(n);


    // --------------------------------------------------------
    // O(n log n)
    // --------------------------------------------------------

    cout << "\nO(n log n) Time Complexity:" << endl;

    nLogNTime(n);


    // --------------------------------------------------------
    // O(n^2)
    // --------------------------------------------------------

    cout << "\nO(n^2) Time Complexity:" << endl;

    quadraticTime(4);


    // --------------------------------------------------------
    // Geometric Progression
    // --------------------------------------------------------

    cout << "\nGeometric Progression Example:" << endl;

    geometricProgression(n);


    // --------------------------------------------------------
    // O(1) Auxiliary Space
    // --------------------------------------------------------

    vector<int> arr = {
        10, 20, 30, 40, 50
    };

    cout << "\nArray Sum:" << endl;

    cout << sumArray(arr) << endl;


    // --------------------------------------------------------
    // O(n) Auxiliary Space
    // --------------------------------------------------------

    cout << "\nCreating Extra Array:" << endl;

    vector<int> temp = createExtraArray(n);

    cout << "Extra Array Size: "
         << temp.size()
         << endl;


    // --------------------------------------------------------
    // O(n^2) Auxiliary Space
    // --------------------------------------------------------

    cout << "\nCreating n x n Matrix:" << endl;

    vector<vector<int>> matrix = createMatrix(4);

    cout << "Matrix Created." << endl;


    // --------------------------------------------------------
    // HashMap - O(n) Space
    // --------------------------------------------------------

    cout << "\nCreating HashMap:" << endl;

    createHashMap(n);


    // --------------------------------------------------------
    // HashSet - O(n) Space
    // --------------------------------------------------------

    cout << "\nCreating HashSet:" << endl;

    createHashSet(n);


    // --------------------------------------------------------
    // Stack - O(n) Space
    // --------------------------------------------------------

    cout << "\nCreating Stack:" << endl;

    createStack(n);


    // --------------------------------------------------------
    // Queue - O(n) Space
    // --------------------------------------------------------

    cout << "\nCreating Queue:" << endl;

    createQueue(n);


    // --------------------------------------------------------
    // Recursion Stack - O(n) Space
    // --------------------------------------------------------

    cout << "\nRecursion Example:" << endl;

    recursionExample(5);

    cout << endl;


    return 0;
}