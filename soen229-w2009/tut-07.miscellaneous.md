# Miscellaneous (February 18th, 2009)

The [Current] Working Directory

When any process executes on a system, it is associated with a _working directory_ (or current working directory) which is where any files it creates or manipulates using a simple name will be saved, and likewise any files it tries to read using a simple name will be found. Any time a file is created, manipulated or saved using a relative path, the path is relative to the working directory.

### On the Linux Command Line: The `pwd` Command

You might wonder, how do you see your [current] working directory in Linux? Oftentimes the prompt that a command line interpreter presents you with is in fact the current working directory. However, when this is not the case, Linux provides you with a command to **P**rint the **W**orking **D**irectory, `pwd`. (who names these things? I'm in my last semester of soen, and never managed to figure out what pwd stood for until yesterday…)

    r_leguen@alamanni

### In Perl Code

In Perl, we have a function which returns the **C**urrent **W**orking **D**irectory, called `cwd`. It is not included or available by default, however. If we write the following Perl script and attempt to run it using the interpreter (or chmod it and then execute it) we'll get an error about an 'undefined subroutine':

    $currentWorkingDir = cwd(); # this script doesn't work
    print $currentWorkingDir."\n";

So how do we actually use this function?

### The Cwd Perl Module

In the same way that in Java we could import packages (such as `java.util`) to gain access to more classes (such as the `Scanner` class, which is in package `java.util`) Perl allows us to use **modules**. A module is a file containing related functions designed to be used by programs and other modules.

In this case we need a module called `Cwd`:

    use Cwd;	# this line of code allows us access to the cwd function,
    		# and a few others which we're not talking about right now…
    $currentWorkingDir = cwd(); # now it works
    print "The current working directory is:\n".$currentWorkingDir."\n";

## File Tests

### Does a File Exist?

So let's say you write a script which is supposed to search the contents of a file for a particular substring. For usability's sake, you might want to make sure that the file exists, no? And if it doesn't, we should output some error message such as 'File Not Found', no?

Perl provides a number of _file tests_ which allow a programmer to determine if a file exists. In terms of syntax, a file test is always written as a dash ('-') followed by a single character and then the filename. The filename should be either a string literal or a scalar variable.

    $filename = "MyFile.txt";
    if(-e $filename) {
    	# the file exists!
    }
    else {
    	print "File Not Found – ".$filename;
    }
    # I could have done the same thing without the variable
    if(-e "MyFile.txt") {
    	# the file exists!
    }
    else {
    	print "File Not Found – MyFile.txt";
    }

Likewise, you can determine if a file's permissions will allow it to be read, written, or executed with the `-r`, `-w` and `-x` file tests, respectively:

    if(-r "MyFile.rb") {
    	# the file can be read
    }
    else {
    	print "This file cannot be read.";
    }
    if(-w "MyFile.rb") {
    	# the file can be written to
    }
    else {
    	print "This file cannot be written to.";
    }
    if(-x "MyFile.rb") {
    	# the file can be executed directly
    }
    else {
    	print "This file cannot be executed directly. ";
    	print "If it is a script, use an interpreter to execute it.";
    }

Generally speaking, when just performing basic reading and writing to/from a text file, you can rely on the `open` function returning true or false:

    if(open("IN", ">myFile.txt")) {
    	print "Reading the file\n";
    }
    else {
    	print "Unable to open file.\n";
    }
