# Linux Command Line, and More Perl  (January 14th, 2009)

The second half of this week’s tutorial will begin teaching you about some basic Linux Command line commands, and some more Perl. We will look at some basic Linux console commands, and try to write simple Perl scripts which accomplish similar tasks. Today we will look at the `ls` command, which should offer us an oportunity to look at arrays in Perl; the `cat` command, for which we will need basic file input; and the `grep` command, which will give us our first look at pattern matching.

## The `ls` Command

The first command we’re going to look at is the `ls` command. Open up a console, and type in the following:

    man ls

This gives you the man page for the `ls` command. The man pages are a thorough and complete description of Linux console commands. Whenever you encounter a command you don’t understand, you should consult its corresponding man page.

The `ls` command provides a list of files in a directory, and can provide extensive information about those files.

### Writing an `ls` Perl Script

In order to write a perl script which behaves like the `ls` command, we’ll have to learn about using arrays in Perl.

#### Arrays in Perl

You’ve encountered arrays before; like in Java, arrays are data structures used to process a colletion of data. Unlike Java, however, in Perl you do not declare the size of an array; if you use an index beyond the length of the array, it is automatically extended as needed.

Syntactically, since they are no scalars, the name of an array-variable does not start with the dollar sign (‘$’) character, but rather the commercial at (‘@’) character. When referencing a value (or _element_) in an array, the syntax is the same as java, using square brackets (‘[' and ']‘) around an integer value.

    # arrays in Perl
    @people = ('Jon', 'Peter', 'Samantha', 'Christina');
    @letters = ('a','b','c');
    $people[4] = 'Sarah';
    $letters[3] = 'd';

Take note; while referencing to the array itself, its identifier starts with the commercial at (‘@’) but when refering to an element in an array, the dollar sign (‘$’) is at the begining of the variabe name.

Like in java, you can use for loops (or foreach loops) to iterate over the contents of an array:

    @words = ('Hello', 'World', 'from', 'Perl');
    for($i=0; $i<@words; $i++) {
    	print $words[$i]." ";
    }
    print "\n";
    foreach $word (@words) {
    	print $word." ";
    }
    print "\n";

#### The glob function

Now that we’ve seen how to use arrays in Perl, we can learn about the `glob` function, so as to write a script which behaves like the Linux command `ls`. The `glob` function lists all files in a directory which match a _wildcard expression_ according to the semantics of the Unix C shell. That may seem confusing, but all you ned to know for now is that the ‘*’ character is a wildcard:

    @plFiles = glob("*.pl");	# generates
    				# a list of files
    				# ending in the .pl extension
    @aFiles = glob("a*");	# ... a list of all files
    			# whose names begin with the letter 'a'
    @dotFiles = glob("*.*");	# ... a list of all files
    				# which contain a '.' in their name
    @allFiles = glob("*"); # a list of all files

So, now, taking everything we’ve learned, we can write a script to behave similarly to the way the `ls` command operates. It will use the `glob(…)` function to obtain an array of the names of files in the current directory, and then iterate over that array using a for loop:

    @allFiles = glob("*"); # a list of all files
    for($i=0; $i<@allFiles; $i++) {
    	print $allFiles[$i]."\n";
    }
    print "\n";

## The `cat` Command

The next command we will look at today is the `cat` command. Before we continue, let’s learn a bit about the `cat` command by consulting the man pages:

    man cat

If you still don’t understand what the `cat` command does, type the following on the command line: (replacing “MyFile.txt” with the name of an existing text file of your choosing)

    cat MyFile.txt

The contents of the file should be generated on screen: the `cat` command displays input from a file, or from the standard keyboard input. We’re going to write a short script which will read text out of a file, and display it onscreen.

### Writing a `cat` Perl script

In order to simulate the funtionality of the `cat` command we will need to learn how to read from a file. Reading from a file will involve more of the filehandles mentioned when we were first learning to receive keyboard input.

Using the `open` we can create our own filehandles. The following code will create a file handle called `IN`, and invoke the line input operator, read in the _first line of text_ from the file `"myFile.txt"` and display it onscreen.

    $filename = "myFile.txt";
    open("IN", "<".$filename);	# we append a '<' at the beginning
    				# of the filename to indicate
    				# Read-Only Access
    $line = <IN>;
    print $line;
    print "\n";

But this only displays one line; to display them all we put the line input operator in a while loop:

    $filename = "myFile.txt";
    open("IN", "<".$filename);
    while($line = <IN>) {
    	print $line;
    }
    print "\n";

You may have noticed that in this example we have an assingment statement being used as a condition in a while statement. In Perl, all operators return value, including assignment. In this particular instance, the assignment will return false once the `IN` filehandle reaches the end of the line.

#### Command Line Arguments

Using the actual `cat` command to display the contents of a file, however, one need only provide the file name when you type in `cat` on the command line:

    cat myFile.txt

Our script doesn’t do this; in order to do this we have to access command line arguments. Perl provides command arguments via the predefined @ARGV array.

    $filename = $ARGV[0];
    open("IN", "<".$filename);
    while($line = <IN>) {
    	print $line;
    }
    print "\n";

## The `grep` Command

The last command for today, we will look at the `grep` command, and use it as a means to introduce very basic pattern matching – one of Perl’s key features – as well as pipes, a key concept in scripting. We will of course begin with consulting the man pages on the `grep` command.

    man grep

The `grep` command allows you to search for a String amidst some input, often a file. If a line of text contains the String, `grep` will output that line to screen. Try it:

    grep seach "MyFile.txt"	# searches MyFile.txt,
    				# displaying all lines
    				# where the word 'search' is found

### Writing a `grep` Perl Script

Before we can write a Perl script which will behave similarly to the `grep` command, we need to learn more about Perl’s string manipulation; more specifically we need to learn about Regular Expressions.

#### Perl Pattern Matching

Perl is a scripting language which has been optimized for working with text and performing String manipulations. One of Perl’s strongest features is its support for Regular Expressions. Pattern matching allows you to very easily search to see if a String contains a particular substring.

    # a pattern match using the pattern binding operator, =~
    if($string =~ /a substring/) {	# this essentially means
    				# "if $string contains 'a substring'"
    	print "The string contains the substring 'a substring'.\n";
    }
    else {
    	print "The string does not contain the substring 'a substring'.\n";
    }
    # the same thing using the negative pattern binding operator, !~
    if($string !~ /a substring/) {	# this essentially means
    				# "if $string does not contain 'a substring'"
    	print "The string does not contain the substring 'a substring'.\n";
    }
    else {
    	print "The string contains the substring 'a substring'.\n";
    }

Between the slashes (‘/’) in the condition of the if statement(s) are regular expressions. Just before them are binding operators, which indicate that we are checking a variable ($string) against a regular expression. This is of course a very simple example, searching literally for the string ‘a substring.’ Take note that the space in the middle of the pattern is not special in any way; it is just another character to match.

We’ll come back to pattern matching in a bit. For now, let’s combine what we’ve learned while writing a `cat` script and what we’ve learned about pattern matching, we can now write a short script which will read the contents of a file and search them for a string.

    $substring = $ARGV[0];	# so the first command line argument
    				# will be the substring for which we search
    $filename = $ARGV[1]; # the second argument is a file name.
    open("IN", "<".$filename);
    while($line = <IN>) {
    	if($line =~ /$substring/) {
    		print $line;
    	}
    }

The `grep` command also provides us with an opportunity to learn about _piping_ input and output on the command line. Let’s search the file `"MyFile.txt"` again, but let’s do it the long way:

    cat MyFile.txt | grep search

The ‘|’ character on the command line denotes piping the output of what’s on the left into what’s on the right.

    cat MyFile.txt | grep search | grep search2

When you pipe input into a Perl script, the piped input replaces the keyboard input as `STDIN`. So what if we wanted to re-write our `grep` script so we can pipe in output, but can still provide a filename as a parameter? First, we replace our filehandle `IN` with `STDIN`; this way we can process input from a pipe, but we can’t provide a filename. We fix this by opening the `STDIN` filehandle if a filename is provided:

    $substring = $ARGV[0];	# so the first command line argument
    				# will be the substring for which we search
    if($ARGV[1]) { # the second argument is a file name.
    	open("STDIN", "<".$ARGV[1]);
    }
    while($line = <STDIN>) {
    	if($line =~ /$substring/) {
    		print $line;
    	}
    }

#### Perl Regular Expressions: Anchors

The syntax of Perl Regular Expressions allows you to specify _anchors_ which constrain where a substring can be in order to match. If you begin your pattern with a carrot (‘^’) character, then the pattern will only match if the String starts with the specified substring. Likewise, if you end your pattern with a dollar sign (‘$’) the pattern only matches if the String ends with the specified substring:

    $name = "Richard";
    if($name =~ /^R/) { # evaluates to true
    	print "The name starts with 'R'\n";
    }
    if($name =~ /R$/) { # evaluates to false
    	print "The name ends with 'R'\n";
    }
    if($name =~ /^d/) { # evaluates to false
    	print "The name starts with 'd'\n";
    }
    if($name =~ /d$/) { # evaluates to true
    	print "The name ends with 'd'\n";
    }

#### Perl Regular Expressions: Character Classes

Regular Expressions allow you to specify _character classes_ and _escape characters_. For example, you can include `[abc]` in a regular expression, and it will match an ‘a’ ‘b’ or a ‘c’ character. Such a grouping, between brackets (‘[' and ']‘) si referred to as a character class.

    if($name =~ / [abc]/) {	# if String $name contains a space
    				# followed by either the letter 'a' 'b' or 'c'
    	print "The name contains";
    	print " a space followed by an 'a' or a 'b' or a 'c'.\n";
    }
    else {
    	print "The name does not contain";
    	print " a space followed by an 'a' or a 'b' or a 'c'.\n";
    }

So what if we wanted to see if a String contained a digit? We could use `[1234567890]` but this can get long to type; imagine trying to match any letter. Since Perl is for lazy people, Perl Regular Expressions provide shortcuts to defining common character classes. So to match any digit, you could write `[0-9]` and to match any lower case letter you could use the `[a-z]` character class.

For common characters, Perl also provides escape sequences:

|Escape Sequence|Matches…|Corresponding Character Class|
|--- |--- |--- |
|\d|Any digit|[0-9]|
|\D|Any non-digit|[^0-9]|
|\w|Any letter, including an underscore|[a-zA-Z_]|
|\W|Any non-letter, non-underscore|[^a-zA-Z_]|
|\s|Any white space|[\r\t\n\f ]|
|\s|Any non-white space|[^\r\t\n\f ]|
|.|_Any_ character|[\d\D\w\W\s\S]|


So lets try using our character classes and escape sequences:

    if($data =~ /^[a-zA-Z]\d/) {
    	print "String data contains a letter followed by  digit.\n"
    }
    if($in =~ / \w /) {
    	print "String in contains a single-letter (or underscore) word.\n";
    }
    if($string =~ /\s\s/) {
    	print "The String contains two consecutive white space characters.\n";
    }

#### Perl Regular Expressions: Quantifiers

The last example above matches two white space characters. What if we wanted to match 100 white space characters? Or either one white space character or none? What if we wanted to match any number of white space characters? Perl regular expression allows us to specify such constraints using _quantifiers_. A quantifier is placed immediately after a character (or character class) to specify how many times it can or should appear for the pattern to match. They include:

|Quantifier|Meaning|
|--- |--- |
|+|Any number of times, consecutively, but at least once|
|*|Any number of times, consecutively, or not at all|
|{2}|Exactly twice|
|{3}|Exactly three times|
|{100}|Exactly 100 times|
|{2,}|At least twice|
|{3,}|At least three times|
|{3,100}|At least three times, at most 100 times|
|?|Exactly once, or not at all.|


So let’s have some examples using quantifiers:

    if($line =~ /^\s*\S+/) {
    	print "The line of text begins with any amount of white space";
    	print "(potentially none)";
    	print " followed by at least one non-white space character.\n";
    }
    if($email =~ /^\w+@\w+\.[a-zA-Z]{2,3}$/) {	# note the '\' before the '.'
    						# to denote that it is not
    						# an escape sequence.
    	print "This email begins with at least one letter (or underscore)";
    	print " followed by an '@', at least one letter (or underscore),";
    	print " a period, and between 2 to three letters.\n";
    }
