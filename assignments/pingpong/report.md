\# XV6 Ping Pong Assignment



Two pipes are created:

\- Parent → Child

\- Child → Parent



The parent sends a byte to the child. The child receives the byte and sends a byte back.



This is repeated N times and performance is measured using uptime().



Output:



pingpong 200000



Exchanges: 200000

Ticks: 547

Exchanges/sec: 36563

