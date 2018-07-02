# Simple Web Server

use Socket;
use IPC::Open2;

 my $server_port = 8080;

# make the socket
 socket(SERVER, PF_INET, SOCK_STREAM, getprotobyname('tcp'));

# so we can restart our server quickly
 setsockopt(SERVER, SOL_SOCKET, SO_REUSEADDR, 1);

# build up my socket address
 my $my_addr = sockaddr_in($server_port, INADDR_ANY);
 bind(SERVER, $my_addr)
     or die "Couldn't bind to port $server_port : $!\n";

# establish a queue for incoming connections
 listen(SERVER, SOMAXCONN)
     or die "Couldn't listen on port $server_port : $!\n";

# accept and process connections
 while (my $request = accept(CLIENT, SERVER)) {

     $pid = open2(">&CLIENT", "<&CLIENT", @ARGV);

     waitpid($pid, 0);
     
     # send them a message, close connection
     close CLIENT; 

 }

close(SERVER);