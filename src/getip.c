#include <stdio.h>
#include <stdlib.h>

int get-ip(){
    printf("Your public ip address: \n");
    int short i;
    for(i=0;i<1;i++){
        system("curl 'api.ipify.org'");
    }
    return 0;
}

int short main(int argc, char * const argv[]){
    #ifdef __linux__
        int short i;
        for(i=0;i<1;i++){
            get-ip();
        }
    #endif
    return 0;
}
