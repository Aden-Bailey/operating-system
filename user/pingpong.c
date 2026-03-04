#include "kernel/types.h"
#include "kernel/stat.h"
#include "user/user.h"

#define TICKS_PER_SEC 100   // xv6-riscv typically uses 100 ticks/sec

int
main(int argc, char *argv[])
{
  int p2c[2], c2p[2];
  char b = 'x';

  int n = 100000;           // default iterations
  if(argc >= 2){
    n = atoi(argv[1]);
    if(n <= 0){
      fprintf(2, "usage: pingpong [positive N]\n");
      exit(1);
    }
  }

  if(pipe(p2c) < 0 || pipe(c2p) < 0){
    fprintf(2, "pipe failed\n");
    exit(1);
  }

  int pid = fork();
  if(pid < 0){
    fprintf(2, "fork failed\n");
    exit(1);
  }

  if(pid == 0){
    // child
    close(p2c[1]);
    close(c2p[0]);

    for(int i = 0; i < n; i++){
      if(read(p2c[0], &b, 1) != 1){
        fprintf(2, "child read failed\n");
        exit(1);
      }
      if(write(c2p[1], &b, 1) != 1){
        fprintf(2, "child write failed\n");
        exit(1);
      }
    }

    close(p2c[0]);
    close(c2p[1]);
    exit(0);
  } else {
    // parent
    close(p2c[0]);
    close(c2p[1]);

    int start = uptime();

    for(int i = 0; i < n; i++){
      if(write(p2c[1], &b, 1) != 1){
        fprintf(2, "parent write failed\n");
        exit(1);
      }
      if(read(c2p[0], &b, 1) != 1){
        fprintf(2, "parent read failed\n");
        exit(1);
      }
    }

    int end = uptime();
    int ticks = end - start;
    if(ticks < 1) ticks = 1;

    wait(0);
    close(p2c[1]);
    close(c2p[0]);

    int exchanges = n;
    int ex_per_sec = (exchanges * TICKS_PER_SEC) / ticks;

    printf("%d: received ping\n", getpid());
    printf("%d: received pong\n", getpid());
    printf("Exchanges: %d, Ticks: %d, Exchanges/sec: %d\n",
           exchanges, ticks, ex_per_sec);

    exit(0);
  }
}