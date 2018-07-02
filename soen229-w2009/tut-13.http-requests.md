# HTTP Requests (March 18th, 2009)

An HTTP Request can contain information which affects how a server (or a CGI script) executes it.

## URLs and Query Strings; GET Parameters

We saw in one of last week's tutorials that an HTTP Request contains (in the request line) a URL, and appended to that URL is a _query string_.

A query string is a collection of key-value pairs (called GET parameters) appended to the URL after a question mark. The keys (the parameter's name) are seperated from the values by an equals character = and each key-value pair is delimited by an ampersand ('&') character:

    index.php?fname=Richard&lname=Le%20Guen

Here we would say that there are two parameters in the query string: fname, and lname.

The query string is actually visible when you visit web sites:

    http://www.facebook.com/profile.php?id=48305422

Same thing, when I search my own name on Google I get sent to the following page:

    http://www.google.ca/search?hl=en&q=richard+le+guen&btnG=Google+Search&meta=

You can see the query string at the end of these urls. If you change them, the page changes; if you change the value for `id` in the facebook url above, the page loads and you're looking at someone else's profile.

You'll notice that the URL from when I searched Google, the spaces in my name (Richard Le Guen) were replaced by an addition character, '+'. This is because the both the names and values of GET parameters are _URL-encoded_. What would happen (in the HTTP request) if we had spaces in the URL or the query string? Remember that a space is supposed to delimit between the URL and the prototol (on the request line, the first line of the request) so we can't allow the URL to contain a space.

On a similar note, what if we wanted to search "Richard & SOEN229"? Type it into the Google search engine, and you might be sent to a URL which looks like this:

    http://www.google.ca/search?hl=en&q=Richard+%26+SOEN229&btnG=Google+Search&meta=

Note that the ampersand '&' turned into `%26`. This is because the ampersand is used to delimit key-value pairs. Consequently we have to encode it. URL encoding dictates that any character in a parameter (or a parameter's name) can be replaced with a percent ('%') character, followed by its two-digit hexadecimal ASCII value. This applies to most of the URL as well. Were I to request a file over HTTP which was contained in a directory with spaces in the name, I would have to do something like the following:

    http://web-site.ex/dir+with+spaces+in+the+name/file.html

I could also replace those spaces with `%20` since 20 is the hexadecimal code for a space's ASCII value:

    http://web-site.ex/dir%20with%20spaces%20in%20the%20name/file.html

### URL Decoding in Perl

In Perl, we have two functions which help us convert a URL-encoded character back into the original character: `hex` and `chr`, and our trusty regular expression substitution operator.

The `hex` function takes a string and – if its valid hexadecimal – converts it to a number. We can then use `chr` to convert that number into an ASCII character.

Lastly, we need to use a special modifier 'e' with a substitution. The 'e' modifier means that the replacement (between the second and third slash '/') isn't a string, but Perl code. So we can now include the `chr` and `hex` functions in the substitution.

    $url =~ s/%([a-f0-9]{2})/chr(hex($1))/eig;
    				# modifiers:
    				# e -	replacement is not a string,
    				#	 but Perl code to generate
    				#	 a string
    				# i -	case insensitive
    				# g -	repeat the substitution as often
    				#	 as possible

## The Request Body; POST Parameters

An HTTP Request can also contain a body. When it does, it specifies a Content-Type header. The two Content-Types which we will look at are `application/x-www-form-urlencoded` and `multipart/form-data`.

### Content-Type: application/x-www-form-urlencoded

The first content type – the more common one – is easy if you understand the query string.If the content type is `application/x-www-form-urlencoded` it means that the body is just key-value pairs, formatted just like the query string.

### Content-Type: multipart/form-data

The second content-type we're looking at makes the body a little bigger and a little more challenging to interpret.

The `multipart/form-data` content type means that the body is divided into multiple _parts_, delimited by a _boundary_. Each part is a different parameter. The boundary is a string defined in the Content-Type header, a seemingly randomly-selected sequence of numbers. When an HTTP request has a Content-Type of `multipart/form-data`, the Content-Type header will have the boundary appended to the header value:

    Content-Type: multipart/form-data; boundary=---------------------------9694380744286

The body begins with a line of text which contains only the boundary, followed by some special "headers" specific to this part of the body. The first of these is usually a 'Content-Disposition':

    ---------------------------9694380744286
    Content-Disposition: form-data; name="variable"

The 'name' in the content-disposition tells you the name of the parameter in this part of the request body.

After these headers we have the parameter value:

    -----------------------------9694380744286
    Content-Disposition: form-data; name="variable_1"

    blah blah blah

So what this part of a `multipart/form-data` request body is saying is that the request came with a parameter "variable_1" which is some plain old form-data which has a value of "blah blah blah".

### File Uploads with multipart/form-data

When you upload a file to a web server via HTTP (like when you upload a picture to Facebook, or attach an email to a gmail message) is when the `multipart/form-data` content-type really shines. You can't include a file in an HTTP request if the request's content-type is `application/x-www-form-urlencoded`. Let's say we're uploading a text file, HelloWeb.txt, with the following contents:

    Hello web!

The resulting 'part' (which describes a parameter) in our request body would look something like this:

    -----------------------------9694380744286
    Content-Disposition: form-data; name="MyUploadedFile"; filename="HelloWeb.txt"
    Content-Type: text/plain

    Hello web!

### A Full, Multi-Part File Upload Request Body

    -----------------------------9694380744286
    Content-Disposition: form-data; name="MyUploadedFile"; filename="HelloWeb.txt"
    Content-Type: text/plain

    Hello web!
    -----------------------------9694380744286
    Content-Disposition: form-data; name="variable_1"

    blah blah blah

So in this request we recieved a parameter with the name "MyUploadedFile" whose value was a file, named "HelloWeb.txt". We then also received another POST parameter names "variable_1" with the value "blah blah blah".

## Perl: Reading the Request Body

So, thinking in Perl now, we know that a request contains a request line and headers, followed by a blank line:

    GET /index.html?fname=Richard&lname=LeGuen HTTP/1.1
    Host: www.wherever.com
    User-Agent: Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)
    Accept: text/xml,text/html,image/gif,*/*
    Accept-Language: en
    Connection: keep-alive

So when we want to interpret GET parameters, it's easy; we just have to use Perl's incredible text manipulation capabilities to extract the key-value pairs in the query string, which is appended to the url with a question mark '?'.

What about the body though? We still haven't read the contents of a request body; up until now we've been reading the request (out of STDIN) up to the empty line, where we stop:

    do {
    	$stdin = <STDIN>;
    	$request .= $stdin;
    } while($stdin =~ /\S/);

We didn't continue to read the request body because there is no EOF character in an HTTP request. If you have no idea what I'm talking about, you might want to revisit the "Reading an HTTP Request Out of STDIN" part of [this](tut-12.http-script.md) tutorial.

Once we've read the request line, headers, and empty line out of the STDIN, we will have to use the built-in perl function `read` to read the body of the request. The `read` function takes three parameters: a file handle, a scalar variable, and a length; a number of characters will be read from the file handle, and saved in your scalar variable. Here's an example: (in which we also use the `-s` file test to get the file's size)

    $filename = "notes.txt";
    open("INPUTFILE", "<".$filename);
    read(INPUTFILE, $file_contents, -s $filename);
    print $file_contents;	# this script works just like
    			# our cat script from the
    			# first week of tutorials

Here's another example, where we will display the first 10 characters of a file: (when you run it, remember that \n is a character)

    $filename = "notes.txt";
    open("INPUTFILE", "<".$filename);
    read(INPUTFILE, $first_ten_chars, 10);
    print "The first ten characters of $filename are: \n";
    print $file_contents;
    print "\n";

So now how do we determine the size of an HTTP request's body? When we receive an HTTP request, the Content-Length header provides that information.
