# Web Servers and HTTP (March 11th, 2009)

And Now For Something Completely Different!

We're hoping to show you a little bit about Perl CGI later in the semester, but before we do that, we're going to learn a little bit about the nuts and bolts of web servers.

## What **IS** a Web Server?

"Web Server" is an ambiguous term which can refer to either:

*   software which accepts a special text file, called an HTTP request, as input and generates a special text file, called an HTTP response, as output.
*   A machine (computer) which runs the above stated software.

Within the scope of this tutorial, we're considering a Web Server as being the first definition, software.

Judging by the description above, you might be surprised that the all-knowing, all-powerful World Wide Web is essentially built on simple text files! As such, since Perl is a master of text manipulation, Perl and the World Wide Web are technologies which have gotten along very well over the years.

## How Does a Web Server Work?

A Webserver accepts HTTP requests it recieves over network. Don't be scared! These HTTP requests are – in the end – just glorified text files. It responds to those requests with another text file, called an HTTP response.

### A Typical HTTP Request

Again, an HTTP request is just a bunch of text! Here's what a very simple, typical HTTP request looks like:

    GET /index.html?fname=Richard&lname=LeGuen HTTP/1.1
    Host: www.wherever.com
    User-Agent: Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)
    Accept: text/xml,text/html,image/gif,*/*
    Accept-Language: en
    Connection: keep-alive

An HTTP Request consists of the request line, headers, an empty line and (optionally) a request body. For now, we're going to ignore the request body, as our example request (above) does not include one.

#### The Request Line

The first line is called the request line. It consists of:

1.  The _request method_; in the example it is `GET`
2.  the requested _URL_; in the example it is `/index.html`
    *   Appended to the URL, the request line optionally includes what is called a _query string_. For now, we will say that the query string is everything appended to the URL after a question. In the example, `fname=Richard&lname=LeGuen` is a query string.
3.  the protocol by which the request is being made; in the example it is HTTP/1.1

Generally speaking you need only understand the URL, and a little bit about the method. Within the scope of this tutorial, we're going to consider the 'GET' method only.

We're also going to consider the URL to be a path relative to the document root which corresponds to a file; the file which the client – who sent this request – wants to download from the server machine. So the server who recieves this request will reply with an HTTP response, which will contains the contents of the file which corresponds to the URL… more on that later.

#### Headers

Headers are key-value pairs which provide information about the request. In the example request above, 'Host,' 'User-Agent' and 'Connection' are all headers. You can see that the format for a header is always the same: the header name, followed by a colon (':') and a space, followed by a value. (hmmm… we're talking about key-value pairs… what Perl type would be most suited to store or manipulate these headers?)

#### An Empty Line

The end of the headers in an HTTP request are marked by an empty line. Anything past this point is the request body, which we're not talking about right now…

#### The Body

The example above does not contain a body, and the body or an HTTP request is outside the scope of this tutorial.

### A Typical HTTP Response

So let's say that the file '/index.html' is an text file which contains the following text:

    <html>
    <body>
    <h1>Hello Web!</h1>
    </body>
    </html>

The HTTP response will look something like this:

    HTTP/1.0 200 OK
    Date: Fri, 27 Feb 2009 23:59:59 GMT
    Content-Type: text/html
    Content-Length: 50

    <html>
    <body>
    <h1>Hello Web!</h1>
    </body>
    </html>

The HTTP Response consists of a status line, headers, en empty line, and the response body.

#### The Status Line

The first line is called the status line. It consists of:

1.  the protocol by which the request is being made; in the example it is HTTP/1.0
2.  A stats code; in the example the status code is "200 OK"

You might be wondering what the status code _is_, think of it as a very short summary of the response. In the example the status code is "200 OK" which means that everything went fine, and the server was able to respond to the HTTP request without a problem. Another common status code you might have seen while surfing the net is "404 Not Found" which means the file corresponding to the request's URL was not found; maybe it doesn't exist.

#### Headers

Again, an HTTP response contains headers, very similar to those in an HTTP request. In the example we have three headers:

*   **Date:** When the server responded to the request.
*   **Content-Type:** Which tells us index.html was an html file.
*   **Content-Length:** The length in bytes (or characters) of the response's body.

#### An Empty Line

The end of the headers is marked by an empty line.

#### The Response Body

The response body is everything below the empty line, and is contents of the resource (file) which was requested.
