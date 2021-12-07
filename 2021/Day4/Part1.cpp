#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

#define NUMBOARDS 100

int main()
{
    int inputarr[NUMBOARDS][5][5];
    int scorearr[NUMBOARDS][5][5];
    int Moves[150];
    int numMoves = 0;
    
    string moves;
    
    ifstream infile("input.txt");
    getline(infile, moves);
    
    stringstream ss(moves);
    while (ss.good()) {
        string substr;
        getline(ss, substr, ',');
        Moves[numMoves] = stoi(substr);
        numMoves++;
    }
    
    int a,b,c,d,e;
    int boardCount = 0;
    int rowCount = 0;
    while (infile >> a >> b >> c >> d >> e){
        inputarr[boardCount][rowCount][0] = a;
        inputarr[boardCount][rowCount][1] = b;
        inputarr[boardCount][rowCount][2] = c;
        inputarr[boardCount][rowCount][3] = d;
        inputarr[boardCount][rowCount][4] = e;
        rowCount++;
        if (rowCount == 5){
            boardCount++;
            rowCount = 0;
        }
    }
    
    for (int a = 0; a < NUMBOARDS; a++){
        for (int b = 0; b < 5; b++){
            for (int c = 0; c < 5; c++){
                scorearr[a][b][c] = 0;
            }
        }
    }
    
    int winningBoard;
    int lastMove;
    for (int a = 0; a < numMoves; a++){
        for (int b = 0; b < NUMBOARDS; b++){
            for (int c = 0; c < 5; c++){
                for (int d = 0; d < 5; d++){
                    if (inputarr[b][c][d] == Moves[a]){
                        scorearr[b][c][d] = 1;
                    }
                }
            }
        }
        
        bool flag = false;
        for (int b = 0; b < NUMBOARDS; b++){
            for (int c = 0; c < 5; c++){
                flag = true;
                for (int d = 0; d < 5; d++){
                    if (!scorearr[b][c][d]){
                        flag = false;
                        break;
                    }
                }
                if (flag){
                    break;
                }
            }
            if (!flag){
                for (int c = 0; c < 5; c++){
                    flag = true;
                    for (int d = 0; d < 5; d++){
                        if (!scorearr[b][d][c]){
                            flag = false;
                            break;
                        }
                    }
                    if (flag){
                        break;
                    }
                }
            }
            if (flag){
                winningBoard = b;
                lastMove = a;
                break;
            }
        }
        if (flag){
            break;
        }
    }
    
    int sumUnmarked = 0;
    for (int a = 0; a < 5; a++){
        for (int b = 0; b < 5; b++){
            if (!scorearr[winningBoard][a][b]){
                sumUnmarked += inputarr[winningBoard][a][b];
            }
        }
    }
    
    cout << sumUnmarked*Moves[lastMove];

    return 0;
}
