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
    
    int o1=0;
    int o2=0;
    int z1=0;
    int z2=0;
    
    int zarr[LENGTH];
    int oarr[LENGTH];
    for (int i = 0; i < LENGTH; i++){
        zarr[i] = 0;
        oarr[i] = 0;
    }
    
    for (int j = 0; j < LENGTH; j++){
        int ocounter = 0;
        int zcounter = 0;
        for (int i = 0; i < LINES; i++){
            bool oflag = true;
            bool zflag = true;
            for (int k = 0; k < j; k++){
                if (input[i][k] != oarr[k]){
                    oflag = false;
                }
                if (input[i][k] != zarr[k]){
                    zflag = false;
                }
            }
            if (input[i][j]==1 && oflag){
                o1++;
                ocounter++;
            }
            if (input[i][j]==0 && oflag){
                z1++;
                ocounter++;
            }
            if (input[i][j]==1 && zflag){
                o2++;
                zcounter++;
            }
            if (input[i][j]==0 && zflag){
                z2++;
                zcounter++;
            }
        }
        cout << ocounter << " " << zcounter << endl;
        if (ocounter == 1){
            for (int l = 0; l < LINES; l++){
                bool oflag = true;
                for (int k = 0; k < j; k++){
                    if (input[l][k] != oarr[k]){
                        oflag = false;
                    }
                }
                if (oflag){
                    for (int i = j; i < LENGTH; i++){
                        oarr[i] = input[l][i];
                    }
                }
            }
        }
        if (zcounter == 1){
            for (int l = 0; l < LINES; l++){
                bool zflag = true;
                for (int k = 0; k < j; k++){
                    if (input[l][k] != zarr[k]){
                        zflag = false;
                    }
                }
                if (zflag){
                    for (int i = j; i < LENGTH; i++){
                        zarr[i] = input[l][i];
                    }
                }
            }
        }
        if (o1 >= z1 && ocounter != 1){
            oarr[j] = 1;
        }
        if (z2 > o2 && zcounter != 1){
            zarr[j] = 1;
        }
        o1=0;
        o2=0;
        z1=0;
        z2=0;
        ocounter=0;
        zcounter=0;
    }
    
    for (int i = 0; i < LENGTH; i++){
        z1 = z1 + zarr[i]*pow(2,LENGTH-i-1);
        o1 = o1 + oarr[i]*pow(2,LENGTH-i-1);
        cout << oarr[i];
    }
    cout << endl;
    for (int i = 0; i < LENGTH; i++){
        cout << zarr[i];
    }
    cout << endl << z1*o1;
    
    return 0;
}
