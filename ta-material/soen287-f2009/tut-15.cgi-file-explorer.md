A CGI File Explorer
===================

We’re going to write a little CGI File explorer. It will allow you to navigate – in the browser – the contents of your web space.

We will want the File Explorer to accept – as a GET parameter- the path to a directory. It should then display a list of files in that directory, including hyperlinks to Explore those paths.

Writing the `FileExplorer.cgi` Script
-------------------------------------

Create a new file and call is `FileExplorer.cgi`. As usual, the first line of our script has to be a shebang:

    #!/usr/bin/perl --

The File Explorer will be manipulating directory paths using the `abs_path` function. This function has to be imported with a `use` statement:

    use Cwd 'abs_path';

We now include our code to read, and parse the query string:

    %params = ();
    $queryString = $ENV{"QUERY_STRING"};
    @keyValuePairs = split(/\&/, $queryString);
    foreach my $keyValuePair (@keyValuePairs) {
    	($key, $value) = split(/\=/, $keyValuePair);
    	$key =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the key
    	$value =~ s/%([a-f0-9]{2})/chr(hex($1))/eig; # URL decode the value
    	$params{$key} = $value;
    }

The only parameter we’re interested in is going to be on we’ll call `FilePath`. It will be the path to the directory we want to explore.

    if($params{"FilePath"}) {
    	$filePath = $params{"FilePath"};
    }
    else {
    	$filePath = "/.";
    }
    $filePath = abs_path($filePath); # removes things like ../ and ./ from the path

We need to perform some validating: up until now we have nothing which confirms we are allowed to read that directory, or that it even exists. We will use Perl file tests to determine if there is a file there that we can read:

    if(!-e $filePath) { # if the file does not exist
    	print "Content-Type: text/html\n\n";
    	print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" ".
    		"\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">";
    	print "<html>";
    	print "<body>";
    	print "<h1>File Browser</h1>";
    	print "<h2>Exploring Directory ".$filePath."</h2>";
    	print "<p>";
    	print "'".$params{"FilePath"}."' resolved to '".$filePath."',<br />";
    	print "and file '".$filePath."' does not exist.";
    	print "</p>";
    	print "</body>";
    	print "</html>";
    }
    elsif(!-r $filePath) { # if we cannot read the file
    	print "Content-Type: text/html\n\n";
    	print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" ".
    		"\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">";
    	print "<html>";
    	print "<body>";
    	print "<h1>File Browser</h1>";
    	print "<h2>Exploring Directory ".$filePath."</h2>";
    	print "<p>";
    	print "I do not have permission to read file '".$filePath."'.";
    	print "</p>";
    	print "</body>";
    	print "</html>&uuot;;
    }

NOTE: You might be wondering why we don’t output the `Content-Type` once, before the if-else… you can, and it will make your code easier to follow, but we’re going to be making furthur changes in future tutorials to this script, and that will make those changes a little more complicated.

Our last error is if the file path corresponds to a file which is not a directory.

    elsif(!-d $filePath) {
    	print "Content-Type: text/html\n\n";
    	print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" ".
    		"\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">";
    	print "<html>";
    	print "<body>";
    	print "<h1>File Browser</h1>";
    	print "<h2>Exploring Directory ".$filePath."</h2>";
    	print "<p>";
    	print "File '".$filePath."' is not a directory.";
    	print "</p>";
    	print "</body>";
    	print "</html>";
    }

… and now we get to the interesting part, where we explore a directory!

    else {
    	$filePath =~ s/([^\/])$/$1\//; # make sure there's a trailing slash
    	$filePattern = $filePath."*"; # the * is a wildcard when you're globbing
    	
    	@files = glob($filePattern);
    	
    	print "Content-Type: text/html\n\n";
    	print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" ".
    		"\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">";
    	print "<html>";
    	print "<body>";
    	print "<h1>File Browser</h1>";
    	print "<h2>Exploring Directory ".$filePath."</h2>";
    	print "<p>";
    	print "<ul>";
    	$upDir = abs_path($filePath."../");
    			# we append ../ to move 'up' one directory.
    			# the abs_path function resolves the "../"
    			# and returns the absolute path to the directory
    	print "<li>";
    	print "<a href=\"FileBrowser.cgi?FilePath=".$upDir."\">";
    		# take note! We have appended a query string to the 'href'
    		print $filePath."..";
    	print "</a></li>";
    	for $file (@files) {
    		print "<li><a href=\"FileBrowser.cgi?FilePath=".$file."\">".$file."</a></li>";
    	}
    	print "</ul>";
    	print "</p>";
    	print "</body>";
    	print "</html>";
    }

Deploy and Run The Script
-------------------------

Follow the steps from [this tutorial](tut-13.cgi-programming.md) on how to move the `FileBrowser.cgi` script to your web space, then browse to its URL and explore the file system a little!

Adding a Search
---------------

We’re now going to add a form to the CGI File Explorer, so that we can only display files from the directory whose names match a search pattern. Add the following to your CGI script where you list the files:

    	print "<form action='FileExplorer.cgi' method='GET'>";
    	print "<input type='hidden' name='FilePath' value='".$filePath."' />";
    	print "<label>Search for Files Matching: </label>";
    	print "<input type='text' name='Glob' />";
    	print "<input type='submit' value='Search!' />";
    	print "</form>";

This form will provide a second GET parameter, `Glob`, which we will use as a globbing pattern. Make the following change to your script, where you initialize the variable `$filePattern`:

    	if(!$params{"Glob"}) {
    		$filePattern = $filePath."*";
    			# the * is a wildcard when you're globbing
    	}
    	else {
    		$filePattern = $filePath.$params{"Glob"};
    	}

Now – in the browser – again visit `FileExplorer.cgi` and you should be presented with an input field and a ‘Search!’ button. Enter `\*.html` in the input field and search; you should see a list of only those files whose extension is `.html`.
