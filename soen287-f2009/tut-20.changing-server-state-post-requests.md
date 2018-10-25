Changing Server State: POST Requests
====================================

Security Issues With BlackJackWithCookies.cgi
---------------------------------------------

Our ‘BlackJackWithCookies.cgi’ script is vulnerable to the second most common attack on the World Wide Web: cross site request forgeries.

### Cross Site Request Forgeries (XSRF)

Cross site request forgeries are related to hotlinking, so if you understand hotlinking you should understand XSRF.

### An XSRF Attack

_This example is best attempted using Internet Explorer_

#### 1) Make Sure You Have The Script in the Right Place

First, though try this experiment. For it to work, makes sure your web space contains the "BlackJackWithCookies.cgi" script at the following URL:

    http://users.encs.concordia.ca/~r_leguen/BlackJackWithCookies.cgi

… where ‘r\_leguen’ is replaced with your ENCS username.

#### 2) Play Some BlackJack

Start playing some Black Jack in your web space at that same URL.

#### 3) Visit My XSRF Page

Then visit the following URL, replacing ‘r\_leguen’ with you ENCS userame:

    http://richard.jp.leguen.ca/scripts/bin/soen287/xsrf.php?username=r_leguen

#### 4) Go Back to BlackJack

You’ll notice that you have lots more cards than before. This is because we use a GET parameter to determine if the user is going to hit or stand, and this makes it vulnerable to XSRF attacks. If you’ll look at the HTML source from the page you visited above, you’ll see a lot of this:

    <img src="http://users.encs.concordia.ca/~r_leguen/BlackJackWithCookies.cgi?Action=Hit" />

When the browser sees this <img> element, it sends an HTTP request for that resource, with no assurance it really is an image! As you can see above though, the URL is in fact a request to "Hit" in our Black Jack game.

The technical way of expressing this problem is that our server does not ensure that GET requests are _safe_ and _idempotent_.

Using POST Requests
-------------------

This problem can be solved by using POST requests instead of GET requests to modify the server state.

A POST request has a request body where information – such as a query string or an uploaded file – can be included. A POST request is also not required to be idempotent according to HTTP specification.

### POST Requests in HTML

The bad news is that in HTML, you can’t use a hyperlink to send a POST request. You have to use a form.

The good news is that all you need to do to send a POST request using an HTML form is change the "method" attribute to "POST".

    <form actin='whatever.cgi' method='POST'>
    	<input type='submit' value='Click here to send a POST requestt!' />
    </form>

### POST Requests in Perl

When you receive a POST request there are some important environment variables you may want to work with. The first is the ‘REQUEST\_METHOD’ environment variable:

    if($ENV{"REQUEST_METHOD"} eq "POST") {
    	# modify server state
    }
    elsif($ENV{"REQUEST_METHOD"} eq "GET") {
    	# don't modify server state
    }

Other environment variables we haven’t looked at yet include ‘CONTENT\_TYPE’ and ‘CONTENT\_LENGTH’ which tell us the formatting and the length of the request body, repectively. These are used in conjunction with the STDIN filehandle to read the request body:

    if($ENV{"CONTENT_TYPE"} eq "application/x-www-form-urlencoded") {
    	$body = "";
    	read(STDIN, $body, $ENV{"CONTENT_LENGTH"});
    	# $body now holds the request body
    	# if the CONTENT_TYPE is "application/x-www-form-urlencoded"
    	#  that means the request body contains a query string.
    	#  we could parse it just the same way we parse
    	#  the query string for a GET request.
    	%POST = ();
    	$queryString = $body;
    	@keyValuePairs = split(/\&/, $queryString);
    	foreach my $keyValuePair (@keyValuePairs) {
    		($key, $value) = split(/\=/, $keyValuePair);
    		$key =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the key
    		$value =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the value
    		$POST{$key} = $value;
    	}
    }
    else {
    	# we'll see other CONTENT_TYPEs later in the semester…
    }

In Summary
----------

Never, ever, ever modify server state with a GET request! Client applications (like browsers, or web crawlers like the ‘GoogleBot’) will assume that it is safe to send a GET request any time for any reason to any URL on your server. Again, an XSRF is perhaps the second most common attack made against web sites, and – like the Cross Site Scripting Attack – it is fairly easy to prevent.

Where XSS vulnerabilities are a sign of negligence or incompetence on the part of the developer, XSRF vulnerabilities are the mark of a lazy, naive web developer.
