# Environment Variables in Perl (March 11th, 2009)

In all Unix and Linux systems, processes have their own private set of _environment variables_. When a new process is created it inherits a duplicate of the environment variables associated with the parent process. So, for example, when you type the following on the command line:

    perl soen229-assign-1.pl

The shell spawns a process which executes the Perl interpreter. As such, the Perl interpreter receives a replica of all the Shell's environment variables. Likewise, when the Perl interpreter executes your script, it now gains access to its own set of Environment variables, which are initialized to the values of the Perl interpreter's environment variables.

As such, you can use environment variables to communicate between a process and its child processes.

## The Pre-Defined `%ENV` Hash

When you run a Perl script, there is a hash, `%ENV`, which is populated with your environment variables. The variable names are used as keys, the values as… well, as the values.

Since the environment variables of a process are used to initialize the environment variables of a child process, when you use `system` to execute another Perl script, its `%ENV` hash will contain the same values.

## Why Do We Care?

Becuause they can be important when your writing CGI scripts in Perl.
