The Web Without a Web Browser
=============================

If you took SOEN229 recently, you may have learned a little about [the HTTP protocol](../soen229-w2009/tut-11.web-and-http.md).

For those of you who aren’t familiar with the HTTP protocol, we’re going to write some HTTP requests and see the responses we get from web servers. To accomplish this, we’re going to use Telnet.

Telnet
------

Telnet is a networking tool, and that’s all you need to know for these tutorials.

The more important matter is how you can use Telnet to view the HTTP responses from your CGI scripts.

On an ENCS machine, boot into Linux, and open a command line. Type the following:  
(the ‘$’ is supposed to be the prompt, so don’t type that)

    $ telnet encs.concordia.ca 80

You’re now connected to a Concordia web server via Telnet, and can manually type out an HTTP request. If at any time you want (or need) to exit, you hold ‘ctrl’+'\]’ to disconnect; then type ‘quit’ and you should exit Telnet.

Try typing the following:

    GET / HTTP/1.1
    Host: encs.concordia.ca
    	

Take note that you have to type the blank line after the request headers. As soon as you type in this blank line, you should see a response from the server.

… and it will be MASSIVE. It will probably not fit on the sreen.

Your ENCS Web Space
-------------------

So that this exercise is a little more useful, we’re going to put a smaller HTML document on a Concordia web server and do it again.

You – as an ENCS user – have a web space available to you. The path to your web space is:

    /www/home/r/r_leguen/

… where you replace `r/r\_leguen` with the first letter of your ENCS username, and your ENCS username.

In your web space directory, create a file, and call it ‘index.html’. Make it a small HTML document:

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
     <head>
      <title>My HTML File</title>
     </head>
     <body>
      <p>
      Hello Web!
      </p>
     </body>
    </html>

Before we try it in Telnet, browse to this document in a web browser, visiting the following url:

    http://users.encs.concordia.ca/~r_leguen/index.html

… where you replace ‘r/r\_leguen’ with the first letter of your ENCS username, and your ENCS username.

No go back to your Linux command line. If you haven’t already, disconnect and exit Telnet. Then use Telnet to connect to `users.encs.concordia.ca`:

    $ telnet users.encs.concordia.ca 80

… and type out a GET request for the file ‘/~r\_leguen/index.html’:

    GET /~r_leguen/index.html HTTP/1.1
    Host: encs.concordia.ca
    	

… still replacing `r/r\_leguen` with the first letter of your ENCS username, and your ENCS username.

The HTTP response you get should be much more managable.

Be Careful!
-----------

Doing something like this is guaranteed to violate a web site’s terms of use, and will often be considered abuse. Try to avoid using Telnet to connect to web sites other than your web space.
