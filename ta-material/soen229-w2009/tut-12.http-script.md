# Writing a Script to Respond to HTTP Requests (March 11th, 2009)

In this tutorial, we're going to write a simplistic script which reads an HTTP request out of the STDIN, and prints an HTTP response to STDOUT.

## IMPORTANT: DON'T PANIC

You do **not** need to know _*ANYTHING*_ about networking or socket programming to go through with either this tutorial, nor the material we will be covering later in the semester! If you don't know what I mean by either "networking" nor "socket programming" don't worry! You shouldn't know those concepts, you don't have to know those concepts, and you won't have to know those concepts!

All we're doing is writing a script which reads specially formatted text input – called an HTTP request (see [this](tut-11.web-and-http.md) tutorial) – via STDIN, and generates specially formatted text output – via STDOUT – which we call an HTTP response (again, see [this](tut-11.web-and-http.md) tutorial).

Once you're done, you may want to test the script we write in this tutorial. There would be no better way to do this than actually send it an HTTP response from you favorite web browser (which should be Firefox!). So you can do this without knowing _*ANYTHING*_ about networking or socket programming I've provided a script, [HttpWebServer.pl](scripts/HttpWebServer.pl), which will let you do exactly that!

### How do I use the [HttpWebServer.pl](scripts/HttpWebServer.pl) Perl Script?

If _your_ script is called 'HttpStuff.pl', run my script like so: (from the Command Line)

    perl HttpWebServer.pl perl HttpStuff.pl

Or, if you've chmod-ed your script so it's an executable file you can do the following:

    perl HttpWebServer.pl HttpStuff.pl

Now open your favorite browser (**FIREFOX**) and type in the following as the URL:

    http://localhost:8080/

And if – at the end of tutorial – your script works, you should see a hello world page! **How cool is that?** If you're exceptionally interested, look at the code in my script.

## Writing the Script

### Outputting an HTTP Response to STDOUT

We're going to start with producing an HTTP response. We want to write an HTTP response to STDOUT. As we saw in [this](tut-11.web-and-http.md) tutorial an HTTP response begins with a status line, like the following:

    print STDOUT "HTTP/1.0 200 OK\n";

The next few lines are called headers, which are key-value pairs. We're going to specify the bare minimum in headers; Date (the time at which the server generated the response)" and the Content-Type (which tells us about the formatting of the data in the body).

    print "Date: Fri, 27 Feb 2009 23:59:59 GMT\n";
    	# wrong time; plagiarizers beware…
    print "Content-Type: text/plain\n";

We then have an empty line:

    print "\n";

Lastly, we have the response body. For now we're just returning (technically, we're generating it) a Hello Web text file:

    print "Hello Web!\n";

So when we put it all together, we get:

    print STDOUT "HTTP/1.0 200 OK\n";
    print "Date: Fri, 31 Feb 2009 23:59:59 GMT\n";
    	# wrong date 'n time; plagiarizers beware…
    print "Content-Type: text/plain\n";
    print "\n";
    print "Hello Web!\n";

And you're good to go! Open your favorite web browser (**FIREFOX**), and go to the URL http://localhost:8080/ and you should see the words "hello web!" on the page. But here's the problem: if you visit http://localhost:8080/directory/file.html you should be able to request a different file, and consequently download something different. But you keep getting the same page!

That's because we're not interpreting the Http Request, so things like the requested URL (which should correspond to a file) don't matter. The script we've written always returns this 'hello web!' message. We need to read the Http Request out of STDIN and interpret it.

### Reading an HTTP Request Out of STDIN

So now we need to read an HTTP Request out of STDIN. We already know how to read out of STDIN though, don't we?

    while($stdin = <STDIN>) {
    	chomp($stdin);
    	$request.= $stdin."\n";
    }

Right? But this isn't going to work. You may remember that using the line input operator inside of a while loop in this fashion will read through an entire file, but an HTTP request isn't a file like other files, since it doesn't exist on-disk. **An HTTP request does not end with the EOD character** so this while loop continues for ever and you have to kill the script with Linux-fu.

For now, since we're ignoring requests which contain bodies, were only going to read the headers, which end with an empty line. So once we've hit the end of the headers, we should read a line which is empty, at which point we need to stop reading out of STDIN, or our script will hang/freeze.

    do {
    	$stdin = <STDIN>;
    	$request .= $stdin;
    } while($stdin =~ /\S/);

Now its just a matter of extracting the first line of the HTTP request and determining what that URL of the request was. I'm not going to show you how to do this; that's easy stuff using what we learned in the [first tutorial](tut-03.linux-and-perl.md).

So from here on in I'll assume that `$url` is a variable into which I've extracted the request's URL. I need to determine if there is a file in the document root which corresponds to that file, and if I can read that file. If it exists, I should read and output its contents in the body of my response. For now, I will only allow requests to download HTML files so we don't have to worry about changing the Content-Type header. (note above it was 'text/plain' and here is it 'text/html')

    $docroot = "/home/r_leguen/htdocs";
    # we somehow extract the URL…
    if(-e $docroot.$url && $url =~ /\.html$/) {
    		# Didn't check if I can read the file;
    		# plagiarizers beware…
    	open("FILE", $docroot.$url);
    	while($line = <FILE>) {
    		$body .= $line;
    	}
    	close FILE;
    	print STDOUT "HTTP/1.0 200 OK\n";
    	print "Date: Fri, 31 Feb 2009 23:59:59 GMT\n";
    		# wrong date 'n time; plagiarizers beware…
    	print "Content-Type: text/html\n"; # DIFFERENT!
    	print "\n";
    	print $body;
    }
    else {
    	# ...
    }
