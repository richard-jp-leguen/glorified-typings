#!/usr/bin/perl --

use List::Util 'shuffle';

%params = ();
$queryString = $ENV{"QUERY_STRING"};
@keyValuePairs = split(/\&/, $queryString);
foreach my $keyValuePair (@keyValuePairs) {
	($key, $value) = split(/\=/, $keyValuePair);
	$key =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the key
	$value =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the value
	$params{$key} = $value;
}

#We now read the cookies
%cookies = ();
$cookieHeader = $ENV{"HTTP_COOKIE"};
	# Why "HTTP_COOKIE" instead of "COOKIE"?
	# The 'Cookie' request header is newer
	#  than the CGI specification, 
	#  and headers no in the specification
	#  get the 'HTTP_' prefix
@keyValuePairs = split(/; /, $cookieHeader);
foreach my $keyValuePair (@keyValuePairs) {
	($key, $value) = split(/\=/, $keyValuePair);
	$cookies{$key} = $value;
}

@deck = ();
@player = ();
@dealer = ();
@discard = ();

if(!$cookies{"SESSIONID"} || !-e "r_leguen.cgi_blackjack.".$cookies{"SESSIONID"}) {
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
	$sessionID = int(rand(999999999999999)).time();
	print "Set-Cookie: SESSIONID=".$sessionID."; expires=Fri, 31-Dec-2010 23:59:59; path=/; domain=".$ENV{"SERVER_NAME"}."\n";

}
else {	# if a session ID is provided, we initialize session data.
	$sessionID = $cookies{"SESSIONID"};
	open("SESSION", "<r_leguen.cgi_blackjack.".$sessionID);
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

if(!@player && !@dealer) {
	for($i=0; $i<2; $i++) {
		push(@player, pop(@deck));
		push(@dealer, pop(@deck));
	}
}

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

print "Content-Type: text/html\n\n";

print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional-dtd\">\n";
print "<html>\n";
print "<head>";
print "<title>CGI BlackJack</title>";
print "</head>\n";
print "<body>\n";
print "<h1>Welcome To CGI BlackJack</h1>\n";
print "<h2>Dealer's Hand:</h2>\n";
print "<p>\n";
	if(@dealer) {
		print "<div>";
		print "<img src=\"http://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Ornamental_".$dealer[0].".svg/140px-Ornamental_".$dealer[0].".svg.png\" alt=\"".$dealer[0]."\" />&nbsp;";
		for($i=1; $i<@dealer; $i++) {
			if($params{"Action"} eq "Stand") {
				print "<img src=\"http://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Ornamental_".$dealer[$i].".svg/140px-Ornamental_".$dealer[$i].".svg.png\" alt=\"".$dealer[$i]."\" />&nbsp;";
			}
			else {
				print "<img src=\"http://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Back03.svg/140px-Back03.svg.png\" alt=\"?\"/>&nbsp;";
			}
		}
		print "</div>";
	}
print "</p>";
print "<h2>Your Hand:</h2>\n";
print "<p>\n";
	if(@player) {
		print "<div>";
		for($i=0; $i<@player; $i++) {
			print "<img src=\"http://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Ornamental_".$player[$i].".svg/140px-Ornamental_".$player[$i].".svg.png\" alt=\"".$player[$i]."\" />&nbsp;";
		}
		print "</div>";
	}
print "</p>\n";
if($params{"Action"} eq "Stand") {
	while(@player) {
		push(@discard, pop(@player));
	}
	while(@dealer) {
		push(@discard, pop(@dealer));
	}
	print "<a href=\"BlackJackWithCookies.cgi?SESSIONID=".$sessionID."\" title=\"Click to Keep Playing\">Play Again?</a>";
}
else {
	print "<a href=\"BlackJackWithCookies.cgi?Action=Hit\" title=\"Draw another card?\">Hit</a> or <a href=\"BlackJackWithCookies.cgi?Action=Stand\" title=\"Don't draw any more cards?\">Stand</a>";
}
print "</body>\n";
print "</html>";

# save session information in a file
open("SESSION", ">r_leguen.cgi_blackjack.".$sessionID);
print SESSION join(",",@deck)."\n";
print SESSION join(",",@player)."\n";
print SESSION join(",",@dealer)."\n";
print SESSION join(",",@discard)."\n";
close(SESSION);

