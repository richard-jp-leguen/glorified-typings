# Perl Regular Expressions, continued (January 21st, 2009)

Last week we were unable to go in-dept as to what Perl Regular Expressions were, and how to use them.

So, we'll have to start this tutorial with the end of last week's tutorial on [The Linux Command Line (and More Perl)](/tutoring/soen229/tutorials/linux-and-perl)

Once you've gone over the end of that tutorial (the part on the Grep command and Regular Expressions) continue on to…

## Using Perl Regular Expressions to Strip HTML Tags  
And Extract Information

So now that we're all Perl RegEx masters, we're going to take the HTML from [this forum](http://www.phpbb.com/community/viewtopic.php?f=46&t=1417375). We will then search this HTML content using Perl Regular Expressions, and generate output similar to [this](http://users.encs.concordia.ca/~v_cook/teaching/soen229/lab2_scripts/output.txt).

The first challenge we will encounter will be using the HTML as input.

Since you're still new to Perl, we're not going to write a Perl script to download the HTML automatically. Instead, we're going to download it to a file, and the parse that file using Perl's `open` function, which we saw in last week's tutorial.

### Linux Command Line: Downloading A Web-Site

To download the HTML from a web site from the command line, we're going to use Linux's `wget` command. So, once again, let's consult the man pages to see what we can learn about `wget`.

    man wget

After reading the man pages on `wget` you'll figure out that to download the HTML contents of a web page (`www.web-site.ex`) we type the following:

    wget http://www.web-site.ex

So to download the HTML contents of our forum, we type in:

    wget http://www.phpbb.com/community/viewtopic.php?f=46&t=1417375

And the contents get saved to a file named `viewtopic.php?f=46&t=1417375`. To rename this file to something more manageable, use the `mv` command; in Linux you don't rename a file, you move it to a new file name. (weird, eh?)

    mv viewtopic.php?f=46&t=1417375 tutorial-2.html

### Reading the HTML File

So last week we saw how to perform basic file IO in Perl, right? So we'll write the basics of what we know; how to read all lines out of the file.

    $filename = "tutorial-2.html";	# I renamed my downloaded
    					# file 'tutorial-2.html'
    open("IN", "<".$filename);
    while($line = <IN>) {
    	# you're going to have to find
    	# a Perl Regular Expression
    	# to extract the information
    	# we're looking for
    }
    print "\n";
