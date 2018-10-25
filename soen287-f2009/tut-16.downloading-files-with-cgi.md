Downloading Files With CGI
==========================

We are now going to change the `FileExplorer.cgi` script so that it allows you to download files from the server’s file system.

Open your `FileExporer.cgi` script, and find the code which executed when the FilePath didn’t correspond to a directory.

    elsif(!-d $filePath) {
    	print "Content-Type: text/html\n\n";
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

We’re going to be modifying the contents of this `elsif` block. Before we get into it, put some files in your web space; add some more html files, some text files, and some files which are not text files or html files or cgi files, so we can try downloading them. I’d suggest at least one image and one PDF file.

Downloading a File With Perl CGI
--------------------------------

Its as easy as including the contents of the file in your output’s body.

    elsif(!-d $filePath) {
    	print "Content-Type: text/html\n\n";
    	
    	open("DOWNLOADFILE", "<".$filePath);
    	while($fileContents = <DOWNLOADFILE>) {
    		print $fileContents;
    	}
    	close DOWNLOADFILE;
    }

You can now click on non-directory files in your FileExplorer and download them. Try downloading an HTML document, then a text document and a CGI script.

(if you’re alarmed you can use this FileExplorer to download CGI scripts, you’re ahead of the curve! Check out the next tutorial, [Security Issues With Your CGI File Explorer](tut-17.security-issues-with-cgi.md))

You may notice things don’t look right. If you think that’s bad, now try to download your other files; they will look like complete jargon!

That is because we left the `Content-Type: text/html` header in our response. Not all these files are HTML files. We need to change the Content-Type depending on the type of file `$filePathcode> corresponds to.`

`

We're going to determine the appropriate Content-Type using the file's extension:

|File Extension|Content-Type|
|--- |--- |
|.html|Content-Type: text/html|
|.htm|Content-Type: text/html|
|.css|Content-Type: text/css|
|.txt|Content-Type: text/plain|
|.xml|Content-Type: text/xml|
|.gif|Content-Type: image/gif|
|.jpeg|Content-Type: image/jpeg|
|.jpg|Content-Type: image/jpeg|
|.png|Content-Type: image/png|
|.mp3|Content-Type: audio/mpeg|
|.pdf|Content-Type: application/pdf|
|.php|Content-Type: text/plain|
|.cgi|Content-Type: text/plain|
|other|Content-Type: application/octet-stream|


So if we add a bunch of if-elsif blocks to our code…

    elsif(!-d $filePath) {
    	if($filePath =~ /\.html$/) {	print "Content-Type: text/html\n\n"; }
    	elsif($filePath =~ /\.htm$/) {	print "Content-Type: text/html\n\n"; }
    	elsif($filePath =~ /\.css$/) {	print "Content-Type: text/css\n\n"; }
    	elsif($filePath =~ /\.txt$/) {	print "Content-Type: text/plain\n\n"; }
    	elsif($filePath =~ /\.xml$/) {	print "Content-Type: text/xml\n\n"; }
    	elsif($filePath =~ /\.gif$/) {	print "Content-Type: image/gif\n\n"; }
    	elsif($filePath =~ /\.jpeg$/) {	print "Content-Type: image/jpeg\n\n"; }
    	elsif($filePath =~ /\.jpg$/) {	print "Content-Type: image/jpeg\n\n"; }
    	elsif($filePath =~ /\.png$/) {	print "Content-Type: image/png\n\n"; }
    	elsif($filePath =~ /\.mp3$/) {	print "Content-Type: audio/mpeg\n\n"; }
    	elsif($filePath =~ /\.pdf$/) {	print "Content-Type: application/pdf\n\n"; }
    	elsif($filePath =~ /\.php$/) {	print "Content-Type: text/plain\n\n"; }
    	elsif($filePath =~ /\.cgi$/) {	print "Content-Type: text/plain\n\n"; }
    	else {				print "Content-Type: application/octet-stream\n\n"; }
    	
    	open("DOWNLOADFILE", "<".$filePath);
    	while($fileContents = <DOWNLOADFILE>) {
    		print $fileContents;
    	}
    	close DOWNLOADFILE;
    }

... we can now download non-html files using our `FileExplorer.cgi` script.
