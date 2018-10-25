Security Issues With Your CGI File Explorer
===========================================

Your CGI File Explorer works; it allows you to navigate the server’s file system, and download files from the file system.

Don’t be too impressed with yourself though! There are some major web security issues that our CGI File Explorer can demonstrate.

Shared Hosting And The Threat of Exposed Source Code
----------------------------------------------------

Your ENCS web space is a shared hosting environment, meaning that it’s not only yours; every other ENCS student is (or at least can be) hosting resources from the same server-environment.

If you – from a Linux command line on an ENCS machine – try to navigate to another student’s web space, it probably won’t work:

    $ cd /www/home/b/b_crudo
    $ cd /www/home/j/j_fora
    # these probably will not work,
    # as you do not have permission

Yet, you can use your CGI File Explorer to navigate to those directories:

    FileExplorer.cgi?FilePath=/home/b/b_crudo
    FileExplorer.cgi?FilePath=/home/j/j_fora
    FileExplorer.cgi?FilePath=/home/r/r_leguen

Not only this, but you can _download server-side programs_, such as CGI scripts, _from other student’s web spaces_. Of course, if you can do it, so can they.

You might not think this is a big deal, but what if your script contained some sort of sensitive username/password information? What if your scripts contained private keys for data encryption? Then you would have an _enormous_ security problem.

Understanding why your FileExplorer can do this takes a little bit of Linux-Fu

### The Linux-Fu (optional)

The folder corresponding to your web space is not accessible to other student’s user accounts; only you have access to your own web space.

However, in order to execute and read your server-side programs, such as CGI scripts, the web server has to have permission to read and execute your scripts, otherwise they wouldn’t work. The web server has its own special user account which it runs under; that user _does_ have access.

In the same way that it has access to your CGI scripts, the web server has access to my CGI scripts.

Consequently, when either of our CGI scripts execute, they are executing under the web server’s user account, who has access to both. As a result, and server-side program written by an ENCS student could read and access any other resource in another student’s web space.

### The Solution

There is no good solution to the shared hosting problem. Whenever you write code and deploy it in a shared server environment, that code is exposed. The only solution is to accept that this, and be careful as to what you include in your CGI scripts.

Cross Site Scripting (XSS) For Beginners
----------------------------------------

Our `FileExplorer.cgi` script is also vulnerable to one of the most prevalent attacks on the web today: cross site scripting attacks. Vulnerabilities to cross site scripting is the signature of an amateur, as it is the result of negligence on the part of the web developer.

The following lines of code:

    	print "'".$params{"FilePath"}."' resolved to '".$filePath."',<br />";
    	print "and file '".$filePath."' does not exist.";

… is an XSS exploit waiting to happen. (there are other similar places in the `FileExplorer.cgi` script, but this one is the easiest to demonstrate.

To better understand, try visiting the `FileExplorer.cgi` script using the following as the query string:

    ?FilePath=%3Cimg%20src=%22http://google.ca/intl.en_ca/images/logo.gif%22%20/%3E

And the page we see does not look right: images have been added, and inspection of the document source reveals the document doesn’t seem to be a properly structured HTML document anymore. This is because we neglected to escape output: whenever you output content for an HTML document, you need to replace (at the very least) the following characters with their corresponding HTML entities:

|Character|HTML Entity|
|--- |--- |
|`<`|`&lt;`|
|`>`|`&gt;`|
|`‘`|`&#39;`|
|`<`|`&quot;`|

If you do not, you will be a negligent, amateur web developer, whose web sites will be vulnerable to XSS.

You may still think this is no big deal ("so what if some formatting got screwed up?") but once we begin learning about client-side scripting and cookies you will begin to see the danger.

Visit your FileExplorer again, this time using the following query string:

    ?FilePath=%3Cscript%20type%3D%22text/javascript%22%3Ealert('XSS!');%3C/script%3E

You may not know Javascript, but this demonstrates how the XSS exploit allows an attacker to possibly insert executable HTML content into your web page. Allowing a 3rd party to add executable content is _bad_.
