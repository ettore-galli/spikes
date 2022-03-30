#include <stdio.h>
#include <math.h>
#include <string.h>

#include <time.h>

int sleepMicro(unsigned int useconds)
{
    struct timespec ts = {
        .tv_sec = useconds / 1000000,
        .tv_nsec = (useconds % 1000000) * 1000};
    return nanosleep(&ts, NULL);
}

void charFrame(char item, int pos, char line[], int lsize)
{

    for (int i = 0; i < lsize; i++)
    {
        if (i == pos)
        {
            line[i] = item;
        }
        else
        {
            line[i] = ' ';
        }
    }
    line[lsize - 1] = '\0';
}

void renderFrame(char *line)
{
    printf("%s\r", line);
    fflush(stdout);
}

void loop(int when)
{
    clock_t trig_time = clock();

    int position = 0;
    int incr = 1;
    const int LINESIZE = 70;
    char line[LINESIZE];
    const char CR = '\r';
    const char LF = '\n';
    const char RULER[] = "....:....1....:....2....:....3....:....4....:....5....:....6....:....7";

    printf("%s\n", RULER);

    while (1)
    {
        clock_t now = clock();

        if (now > trig_time + when * CLOCKS_PER_SEC / 1000)
        {
            trig_time = now;

            charFrame('*', position, line, LINESIZE);
            renderFrame(line);

            position = position + incr;

            if (position >= LINESIZE - 1 || position <= 0)
            {
                incr = -incr;
            }
        }
    }
}

int main()
{
    loop(30);
    return (0);
};

// ....:....1....:....2....:....3....:....5....:....6....:....7.....:....8....:....9....:....0
//                       *                                                *                          ^C

// void loop2(int when)
// {
//     int position = 0;
//     int incr = 1;
//     char line[78];

//     while (1)
//     {
//         clock_t now = clock();
//         sleepMicro(1000000 * when);

//         line[position] = '*';

//         fputs(line, stdout);

//         position += incr;
//         if (position >= sizeof(line) / sizeof(char) || position <= 0)
//         {
//             incr = -incr;
//         }
//     }
// }