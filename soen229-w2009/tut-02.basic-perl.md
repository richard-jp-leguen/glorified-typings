# Basic Perl Programming  (January 14th, 2009)

The first half of this week’s tutorial focuses on Perl programming.

## What is Perl?

Perl is a scripting language (or a programming language, depending on one’s point of view), created by [Larry Wall](http://www.wall.org/~larry/) in the mid-1980s. It is nicknamed the “Pathological, Eclectic Rubbish Lister” and once you encounter your first bug and see an error message you may understand why.

Perl is a language meant for lazy, lazy people, and its syntax is highly flexible so scripts can be written in as little time possible. This means, however, that it can be challenging to learn Perl, and even more challenging to understand a script someone else has written.

## Script #1: Hello World

Sure enough, we’re starting with Hello World script. This script will be fairly short, so I’m just going to present it in whole…

### The Code

    #! /usr/bin/perl
    # My first perl program; Hello World
    print "Hello world!\n"; # This line will generate output on the screen.

### The Code Explained

So what do we see here? The first line probably makes no sense to you, and don’t worry about it; we’ll talk about that when it comes to running the code.  
The second line is a comment; Perl does not use the C-style comments you’ve seen in Java. Rather, in Perl, you will only be able to insert _line comments_ into your code using an octothorpe (#) character.

But Hello World programs are so lame we’re not going to bother running this code until we’ve made it a little more interesting.

## Script #2: Hello World Variation

We now are going to write a little program which will prompt for one’s name, and then greet the user with a Hello message.

### The Code

So we will start with the same Hello World script we’ve written, but we’re going to make a few minor changes:

    #! /usr/bin/perl
    # My first Perl program; Hello World
    $name = "world\n";
    print "Hello ".$name; # This line will generate output on the screen.

So what did we do? First, we added a line of code `$name = "world";` which looks very much like an assignment statement, because it is. Take note; when using Perl, scalar variables (meaning numerical values and Strings) must have names which begin with a dollar sign ($) character.

You should also take note that variables in Perl do not need to be declared.

The next change is that we are now outputting a concatenation of the string literal `"Hello "` and the scalar variable `$name`. In Perl, you cannot add strings together with the ‘+’ operator, as you do in Java. This is because in Perl, scalar variables are typeless, and could be either a String or a numerical value. The ‘+’ operator will perform numerical addition, while the ‘.’ operator will perform String concatenation.

This script, however, still doesn’t prompt for the user’s username. To achieve this, we change the assignment statement:

    #! /usr/bin/perl
    # My first Perl program; Hello World
    print "What is your name? ";
    $name = <STDIN>;
    print "Hello ".$name; # This line will generate output on the screen.

Here we see our first Perl _filehandle_, `STDIN`. We’ll have more on filehandles later; for now, whenever you need to get keyboard input, you can assign it to a variable by invoking the _line input operator_ on pre-assigned filehandle `STDIN` by like so:

    $input = <STDIN>;
    chomp($input);	# the chomp(…) function removes the newline character
    		# from the end of a String, if its there.

### Running your Perl scripts

So we’ve _written_ two Perl scripts… now what? Now we run them! But how?

Save your Hello World variation script as `MyFirstScript.pl`.

Perl is an interpreted language, which is why I choose to refer to it as a scripting language. You never have to compile Perl code; rather go to the command line and type the following:

    perl MyFirstScript.pl

You can also run a Perl script without invoking the interpreter directly; by including `#! /usr/bin/perl` at the top of your script, you could also execute your script directly. It wouldn’t even need to have a `.pl` extension, but you would have to change the file’s permissions with the `chmod` console command to be able to execute it.

    ./MyFirstScript.pl

Click [here](/tutoring/soen229/tutorials/linux-and-perl) for the next part of this week’s tutorial.
