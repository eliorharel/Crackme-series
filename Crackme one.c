#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>


void generateSecretKey(char *key) {
    const char charset[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    int i;

    for (i = 0; i < 4; i++) {
        key[i] = charset[rand() % (sizeof(charset) - 1)];
    }
    key[i++] = '-';

    for (int j = 0; j < 4; j++) {
        key[i++] = charset[rand() % (sizeof(charset) - 1)];
    }
    key[i++] = '-';

    for (int j = 0; j < 4; j++) {
        key[i++] = charset[rand() % (sizeof(charset) - 1)];
    }
    key[i++] = '-';

    for (int j = 0; j < 4; j++) {
        key[i++] = charset[rand() % (sizeof(charset) - 1)];
    }
    key[i] = '\0'; e
}

int main() {
    char userInput[20];
    char labor[20];

    srand(time(NULL));
    generateSecretKey(labor);


    printf("Enter the key (format: XXXX-XXXX-XXXX-XXXX): ");
    fgets(userInput, sizeof(userInput), stdin);
    userInput[strcspn(userInput, "\n")] = 0;


    if (strcmp(userInput, labor) == 0) {
        printf("Success\n");
    } else {
        printf("Try again\n");
    }


    printf("Debug: The key was: %s\n", secretKey);

    return 0;
}
