# Assignment 1 Pitfalls and Assignment 2 Prep (February 25th, 2009)

Here is a brief summary of the major pitfalls I saw in Assignment #1.

## Variables in RegExs (corrected)

For their find script, everyone's script searches a file to match against a regular expression. The Ms-Dos tool FIND searches for a substring, not a regular expression.

    perl Find.pl "\w" myFile.txt	# should search for a slash followed by a 'w'
    				# but everyone's implementation had it
    				# searching for any word character!
    				# Remember: \w is a character class
    				# in Perl RegExs

Here is the problem, in code:

    $text = "Blah blah blah";
    $var = '\w';
    if($text =~ /$var/) {	# the same as if($text =~ /\w/) which means
    			# "if $text contains any word character or underscore"
    	print "The string contains \\w \n";
    }
    else {
    	print "The string does not contain \\w \n";
    }

The `if` statement will evaluate to true. To fix this we need to escape the special characters in our string, `$var`, such as '\'. There are a lot of special characters though! '[' and ']' and '/' are special characters, as well as '?' and '+' and… etc.

Before we figure out _what_ characters we want to escape, we will figure out _how_ to escape those characters. We will be using Perl's regular expression substitution operator. An example of using the substitution operator follows:

    $string = "No_spaces;_only_underscores.";
    $string =~ s/_/ /g; # here's where we use the substitution.
    print $string."\n";

The `$string` variable gets all its underscores replaced with spaces. The 's' signifies we're using the substitution operator. Between the first slash and the second are a regular expression of what we're substituting, and between the second and the third is a string literal, which is what we will replace it with. The trailing 'g' is a modifier which specifies that we want to apply the substitution all the way through the string. Without it, we'd only substitute the first underscore.

### More on the Substitution Operator's Syntax (optional)

You might think the syntax for the substitution operator is a little strange. Pat of the reason is because the tutorials have only shown you the shorthand for Perl's pattern matching operator. The other part is that the syntax _sis_ strange.

Let's briefly revisit the Pattern Matching operator. The following two if statements mean the same thing:

    if($var =~ /regex/) {

    }

    if($var =~ m/regex/) {

    }

See the 'm' character before the slash, after the binding operator in the second 'if' statement? It means to denote that we're performing pattern **m**atching. If it's not there, it is assumed to be there. So this code…

    $line =~ m/regex/;

... Is saying "take `$line` and apply the regular expression operation 'pattern **m**atch' to it." Likewise, this code…

    $line =~ s/regex/replace/;

... Is saying "take `$line` and apply the regular expression operation '**s**ubstitution' to it."

### RegExs – Escaping Characters Variable

We still need to escape 'special' characters to use a variable in a RegEx ans search for a substring. Do we really need to determine which characters are 'special' and which are not?

Consider this code:

    if($word =~ /S\O\E\N/) {
    	# ...
    }

What does it mean? The RegEx matches any string which contains the substring 'SOEN' despite the slashes. The slashes – when placed before non-special characters – don't have any affect on the RegEx.

So if we replace every non-letter character in a string with a slash followed by itself, we should be able to solve our problem with using a variable in a RegEx while searching for a substring.

    $text = "Blah blah blah";
    $var = '\w';
    $var =~ s/([^a-zA-Z])/\\$1/g;	# we replace any non-letter character [^a-zA-Z]
    				# with a slash \ and itself $1
    				# Remember:
    				# since the [^a-zA-Z] is in brackets,
    				# that character is stored in $1
    if($text =~ /$var/) {	# no longer the same as if($text =~ /\w/)
    			# so it now means,
    			# "if $text contains the substring '\w'"
    	print "The string contains \\w \n";
    }
    else {
    	print "The string does not contain \\w \n";
    }

Why only non-letter characters? Because a slash followed by a letter character is the syntax for a character class.

## Confusion: Filehandles

There seems to be a lot of confusion about filehandles. First of all, despite its deceptive name, a filehandle is _not_ a file. A filehandle represents an IO connection. If it helps, think of it as being similar to either a `Scanner` object or a `PrintWriter` object you'd use in Java. Here are some examples:

### Reading from a File

    open("INFH", "<some-file.txt");
    $input = <INFH>;
    print $input;
    $input = readline(INFH);	# same as $input = <INFH>;
    print $input;

In the code above, I am creating a filehandle; it is a connection between my Perl script and file 'some-file.txt' which grants my script only read-only access to the file. If I were to conceptually equate this to something similar in Java, I might write it like this: (remember, this is **not** the same code in Java; it is only an analagy to help you understand)

    Scanner INFH = new Scanner(new FileInputStream("some-file.txt"));
    String input = INFH.nextLine();
    System.out.print(input);
    String input = INFH.nextLine();
    System.out.print(input);

### Reading from STDIN

    print "What is your name? ";
    $input = <STDIN>;
    print "Hello ".$input;
    print "\n";

In the code above, I don't create a file handle; I am using the pre-defined STDIN filehandle, which represents the standard input. STDIN is a connection between my Perl script and some form of input, provided by whatever process started the execution of the script. Usually, the shell starts the script, so the shell provides that input. Typically the shell gets that input from the keyboard. If I were to conceptually equate this to something similar in Java, I might write it like this: (remember, this is **not** the same code in Java; it is only an analagy to help you understand)

    System.out.print("What is your name? ");
    Scanner STDIN = new Scanner(System.in);
    String input = STDIN.nextLine();
    System.out.println("Hello ".input);

### Writing to a File

    open("FILE", ">out.txt");
    print FILE "I am writing to a file.\n";
    close FILE;

In the code above, I am creating a filehandle; it is a connection between my Perl script and file 'out.txt' which grants my script write-only access to the file. If the file existed before we executed the script, the file's contents are lost and replaced with the output from the script. If the file did not exist, it is created. If I were to conceptually equate this to something similar in Java, I might write it like this:

    PrintWriter FILE = new PrintWriter(new FileOutputStream("out.txt", false));
    FILE.print("I am writing to a file.\n");
    FILE.close();

### Appending to a File

    open("FILE", ">>out.txt");
    print FILE "I am writing to a file.\n";
    print FILE "The test is appended to the end of the file.\n";
    close FILE;

In the code above, I am creating a filehandle; it is a connection between my Perl script and file 'out.txt' which grants my script write-only access to the file. If the file existed before we executed the script, the file's contents are preserved, and the output from the script is appended to the end of the file. If the file did not exist, it is created. If I were to conceptually equate this to something similar in Java, I might write it like this:

    PrintWriter FILE = new PrintWriter(new FileOutputStream("out.txt", true));
    FILE.print("I am writing to a file.\n");
    FILE.print("The test is appended to the end of the file.\n");
    FILE.close();

### Writing to STDOUT

    print "I am writing to STDOUT,\n";
    print STDOUT "which is probably the screen.\n";	# by default,
    						# print sends output
    						# to STDOUT, though
    						# you can specify
    						# another filehandle to
    						# send output elsewhere

In the code above, I don't create a file handle; I am using the pre-defined STDOUT filehandle, which represents the standard output. So STDOUT is a connection between my Perl script and some form of output, controlled by whatever process started the script. Usually, the shell starts the script, and the shell usually sends the output to the screen. If I were to conceptually equate this to something similar in Java, I might write it like this: (remember, this is **not** the same code in Java; it is only an analagy to help you understand)

    System.out.print("I am writing to STDOUT,\n");
    System.out.print("which is probably the screen.\n");

## Accepting Either Piped Input or a Filename

Several assignments used the `-t` filehandle to determine if the script it receiving piped input. While this is good, most assignments also used it in a very big if-else, and wrote up the same code twice using different filehandles. In [this tutorial](/tutoring/soen229/tutorials/linux-and-perl) we saw a way in which we can re-assign a filehandle:

    $substring = $ARGV[0];
    if($ARGV[1]) { # the second argument is a file name.
    	open("STDIN", "<".$ARGV[1]);	# The STDIN filehandle
    					# is now associated
    					# with a file instead
    					# of the standard input
    }
    while($line = <STDIN>) {
    	if($line =~ /$substring/) {
    		print $line;
    	}
    }

Here's a similar concept to this, in Java: (remember, this is **not** the same code in Java; it is only an analagy to help you understand)

    if(argv[0]!=null&&argv[0]!="") {
    	System.setIn(new FileInputStream(argv[0]));
    }
    Scanner STDIN = new Scanner(System.in);
    while(…) {
    	...
    }

If you are uncomfortable with the idea of re-assigning the STDIN filehandle, you can instead use another filehandle as an alias for STDIN.

    $substring = $ARGV[0];
    if($ARGV[1]) { # the second argument is a file name.
    	open("IN", "<".$ARGV[1]);
    }
    else {
    	open("IN", "<&STDIN"); # now IN is an alias for STDIN
    }
    while($line = <IN>) {
    	if($line =~ /$substring/) {
    		print $line;
    	}
    }
    close IN;

Here's a similar concept to this, in Java: (remember, this is **not** the same code in Java; it is only an analagy to help you understand)

    Scanner IN;
    if(argv[0]!=null&&argv[0]!="") {
    	IN = new Scanner(new FileInputStream(argv[0]));
    }
    else {
    	IN = new Scanner(System.in);
    }
    while(…) {
    	...
    }

## Control Flow: `elsif`

Everyone gets that in Perl, you have to include braces {} after an `if` statement, or `while` statement, or in a `for` loop. As such, though, I saw a lot of code which looked like this:

    if($condition1) {
    	#…
    }
    else {
    	if($condition2) {
    		#…
    	}
    	else {
    		if($condition3) {
    			#…
    		}
    		else {
    			#…
    		}
    	}
    }

So I figured it would be best to at least mention that Perl has an `elsif` control flow construct, which makes code look much nicer.

    if($condition1) {
    	#…
    }
    elsif($condition2) {
    	#…
    }
    elsif($condition3) {
    	#…
    }

## Notes on Command Line Interpreters

### Search Path

A command line interpreter has a specific directory in which it stores and 'searches' for executable commands. This seems to be confusing people quite a bit.

First of all, some students checked for the existance of an executable file in one directory and then executed it from another. This is incredibly **wrong**:

    $file = $searchpath.$commandFileName;
    if(-e $file) {
    	system("scripts/".$commandFileName); # WRONG!
    }
    else {
    	print "That is not a recognized command.
    }

In order to avoid this sort of thing, hard code your search path to be somewhere in a completely different place from your command line interpreter script, and independant of your current working directory.

Additionally, the use of the name "search path" seems to be causing a lot of confusion. There were a lot of loops and `glob` functions used to find an executable file corresponding to a command. Consider this; if you have the name of a directory (your search path) and the name of the command you're looking for _in_ that directory… are you really _searching_ or just testing for the existance of a file?

Consider the real Linux command line; type in `which ls` and you should see that the executable file for the `ls` command is '/bin/ls'. Take note that there is no file extension on this executable file. We combine the name of a directory (the search path '/bin') and the command name (using 'ls' as a filename) and we get the full path to the executable file.

## Perl Functions: `exec`

The built-in Perl function `exec` replaces the currently executing program (the script) with another, leaving the process intact. It is a direct interface to the system call of the same name.

    exec("ls -l /home/");	# this will halt the execution
    				# of the current Perl script
    				# and replace it with ls.

If `exec` is able to execute, the script _does not_ finish executing. A program that calls `exec` gets 'wiped clean.'

    exec("ls -l /home/");
    print "Unable to exec(…)";	# this line of code is not executed
    				# unless exec(…) fails due to permissions
    				# or there being no such program to execute

## Perl Functions: `fork`

The built-in `fork` function creates a child process. For the parent process, it returns the process id of the newly created child.

    if($pid = fork()) {
    	# the parent process executes code in this block.
    	waitpid($pid,0); # wait for the child process to finish executing.
    }
    else {
    	# the child process executes the code in this block.
    }

You can read more about `fork` and `exec` [here](http://books.google.ca/books?id=lNVHi3TunxsC&pg=PA243&lpg=PA243&dq=learning+perl+fork&source=bl&ots=2ZSWU7686O&sig=dawlJgc6eRR7-U_styHWLxTpoio&hl=en&ei=w3ulSZDnCITFnQec4sSmBQ&sa=X&oi=book_result&resnum=1&ct=result).
