#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>

using namespace std;

#define LINES 1000
#define LENGTH 12

int main()
{
    string filename("input.txt");
    int input[LINES][LENGTH];
    
    FILE* input_file = fopen(filename.c_str(), "r");

    char c;
    int ci = 0; //char index
    int ni = 0; //num index
    while ((c = fgetc(input_file)) != EOF) {
       if (c == '\n'){
            ci = 0;
            ni++;
        }else{
            input[ni][ci] = (c=='0'?0:1);
            ci++;
        }
    }
    fclose(input_file);
    
    int z=0;
    int o=0;
    
    int zarr[LENGTH];
    int oarr[LENGTH];
    for (int i = 0; i < LENGTH; i++){
        zarr[i] = 0;
        oarr[i] = 0;
    }
    
    for (int j = 0; j < LENGTH; j++){
        for (int i = 0; i < LINES; i++){
            if (input[i][j]==1){
                o++;
            }else{
                z++;
            }
        }
        if (z > o){
            oarr[j] = 1;
        }else{
            zarr[j] = 1;
        }
        z = 0;
        o = 0;
    }
    
    for (int i = 0; i < LENGTH; i++){
        z = z + zarr[i]*pow(2,LENGTH-i-1);
        o = o + oarr[i]*pow(2,LENGTH-i-1);
    }
    cout << z*o;
    
    return 0;
}