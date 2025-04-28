#include <iostream>
using namespace std;

// Define maximum board size (adjust as needed)
#define MAX_N 20

int N;
int board[MAX_N][MAX_N];

// Function to check if position (i,j) is under attack
bool attack(int i, int j) {
    // Check vertically and horizontally
    for (int k = 0; k < N; k++) {
        if (board[i][k] == 1 || board[k][j] == 1)
            return true;
    }
    
    // Check diagonally
    for (int k = 0; k < N; k++) {
        for (int l = 0; l < N; l++) {
            if ((k + l == i + j) || (k - l == i - j)) {
                if (board[k][l] == 1)
                    return true;
            }
        }
    }
    return false;
}

// Recursive function to solve N-Queens
bool N_queens(int n) {
    // Base case: all queens placed
    if (n == 0)
        return true;
    
    // Try placing queen in each position
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!attack(i, j) && board[i][j] != 1) {
                board[i][j] = 1;
                
                if (N_queens(n - 1))
                    return true;
                
                // Backtrack if placement doesn't lead to solution
                board[i][j] = 0;
            }
        }
    }
    return false;
}

// Function to print the board
void printBoard() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    cout << "Enter the number of queens: ";
    cin >> N;
    
    // Initialize board with zeros
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            board[i][j] = 0;
        }
    }
    
    // Solve and print result
    if (N_queens(N)) {
        cout << "Solution found:\n";
        printBoard();
    } else {
        cout << "No solution exists for N = " << N << endl;
    }
    
    return 0;
}