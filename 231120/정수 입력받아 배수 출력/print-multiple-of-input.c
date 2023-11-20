#include <stdio.h>

int main() {
    int n = 0;
    scanf("%d", &n);
    for(int i=1;i<=5;i++){
        printf("%d ", n*i);
    }
    return 0;
}