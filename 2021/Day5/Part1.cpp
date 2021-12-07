#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream infile("input.txt");
    int a,b,c,d;
    int amax=0;
    int bmax=0;
    int cmax=0;
    int dmax=0;
    string test;
    int arr[1000][1000];
    for (int i = 0; i < 1000; i++){
        for (int j = 0; j < 1000; j++){
            arr[i][j] = 0;
        }
    }
    while (infile >> a >> b >> c >> d){
        if (a==c){
            if (b>d){
                int temp = b;
                b = d;
                d = temp;
            }
            for (int i = b; i <= d; i++){
                arr[i][a]++;
            }
        }else if (b==d){
            if (a>c){
                int temp = a;
                a = c;
                c = temp;
            }
            for (int i = a; i <= c; i++){
                arr[b][i]++;
            }
        }
    }
    int count = 0;
    for (int i = 0; i < 1000; i++){
        for (int j = 0; j < 1000; j++){
            if (arr[i][j]>1){
                count++;
            }
        }
    }
    cout << count;

    return 0;
}
