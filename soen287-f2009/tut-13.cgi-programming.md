CGI Programming
===============

Normally, when you request a resource on the World Wide Web, the web server receives an HTTP request, finds a file which corresponds to the URL, and includes that file in an HTTP response. This results in _static_ web content.

Nowadays, however, most web content is _dynamic_.

When you search something on [google.com](http://google.com), Google doesn’t have thousands of HTML documents to display for every possible search. Likewise, Facebook doesn’t have an individual HTML file for every single one of its user profiles, groups, events and applications.

So how does this work?

The Common Gateway Interface
----------------------------

The Common Gateway Interface is one means of generating dynamic web content. The CGI Specification describes a contract between the web server, and an external executable program.

The deal is like this: The Web Server reads and parses the request line and the headers from the HTTP request. It uses the request line and the headers to populate environment variables. The Web Server then spawns a new process to execute the CGI program, feeding the CGI program the request body via STDIN. The CGI program is then responsible to output response headers, server directives (special headers which are not sent to the client) and a response body to STDOUT. The Web Server reads from the CGI script’s STDOUT, and uses the output to produce an HTTP response.

What?
-----

It’s a mouthful, so if you don’t understand the last paragraph, don’t worry. If you were able to follow "the previous tutorial" on HTTP protocol, you’re doing fine.

An Example – in Perl
--------------------

So here is a sample CGI program. The most important thing we need to remember right now, is that the CGI program is responsible to output response headers and a response body to STDOUT.

So create a file `HelloWeb.cgi` and include a shebang as the first line of the script:

    #!/usr/bin/perl --

A CGI script always has to output a `Content-Type` header:

    print "Content-Type: text/html\n";

Since this is our first CGI script, we’re not going to include any other HTTP headers. To mark the end of our headers, we print a blank line:

    print "\n";

Now we print the body of our request:

    print "<strong>Hello Web!</strong>";

… but ‘Hello World’ programs always bore me, so we’ll add in something a little more interesting.

    print "<br />The UNIX timestamp is ".time();

### The Entire Example Script

    #!/usr/bin/perl --
    	
    print "Content-Type: text/html\n";
    print "\n";
    # Take note:
    #	this script does not produce a valid, properly formatted HTML document!
    #		(why not?)
    print "<strong>Hello Web!</strong>";
    print "<br />The UNIX timestamp is ".time();

Running The Example
-------------------

### Running it on the Command Line

You can run the script from the command line and it should have no problems:

    $ perl HelloWeb.cgi

Doing so wil show you how the output from our script looks like a chunk of an HTTP response.

### Running it on a Web Server

We’re much more interested in running the script from a browser, however. To do this, we need the script to be on a Web Server.

As an ENCS student, you have a web space available. The directory path of your web space is:

    /www/home/r/r_leguen

… where you replace `r/r\_leguen` with the first letter of your username followed by your username.

Files you put in that folder with the proper permissions are downloadable in a web browser. The URL to download resources from that directory is:

    http://users.encs.concordia.ca/~r_leguen

… where you replace `r\_leguen` with your username.

You can execute CGI scripts written in Perl from your web space. You will have to copy your file to that location:

    $ cp HelloWeb.cgi /www/home/r/r_leguen/HelloWeb.cgi

Again, replace ‘r/r\_leguen’ with the first letter of your ENCS username, followed by your ENCS username.

If you now try to browse to your CGI script in a browser you will probably get an error. You have to change the permissions of your script before you execute it. In your web space, you need to grant the file’s owner (read-write-execute) permissions, the members of a file’s group (read-execute) permissions and all other users (read-execute) permissions.

    $ chmod 755 /www/home/r/r_leguen/HelloWeb.cgi

I Get an Error!
---------------

Your checklist whenever you get an error message from the server should be:

1.  Check that your script ends in a ‘.cgi’ extension
2.  Check that the shebang line of your script is correct:
    *   #!/usr/bin/perl –
3.  Check that your script prints a ‘Content-Type’, and that there is an empty line between the headers and the request body.
4.  Check that your script’s permissions are correct.

Check It Out In Telnet!
-----------------------

Once you have successfully browsed to your CGI script, open up Telnet to view the HTTP response from your CGI script:

    $ telnet users.encs.concordia.ca 80

… and type the GET request for your script.

    GET /~r_leguen/HelloWeb.cgi HTTP/1.1
    Host: users.encs.concordia.ca
    	

As always, replace `r/r\_leguen` with the first letter of your ENCS username followed by your ENCS username, and don’t forget to include an empty line after your headers. You’ll notice that he web server adds some HTTP headers, such as the `Content-Length`.
