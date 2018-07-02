# Building Larger Scripts

As you write larger scripts, you may begin to find that you need to split them up into smaller parts, sometimes even smaller files. In this tutorial, I'll show you how.

## The `do` Operator

It has nothing to do with the `do-while` control flow construct. Rather, `do` takes a string as a parameter; the name of a file. The interpreter then acts as though the contents of that file had been copy-pasted into the currently executing script.

For example, let's say I had a file 'print-arr.pl' which contained the following code:

    foreach $element (@arr) {
    	print $element." ";
    }
    print "\n";

... and file 'driver.pl' which contained the following:

    @arr = ("a", "b", "c");
    do "print-arr.pl";

    @arr = ("Hello", "World");
    do "print-arr.pl";

The output would be:

    a b c 
    Hello World 

The 'driver.pl' script is executed as though the contents of 'arr.pl' were present where the `do` operator was used. The following code ends up being practically the same:

    @arr = ("a", "b", "c");
    foreach $element (@arr) {	# used to be in file
    				# 'print-arr.pl'
    	print $element." ";
    }
    print "\n";

    @arr = ("Hello", "World");
    foreach $element (@arr) {	# used to be in file
    				# 'print-arr.pl'
    	print $element." ";
    }
    print "\n";

Generally speaking, using `do` in this way is a bad idea. You should use subroutines instead; we will now re-write our scripts to use a subroutine while still leaving the code to print an array in the 'print-arr.pl' script.

Here is our new 'print-arr.pl' script, which contains a subroutine definition:

    sub printArr() {
    	if(ref($_[0]) ne "ARRAY") {
    		die("Array reference expected.");
    	}
    	foreach $element (@{$_[0]}) {
    		print $element." ";
    	}
    	print "\n";
    }

And now, here is out new 'driver.pl' which uses the `printArr` subroutine defined in file 'print-arr.pl':

    do "print-arr.pl"; # only once
    @arr = ("a", "b", "c");
    &printArr(\@arr);

    @arr = ("Hello", "World");
    &printArr(\@arr);

This code works, but we should move away from using `do` as it can cause your program to bugger up as your project gets bigger and bigger.

### Circular Dependancies with the `do` Operator

Imagine I defined two scripts, 'script1.pl'…

    do "script2.pl";
    print "Hello World from Script 1!\n";

And 'script2.pl'…

    do "script1.pl";
    print "Hello World from Script 2!\n";

If I tried to run either of them, they'd just hang. So how do we solve this problem?

## The `require` Operator

The Perl `require` operator is very similar to `do` but keeps track of circular dependancies. Like `do`, `require` takes a filename as a parameter.

Now the contents of file 'print-arr.pl' are as follows:

    sub printArr() {
    	if(ref($_[0]) ne "ARRAY") {
    		die("Array reference expected.");
    	}
    	foreach $element (@{$_[0]}) {
    		print $element." ";
    	}
    	print "\n";
    }
    1;	# so you can use it successfully with the 
    	# 'require' keyword, a script must
    	# end with with a statement which
    	# evaluates to true.
    	# I don't make the rules.

While file 'driver.pl' now uses `require` and a subroutine call:

    require "print-arr.pl"; # only once
    @arr = ("a", "b", "c");
    &printArr(\@arr);

    @arr = ("Hello", "World");
    &printArr(\@arr);

It's a good idea to have your subroutines in other files, which you `require` in your 'main' script. This will result in smaller files, and – if you name your subroutines well – potentially more readible code.

## Packages in Perl

I'm now going to write a file 'arrays.pl' which will contain a bunch of subroutines to manipulate arrays. In it, I will define a subroutine 'print' to print an array, as well as 'flip' which will invert the order of the elements in an array.  
(remember that in Perl – when we invoke user-defined subroutines using the ampersand '&' – there is no problem naming a subroutine after an existing function or operator)

However, a subroutine named 'print' is a little generic. I might want to define another subroutine elsewhere with the same name, which does something else. So in order to distinguish _this_ `print` subroutine from others, I will include a package declaration at the top of the file:

    package arrays;

    sub print() {
    	if(ref($_[0]) ne "ARRAY") {
    		die("Array reference expected.");
    	}
    	foreach $element (@{$_[0]}) {
    		print $element." ";
    	}
    	print "\n";
    }

    sub flip() {
    	if(ref($_[0]) ne "ARRAY") {
    		die("Array reference expected.");
    	}
    	return reverse @{$_[0]};
    }

    sub contains() {
    	if(ref($_[0]) ne "ARRAY") {
    		die("Array reference expected.");
    	}
    	foreach $element (@{$_[0]}) {
    		if($_[0]==$_[1] || $_[0] eq $_[1]) {
    			return true;
    		}
    	}
    	return false;
    }

    1;

Now, when I write another script to use these subroutines the syntax changes slightly:

    require "arrays.pl";
    @arr = ("Hello", "World");
    &arrays::print(\@arr);
    @arr = &arrays::flip(\@arr);
    &arrays::print(\@arr);
    if(&arrays::contains(\@arr, "Hello")) {
    	print "The array contains 'Hello' as an element\n";
    }

Since the subroutines are defined in a different package, the call to each subroutine needs to be prefixed with the name of the package in which they are contained.

You can define several packages in one file, although its not recommended as it can be a little tough to read.

    &soen229::helloWorld();
    &richard::helloRichard();

    {
    	package soen229;

    	sub helloWorld() {
    		print "Hello World\n";
    	}
    }

    {
    	package richard;

    	sub helloRichard() {
    		print "Hello Richard\n";
    	}
    }

You can also include variables in packages:

    {
    	package math;
    	$pi = 3.141592654;
    }

    print $math::pi;
    print "\n";
