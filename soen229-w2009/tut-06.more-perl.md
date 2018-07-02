# A Lot More Perl (January 28th, 2009)

## The Text-Analyzer Script

To begin, we're going to write our text-analysis script to look very similar to our `cat` command script (see the [tutorial on Linux and Perl](/tutoring/soen229/tutorials/linux-and-perl) from January 14th) except that we will read from `STDIN`:

    while($line = <STDIN>) {

    }
    print "\n";

Until we write a script to download a document and pipe it into our analyzer, we'll need to do it manually. Look at [last week's tutorial](/tutoring/soen229/tutorials/perl-regex) to see how to use the Linux command line tool `wget` to download the document to a file. We'll then pipe its content like so:

    perl TextAnalyzer.pl < tutorial-2.html

As it stands, this just prints the contents of the HTML document to screen. Our end goal is for our analyzer to display the number of times words appeared in the text document – words being defined as a string of one or more letter characters or underscores – as well as whether any of those words were palindromes. In order to do this, we'll start by turning the input we get from `STDIN` into an array of words. How can we do this? With the `split` operator.

### The `split` Operator

    @data = split /:/, "A:B:C"; # @data is now {'A','B','C'}
    @nonLetters = split(/\d/, "1qa2ws3ed4rf5tg");
    	# @nonLetters is now {'qa','ws','ed','rf','tg'}
    @arr = split(/\s/, $txt);

Take note that the first parameter to the `split` operator is a pattern. So, like in the second example, you can split on something like 'decimals,' or any other pattern you can think of. (see last week's tutorial for more on Patterns)

To turn that array back into a scalar variable, you can use the `join` operator:

    @data = split /:/, "A:B:C"; # @data is now {'A','B','C'}
    print join(",\nthen the letter");

So how can we use these operators to sift out the words in our input? Well, we've already stated we're defining a word as a string of any letter characters, or underscores. Looking at last week's tutorial, we can see that the `\w` character class matches any letter character or underscore, and that its 'inverse,' `\W`, matches anything else. So we can try this:

    while($line = <STDIN>) {
    	@in = split(/\W/, $line);
    }
    print "\n";

Now we want to count how many times each word appears. In order to achiev this goal, we need to learn about Hashes.

### Hashes

A Hash is very similar to an array. Being like an array, q Hash is not a scalar variable, and therefore we don't identify it with the dollar character ('`$`') but rather with a percent character ('`%`'). Before specifying how a Hash differs from an array, I'm going to show the an example which emphasises how it's similar to an array:

    @myArray;
    $myArray[0] = "Hello";
    $myArray[1] = "World!";
    %myHash;
    $myHash{1} = "Hello"; # We use { } as opposed to [ ] to index a hash
    $myHash{2} = "World!";

Here's where Hashes differ from Arrays:

    $myHash{"index"} = "Whoa!";
    $myHash{"richard"} = "Awesome tutor!";
    $myHash{"assignment 1"} = "Will be hard!";

A Hash takes character strings as indexes, as opposed to only integers. Again, a hash works like an array, but you can use character-string indexes.

So, in order to count how often words occur, we're going to increment a value in the Hash every time we encounter that word:

    %myHash{"word"}++;

But, since I want to cram even _more_ material down your throats, we're also going to perform this logic in a subroutine.

### Defining Subroutines in Perl

We'll call this subroutine `countWords`.

    while($line = <STDIN>) {
    	chomp($line);
    }

    sub countWords() {
    	print "We called a subroutine!\n";
    }

So we've written our first subroutine. As you can see, in Perl, you declare a subroutine with the `sub` keyword. If we want to call the routine, we type its name after an ampersand ('&') character.

    while($line = <STDIN>) {
    	chomp($line);
    	&countWords($line); # <- I'm calling my subroutine
    }

    sub countWords { # Hey! I didn't include brackets this time!
    	print "We called a subroutine!\n";
    }

#### Passing Arguments to Subroutines

We've seen a few of the functions which are native to Perl, such as `print` or `glob`. Both of these take arguments (or parameters) in brackets. How do we do the same for our user-defined subroutines?

Unfortunately, Perl syntax doesn't allow you to name arguments in you subroutines signature, like you do in Java:

    sub countWords($arg) { # won't work! $arg will always be null.
    	print "We called a subroutine, \$arg is $arg!\n";
    }

In the same way that Perl has a pre-defined array, @ARGV, which provides us with command line arguments from the console. Likewise, when you call a subroutine, then @_ array contains all the arguments (or parameters) which were passed into the subroutine.

    sub mySubroutine() {
    	for($i=0; $i<@_; $i++) {
    		print $_[$i]." ";
    	}
    	print "\n";
    }

    &mySubroutine("We called a subroutine!");
    &mySubroutine("We", "called", "a", "subroutine,", "again!");

Since subroutines are called using an ampersand ('&') character, we can even define subroutines with the same names as built-in Perl functions.

    sub print() {
    	for($i=0; $i<@_; $i++) {
    		print $_[$i]." ";
    	}
    	print "\n";
    }

    &print("We called a subroutine!");

There are more rules for defining subroutines in Perl, but they can get a little too complicated, and we need to move on to other topics this tutorial. So for now, this will do.

## The Text-Analyzer Script – Counting Words

So let's get back to our text-analyzer script. We're going to write a subroutine which take a line of text as a parameter, and keep track of how often some words appear.

    %wordCount;

    while($line = <STDIN>) {
    	chomp($line);
    	&countWords($line);
    }
    print "\n";
    foreach $key (keys %wordCount) {
    	print "$key => $wordCount{$key}\n";
    }

    sub countWords() {
    	my $line = $_[0];	# The @_ array contains the argument
    			# passed into this subroutine
    	my @line_words = split(/\W/, $line);
    	foreach my $word (@line_words) {
    		if($wordCount{$word}) {
    			$wordCount{$word}++;
    		}
    		else {
    			$wordCount{$word} = 1;
    		}
    	}
    }

So this looks like it should count the number of words in the document. You'll need to notice two relatively important points;

1.  # The variables in the subroutine are all declared using the '`my`' keyword.
2.  The variable `%wordCount` is used in the subroutine, even though it looks like it's out of scope.

The important thing to remember with Perl subroutines is that all variables are global. So, when we assign the first element of the @_ array to a variable named `$line` this actually refers to the same `$line` from the while loop earlier in the code. In order to get around this, we use the '`my`' keyword to declare variables as being local as opposed to global.

Once again, for emphasis. In Perl, all variables are global in scope by default. So if you write a script which includes a subroutine such as this:

    sub forloop() {
    	for($i=0;$i<10;$i++) {
    		print "$i";
    	}
    }

    for($i=0; $i<10; $i++) {
    	&forloop();
    }

The output will only be the numbers 0-9, as both for loops manipulate the same `$i` variable.

## The Text-Analyzer Script – Finding a Palindrome

So now we want to write another subroutine which will determine if a word is a palindrome (a word spelled the same way backwards as forwards) so we'll start with the basics; declaring the subroutine.

    sub is_a_palindrome() {
    	my $word = $_[0];
    	# we have now declared our subroutine
    }

To determine if the string argument is a pallindrome, we're going to use the `substr` function. The `substr` function takes three arguments: the full string, the index of the first character of our substring, and the length of our substring.

    $drink = "fruit juice";

    print substr $drink, 0, 3; # returns 'fru'
    print substr($drink, 3, 5); # returns 'it ju'
    print substr $drink, -3, 3; # returns 'ice'

So we're going to fill out our palindrome subroutine now; it should check whether the first character is the same as the last character, and then that the second is the same as the second to last. We saw above that in order to get characters at the end of our string, we can specify a negative index at which to start. So, if we want the n<sup>th</sup> character in a string, we could use `substr($string, $n, 1)` and if we wanted the n<sup>th</sup> from last, we could use `substr($string, -($n+1), 1)`. So here's the code:

    sub is_a_palindrome() {
    	my $word = $_[0];
    	for(my $n=0; $n<length($word)/2; $n++) {
    		if(substr($word, $n, 1) ne substr($word, -($n+1), 1)) {
    			return false;
    		}
    	}
    	return true;
    }

So, we'll now use it in our Text-Analyzer program. I've written another subroutine which splits a line into words and checks if each of them is a palindrome.

    %wordCount;
    %palindromes;

    while($line = <STDIN>) {
    	chomp($line);
    	&countWords($line);
    	&findPalindromes($line);
    }
    print "\nThis is how often words appeared:\n";
    foreach $key (keys %wordCount) {
    	print "\t$key => $wordCount{$key}\n";
    }
    print "\nThese words are palindromes:\n";
    foreach $key (keys %palindromes) {
    	print "\t$key\n";
    }

    sub countWords() {
    	my $line = $_[0];	# The @_ array contains the argument
    			# passed into this subroutine
    	my @line_words = split(/\W/, $line);
    	foreach my $word (@line_words) {
    		if($wordCount{$word}) {
    			$wordCount{$word}++;
    		}
    		else {
    			$wordCount{$word} = 1;
    		}
    	}
    }

    sub findPalindromes() {
    	my $line = $_[0];	# The @_ array contains the argument
    			# passed into this subroutine
    	my @line_words = split(/\W/, $line);
    	foreach my $word (@line_words) {
    		if(&is_a_palindrome($word)) {
    			$palindromes{$word} = 1;
    		}
    	}
    }

    sub is_a_palindrome() {
    	my $word = $_[0];
    	for(my $n=0; $n<length($word)/2; $n++) {;
    		if(substr($word, $n, 1) ne substr($word, -($n+1), 1)) {
    			return 0;
    		}
    	}
    	return 1;
    }

## The Downloader Script

We're now goig to write another Perl script which will call `wget` and automatically pipe the document we download into the Text-Analyzer. (since the Text-Analyzer reads from `STDIN`)

The first way we could do this is using the `system()` function. The `system` function allows you to execute console commands from your Perl script:

    $status = system("wget -q -O – http://www.google.ca | perl TextAnalyzer.pl");

This, however, is the easy way. We instead will be using the `open` function. Remember when we used `open`, how you had to prefix the name of your file with a 'mode'?

    open "FILEHANDLE", "<myfile.txt";	# I'm only reading this file,
    					# as denoted by the '<' mode
    open "FILEHANDLE", ">myfile.txt";	# I'm overwriting this file,
    					# as denoted by the '>' mode
    print FILEHANDLE, "I'm writing to file.";
    open "FILEHANDLE", ">>myfile.txt";	# I'm appending to this file,
    					# as denoted by the '>>' mode

We can open a process using the `open` function, by using special pipe modes:

    open PIPEIN, "ls -al |";	# note that the mode
    				# is at the end when
    				# readin from a pipe
    while($line = <PIPEIN>) {
    	print $line;
    }
    close(PIPEIN);

    open PIPEOUT, "| cat";
    print PIPEOUT "This will write to the cat command's STDIN";
    close PIPEOUT;

So we're going to use our two examples – how read from a program's `STDOUT` and how to write to a program's `STDIN` – to write a script which will automatically download a document from the internet and then analyze it using the Text-Analyzer script.

In order to have `wget` print the contents of a document to screen, we use the `-O -` (Output) option, and in order to remove any output which is not part of the document, we use the `-q` (quiet) option:

    open PIPEIN, "wget -q -O – http://www.google.ca | ";
    open PIPEOUT, "| perl TextAnalyzer.pl";

    while(PIPEIN && $in = <PIPEIN>) {
    	print PIPEOUT $in;
    }

    close PIPEIN;
    close PIPEOUT;

We coud of course use the @ARGV array to allow us to use a command line argument as the url we will download from:

    open PIPEIN, "wget -q -O – ".$ARGV[0]." | ";
    open PIPEOUT, "| perl TextAnalyzer.pl";

    while(PIPEIN && $in = <PIPEIN>) {
    	print PIPEOUT $in;
    }

    close PIPEIN;
    close PIPEOUT;
