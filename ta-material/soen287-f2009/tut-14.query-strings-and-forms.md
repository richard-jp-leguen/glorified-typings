Query Strings and HTML Forms
============================

It should have been mentioned in a [previous tutorial](../soen229-w2009/tut-11.web-and-http.md) that an HTTP request contains – appended to the URL – a _query string_. Query strings are one of the means by which you can pass information from the browser to the server-side application, in this case your CGI script.

What Is a Query String?
-----------------------

### Common Examples

You’ve seen query strings before, very often, probably. For example, when you perform a Google search, you will get a URL similar to this on:

    http://www.google.ca/search?hl=en&q=richard%20le%20guen&btnG=Google%20Search&meta=

Likewise, you may notice that when you visit someone’s Facebook profile, the URL in your browser looks like this:

    http://www.facebook.com/profile.php?id=48305422

… if you change the numeric value for `id`, you end up at someone else’s profile:

    http://www.facebook.com/profile.php?id=XXXXXXXX

You can also use query strings when you visit static pages, but they will have no effect:

    index.html?foo=bar

### The Format Of a Query String

In both the examples you’ll notice that there is a question mark `?` in the URL. Everything after a question mark in a URL is part of the query string.

The query string is presented in the form of key-value pairs called _parameters_. More specifically, these parameters in the query string are called _GET parameters_.

Our example URL from Facebook has only one parameter. Its name is `id` and its value is `48305422`.

    id=48305422

The example URL from our Google search is a little more complicated. It has several parameters; they are delimited by ampersand characters `&` in the query string. The query string contains parameters `hl` (with a value of `en`), `q` (with a URL-encoded value of `richard%20le%20guen`), `btnG` (with a URL-encoded value of `Google%20Search`) and `meta` (with a value of empty string).

    hl=en&q=richard%20le%20guen&btnG=Google%20Search&meta=

### URL Encoding

You may have noticed that in the example URL from Google there are lots of percentage characters `%`.

You may also be wondering what happens when a parameter name or value contains an equals character `=` or an ampersand character `&`?

Parameter names and values are _URL encoded_. Any character in a URL or a query string can be replaced with a percent sign, followed by the character’s two-digit hexadecimal ASCII value.

In hexadecimal, 20 is `32`, which is the ASCII value for a space.

So, returning to the example Google URL, the parameter values are in fact `en` for parameter `hl`, `richard le guen` for parameter `q`, `Google Search` for parameter `btnG` and empty string for parameter `meta`.

Query Strings in CGI Programming
--------------------------------

According to the CGI specification, the web server provides the query string to the CGI program via an environment variable `QUERY_STRING`.

So, when writing CGI programs using Perl, we can access the query string as follows:

### Reading the Query String

    $queryString = $ENV{"QUERY_STRING"};

… but this is only the query string. We need to split that query string into its kay-value parameters.

### Parsing the Query String

    %params = ();
    $queryString = $ENV{"QUERY_STRING"};
    @keyValuePairs = split(/\&/, $queryString);
    foreach my $keyValuePair (@keyValuePairs) {
    	($key, $value) = split(/\=/, $keyValuePair);
    	# ...
    	$params{$key} = $value;
    }

### URL Decoding the Query String

There is a problem with this script though; our parameter’s names and values are still URL encoded.

The following Perl code can be used to URL decode a string:

    $aString =~ s/%([a-f0-9]{2})/chr(hex($1))/eig;
    				# pattern modifiers:
    				# e -	replacement is not a string,
    				#	 but Perl code to generate
    				#	 a string
    				# i -	case insensitive
    				# g -	repeat the substitution as often
    				#	 as possible

We can now add it to our earlier code segment to parse the GET parameters into a hash. Save the following in your web space, and name it `QueryString.cgi`. We will need it for the rest of the tutorial.

    %params = ();
    $queryString = $ENV{"QUERY_STRING"};
    @keyValuePairs = split(/\&/, $queryString);
    foreach my $keyValuePair (@keyValuePairs) {
    	($key, $value) = split(/\=/, $keyValuePair);
    	$key =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the key
    	$value =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the value
    	$params{$key} = $value;
    }
    print "Content-Type: text/plain\n";
    print "\n";
    print "GET Parameters:\n";
    foreach my $parameterName (keys %params) {
    	print $parameterName." => ".$params{$parameterName}."\n";
    }

Try this script out; browse to this script in your web space, and start manually appending query strings to the URL to see the results.

Providing Parameters From the Browser
-------------------------------------

So how can I make use of query strings in an HTML document? There are two ways:

*   Anchors/Hyperlinks
*   HTML Forms

### Anchors/Hyperlinks

We’ve seen HTML anchor elements, `<a>`, which are sometimes negligently referred to as ‘links’. Since a query string is appended to a URL, we can just include it in the value of an anchor element’s `href` attribute:

    <a href='QueryString.cgi?1%2B1=2&2%2B2=5'>Click Here</a>

### HTML Forms

Now for the new stuff: HTML forms. HTML forms allow you to use an HTML document as a ‘front end’ or user interface for a server-side application. It allows your end-user to communicate with your CGI program without having to know HTTP protocol.

In an HTML document, a form element should contain input elements.

The user provides information for various inputs, and submits the form. When the form is submit, the browser turns that form into an HTTP request, using the inputs as parameters.

Here is an example HTML form:

    <form action='QueryString.cgi' method='GET'>
     <div>
      First Name:
      <input type='text' name='fname'/>
     </div>
     <div>
      Last Name:
      <input type='text' name='lname'/>
     </div>
     <input type='submit' />
    </form>

Add this to an HTML file in your web space, and then browse to that HTML file. Fill out the form, and press the ‘submit’ button. You should see that the information you provided to those inputs which have a `name` attribute are now in the query string.

Here are the relevant points to take from this example:

*   A form has an attribute `action`. When the form is submit, the browser sends an HTTP request for a resource corresponding to the `action`. Always include an `action` attribute in your forms.
*   A form has a `method` which will be the method of the HTTP request sent. Typically you’ll see GET or POST, and the two methods send parameters differently; POST doesn’t use a query string. Again, always include a `method` attribute in your forms.
*   Every `<input>` has a `type` attribute. This tells the browser how to render that input element. The `type` can distinguish between text boxes, check boxes, radio boxes etc.
*   There is one special `<input>` element of type `submit` which the user clicks when he is done filling out the form.
*   When the form is submit, all those input elements which have `name` attributes are used as parameters in the HTTP request.
