Maintaining State With Query Strings
====================================

What is State?
--------------

State – in the context of web development – means that the same URL and query string may return a different web page, depending on the state of the server.

For example, I visit my Gmail inbox. The url is:

    http://mail.google.com/mail/#inbox

When I log into my Gmail account, I ony have to do it once; I don’t have to log in over and over again every time I change pages. Between requests, Gmail ‘remembers’ me, without my changing the URL.

Likewise, when I browse to the page, sometimes I’ve received a new email and the page is different. Likewise, when I delete or move an email from my inbox, the next time I return, it hasn’t moved back to my inbox. Gmail ‘remembers’ the state of my inbox from one request to the next.

Maintaining state is essentially a technical way of saying "the web site remembers things."

Why Is It "Hard" To Maintain State?
-----------------------------------

HTTP is a stateless protocol; there is no mechanism is the protocol which defines a relationship between one request and another.

So how do web sites like Gmail accomplish this statefulness?

How To Maintain State
---------------------

Generally speaking, a web application accomplishes this by assigning the browser an identifier. When the request is over, the CGI script persists state-related information; the state could be persisted in a file for example. When the client makes another request, they include their identifier in the request. The CGI script uses this identification to find the persisted data, and proceeds with the transaction.

This is why I always put "remember" in quotation marks: while the server has to "remember" stateful information, its just as important that the client reminds the server with its identifier…

We are going to refer to a series of request-response interactions between a server and a specific client during which we maintain state a _session_. We are going to call the identifier that the browser includes with every request as a _session ID_.

There are two ways of passing the session ID between the client and the server: using a parameter in the query string to identify the client, and using cookies. We will see how to do this with a parameter in the query string this tutorial, and see how to use cookies in the next.

The Sample Application – BlackJack
----------------------------------

The sample application will be a simple blackjack game.

Since we’re maintaining state using the query string, a GET parameter, `SESSIONID`, will be used to identify the session. Session information will be in a file in the `/tmp` directory. That file will contain four lists: one for the cards in the deck, one for cards in the player’s hand, one for cards in the dealer’s hand, and one for cards in the discard pile.

### The Rules

To make the game of Blackjack simpler, we’re going to remove the Aces from our deck, and only give the player the option to "Hit" and "Stay". We won’t bother keeping track of the player’s score, and the player can "Hit" as much as they want.

What we do want to keep track of is the cards. We going to deal cards out of the deck to the two players, and those cards have to be valid across requests. Additionally, when there are no more cards, we shuffle the discard pile, and start using it as a deck.

### The Basics

Ignoring anything about the rules of Blackjack, our script will look like this in the end:

    #!/usr/bin/perl --
    	
    # We read GET parameters out of the query string
    %params = ();
    $queryString = $ENV{"QUERY_STRING"};
    @keyValuePairs = split(/\&/, $queryString);
    foreach my $keyValuePair (@keyValuePairs) {
    	($key, $value) = split(/\=/, $keyValuePair);
    	$key =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the key
    	$value =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the value
    	$params{$key} = $value;
    }
    	
    if(!$params{"SESSIONID"} || !-e "/tmp/r_leguen.cgi_blackjack.".$params{"SESSIONID"}) {
    				# if no session ID is provided,
    				# we initialize a session
    	# ...
    }
    else {	# if a session ID is provided, we initialize session data.
    	# read from a file where we stored the session info.
    	open("SESSION", "</tmp/r_leguen.cgi_blackjack.".$sessionID);
    	# read data from the session file…
    	close(SESSION);
    }
    	
    # code for the logic
    # and rules of Blackjack
    	
    # save session information in a file
    open("SESSION", ">/tmp/r_leguen.cgi_blackjack.".$sessionID);
    # write data to the session file…
    close(SESSION);

### Writing the BlackJack Game

As always, we start with our shebang:

    #!/usr/bin/perl --

We’re going to represent the deck and discard piles as arrays, so to keep things simple, we’re going to use a shuffle function provided by the List module.

    use List::Util 'shuffle';

We now are going to read the information out of the query string, we we’ll include our code to do that:

    %params = ();
    $queryString = $ENV{"QUERY_STRING"};
    @keyValuePairs = split(/\&/, $queryString);
    foreach my $keyValuePair (@keyValuePairs) {
    	($key, $value) = split(/\=/, $keyValuePair);
    	$key =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the key
    	$value =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the value
    	$params{$key} = $value;
    }

We now initialize the deck, the player’s card, the dealer’s cards, and the discard pile. They are all arrays.

    @deck = ();
    @player = ();
    @dealer = ();
    @discard = ();

We now have to load our session data. We have two situations: if the request included session information, and when the request did not include session information. If the request did not include session information we initialize everything and create a random SESSIONID:

(if you’re wondering why the names of the cards are so strange, it’s because we’re going to be [hotlinking](http://en.wikipedia.org/wiki/Inline_linking) to Wikimedia Commons… meaning we’re stealing images from someone else’s web site…)

    if(!$params{"SESSIONID"} || !-e "/tmp/r_leguen.cgi_blackjack.".$params{"SESSIONID"}) {	
    				# if no session ID is provided,
    				# we initialize a session
    	@cards = (
    			"c_2", # the 2 of clubs
    			"c_3", # the 3 of clubs
    			"c_4", # the 4 of clubs
    			"c_5", # the 5 of clubs
    			"c_6", # the 6 of clubs
    			"c_7", # the 7 of clubs
    			"c_8", # the 8 of clubs
    			"c_9", # the 9 of clubs
    			"c_10", # the 10 of clubs
    			"c_j", #the Jack of clubs
    			"c_q", #the Queen of clubs
    			"c_k", #the King of clubs
    		
    			"d_2", # the 2 of diamonds
    			"d_3", # the 3 of diamonds
    			"d_4", # the 4 of diamonds
    			"d_5", # the 5 of diamonds
    			"d_6", # the 6 of diamonds
    			"d_7", # the 7 of diamonds
    			"d_8", # the 8 of diamonds
    			"d_9", # the 9 of diamonds
    			"d_10", # the 10 of diamonds
    			"d_j", #the Jack of diamonds
    			"d_q", #the Queen of diamonds
    			"d_k", #the King of diamonds
    		
    			"h_2", # the 2 of hearts
    			"h_3", # the 3 of hearts
    			"h_4", # the 4 of hearts
    			"h_5", # the 5 of hearts
    			"h_6", # the 6 of hearts
    			"h_7", # the 7 of hearts
    			"h_8", # the 8 of hearts
    			"h_9", # the 9 of hearts
    			"h_10", # the 10 of hearts
    			"h_j", #the Jack of hearts
    			"h_q", #the Queen of hearts
    			"h_k", #the King of hearts
    		
    			"s_2", # the 2 of spades
    			"s_3", # the 3 of spades
    			"s_4", # the 4 of spades
    			"s_5", # the 5 of spades
    			"s_6", # the 6 of spades
    			"s_7", # the 7 of spades
    			"s_8", # the 8 of spades
    			"s_9", # the 9 of spades
    			"s_10", # the 10 of spades
    			"s_j", #the Jack of spades
    			"s_q", #the Queen of spades
    			"s_k", #the King of spades
    		);
    	@deck = shuffle(@cards);
    	$sessionID = int(rand(999999999999999));
    }

If a SESSIONID parameter _was_ provided though, we need to load our state out of a file. In the following code, change `r\_leguen` to your ENCS username:

    else {	# if a session ID is provided, we initialize session data.
    	$sessionID = $params{"SESSIONID"};
    	open("SESSION", "</tmp/r_leguen.cgi_blackjack.".$sessionID);
    	# we read the first line,
    	# which is the list of cards in the deck
    	# seperated by commas
    	$cards = <SESSION>;
    	chomp($cards);
    	@deck = split(/,/, $cards);
    	
    	# we read the second line,
    	# which is the list of cards in the hand
    	# seperated by commas
    	$cards = <SESSION>;
    	chomp($cards);
    	@player = split(/,/, $cards);
    	
    	# we read the third line,
    	# which is the list of cards in the computer's hand
    	# seperated by commas
    	$cards = <SESSION>;
    	chomp($cards);
    	@dealer = split(/,/, $cards);
    	
    	# we read the fourth line,
    	# which is the list of cards in the deck
    	# seperated by commas
    	$cards = <SESSION>;
    	chomp($cards);
    	@discard = split(/,/, $cards);
    	close(SESSION);
    }

If neither the payer nor the dealer have any cards, it means we’re playing a new game and need to deal cards to them:

    if(!@player && !@dealer) {
    	for($i=0; $i<2; $i++) {
    		push(@player, pop(@deck));
    		push(@dealer, pop(@deck));
    	}
    }

We’re going to communicate what the player wants to do (Hit or Stand) via another GET parameter, called "Action".

    if($params{"Action"} eq "Hit") {
    	push(@player, pop(@deck));
    	if(!@deck) {
    		# if the player draws
    		# all the cards from
    		# the deck, we shuffle the 
    		# discard pile back in.
    		@deck = shuffle(@discard);
    		@discard = ();
    	}
    }
    elsif($params{"Action"} eq "Stand") {
    	$dealerScore = 0;
    	for($i=0; $i<@dealer; $i++) {
    		$card = $dealer[$i];
    		if($card =~ /(\d+)/) {
    			$dealerScore += $1;
    		}
    		else {
    			$dealerScore += 10;
    		}
    		# the dealer has to keep drawing cards
    		# until his score is 17 or higher
    		if($dealerScore < 17 && $i+1 >= @dealer) {
    			push(@dealer, pop(@deck));
    			if(!@deck) {
    				# if the dealer draws
    				# all the cards from
    				# the deck, we shuffle the 
    				# discard pile back in.
    				@deck = shuffle(@discard);
    				@discard = ();
    			}
    		}
    	}
    }

Now that we’ve handled any actions the user wants to make, we begin our output:

    print "Content-Type: text/html\n";
    print "\n";
    	
    print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\"".
    	" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional-dtd\">\n";
    print "<html>\n";
    print "<head>";
    print "<title>CGI BlackJack</title>";
    print "</head>\n";
    print "<body>\n";

We’ll print an `<h1>` header with the name of our page:

    print "<h1>Welcome To CGI BlackJack</h1>\n";

We will now output the dealer’s hand. We are going to hotlink to images on wikimedia commons, such as this playing card clipart:  
![http://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Ornamental_s_8.svg/140px-Ornamental_s_8.svg.png](http://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Ornamental_s_8.svg/140px-Ornamental_s_8.svg.png)  
Take note that only the first card of the dealer’s hand is revealed until the player chooses to ‘Stand’.

    print "<h2>Dealer's Hand:</h2>\n";
    print "<p>\n";
    	if(@dealer) {
    		print "<div>";
    		print "<img src=\"". # we always output the dealer's first card
    			"http://upload.wikimedia.org".
    			"/wikipedia/commons/thumb/e/ef/".
    			"Ornamental_".$dealer[0].".svg/".
    			"140px-Ornamental_".$dealer[0].".svg.png".
    		"\" alt=\"".$dealer[0]."\" />";
    		print "&nbsp;";
    		for($i=1; $i<@dealer; $i++) {
    			if($params{"Action"} eq "Stand") {
    					# the dealer's other cards
    					# are only output when the
    					# player chooses to 'Stand'
    				print "<img src=\"".
    					"http://upload.wikimedia.org".
    					"/wikipedia/commons/thumb/e/ef/".
    					"Ornamental_".$dealer[$i].".svg/".
    					"140px-Ornamental_".$dealer[$i].".svg.png".
    				"\" alt=\"".$dealer[$i]."\" />&nbsp;";
    			}
    			else {
    					# If the player has not
    					# chosen to stand we display 
    					# the backs of cards
    					# (as they are face-down)
    				print "<img src=\"".
    					"http://upload.wikimedia.org/".
    					"wikipedia/commons/thumb/c/cc/".
    					"Back03.svg/".
    					"140px-Back03.svg.png".
    				"\" alt=\"?\"/>&nbsp;";
    			}
    		}
    		print "</div>";
    	}
    print "</p>";

Next, we output the player’s hand. The player’s hand is always visible.

    print "<h2>Your Hand:</h2>\n";
    print "<p>\n";
    	if(@player) {
    		print "<div>";
    		for($i=0; $i<@player; $i++) {
    			print "<img src=\"".
    				"http://upload.wikimedia.org/".
    				"wikipedia/commons/thumb/e/ef/".
    				"Ornamental_".$hand[$i].".svg/".
    				"140px-Ornamental_".$hand[$i].".svg.png".
    			"\" alt=\"".$player[$i]."\" />&nbsp;";
    		}
    		print "</div>";
    	}
    print "</p>\n";

At the bottom of the page, we include hyperlinks to either "Hit" or "Stand". Take note that these hyperlinks contain query strings in their `href` attributes, and as such they will send the following GET parameters to the server:

*   Action
*   SESSIONID

The SESSIONID is important; without it we lose our session and the game has to start over.

    if($params{"Action"} eq "Stand") {
    	while(@player) { # we empty the player's hand into the discard pile
    		push(@discard, pop(@player));
    	}
    	while(@dealer) { # we empty the dealer's hand into the discard pile
    		push(@discard, pop(@dealer));
    	}
    	print "<a href=\"BlackJack.cgi?SESSIONID=".$sessionID."\"".
    	# this hyperlink includes the SESSIONID
    	# in the URL's query string
    		" title=\"Click to Keep Playing\">Play Again?</a>";
    }
    else {
    	print "<a href=\"".
    			"BlackJack.cgi?Action=Hit&SESSIONID=&uuot;.$sessionID."".
    			# this hyperlink includes the SESSIONID
    			# in the URL's query string
    		"\" title=\"Draw another card?\">";
    		print "Hit";
    	print "</a>";
    	print " or ";
    	print "<a href=\"".
    			"BlackJack.cgi?Action=Stand&SESSIONID=".$sessionID."".
    		"\" title=\"Don't draw any more cards?\">";
    			# this hyperlink includes the SESSIONID
    			# in the URL's query string
    		print "Stand";
    	print "</a>";
    }

We complete our HTML document:

    print "</body>\n";
    print "</html>";

… BUT we’re not done. We _still_ have to _save_ the session state.

    # save session information in a file
    open("SESSION", ">/tmp/r_leguen.cgi_blackjack.".$sessionID);
    print SESSION join(",",@deck)."\n";
    print SESSION join(",",@player)."\n";
    print SESSION join(",",@dealer)."\n";
    print SESSION join(",",@discard)."\n";
    close(SESSION);

You’re now ready to play some Blackjack! If you’re having trouble following the code segments in this tutorial, download the script [here](assets/BlackJack.cgi).

The Disadvantages of Maintaining State Using Query Strings
----------------------------------------------------------

When you use query strings to maintain state, you have to include the SESSIONID in the URL. This means that every hyperlink in the document has to include the query string. If you forget t include it in the `href` attribute of a hyperlink, or if the user leaves the page, their session is ‘lost’.

### Session Hijacking

It’s also much easier for a web page which uses query strings to maintain state to suffer what is called a [session hijacking attack](http://en.wikipedia.org/wiki/Session_hijacking), as the SESSIONID is completely exposed; all you have to do to gain access to someone else’s session is "shoulder surf", remember the SESSIONID, and manually add it to the query string of a URL in your own browser.

#### Session Fixation

This also makes the web site vulnerable to the slightly more complicated [session fixation attack](http://en.wikipedia.org/wiki/Session_fixation), where an attacker causes the victim to use a SESSIONID they have already chosen; all they have to do is include a hyperlink to:

    BlackJack.cgi?SESSIONID=12345

…in an email for example. When the target clicks on the link, their SESSIONID has been chosen by the attacker, and the victim’s session can now be hijacked. To mitigate the risk of session fiation attacks, we could split the following if statement in two:

    if(!$params{"SESSIONID"} || !-e "/tmp/r_leguen.cgi_blackjack.".$params{"SESSIONID"}) {

… because if the parameter exists, but the file with the session data does not, this is probably an attack.

### Cross Site Request Forgery (XSRF)

This web page is also vulnerable to a _Cross Site Request Forgery_ attack, but we’ll get into that later.
