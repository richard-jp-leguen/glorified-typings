# Command Line Options & the lstat function (February 18th, 2009)

So we've seen iNodes in class, and now we want to poke around with them on the Linux command line, and then in Perl. Today we're going to review some of the command line tools which allow you to view the iNode information for a file, as well as learn to write some corresponding Perl scripts.

## Linux Command Line – `stat`

You can use the Linux command line tool `stat` to view the iNode information for a particular file:

    stat script.pl
      File: `script.pl'
      Size: 289       	Blocks: 8          IO Block: 4096   regular file
    Device: bh/11d	Inode: 3881        Links: 1
    Access: (0644/-rw-r--r--)  Uid: ( 1000/    user)   Gid: ( 1000/    user)
    Access: 2009-01-24 12:47:30.000000000 -0500
    Modify: 2009-01-13 15:01:49.000000000 -0500
    Change: 2009-01-13 15:01:49.000000000 -0500

## Perl – the `lstat` Function

Perl provides a function, `lstat`, which returns iNode information. It returns an array of data. The following code could serve as a very poor implementation of the Linux command line tool `lstat` were it written in Perl:

    @data = lstat($filename);

    print "Device Number: ".$data[0]."\n";
    print "iNode Number: ".$data[1]."\n";
    print "Mode: ".$data[2]."\n"; #this one is interesting
    print "No of hard links: ".$data[3]."\n";
    print "User id of owner: ".$data[4]."\n";
    print "Group id of owner: ".$data[5]."\n";
    print "Device identifier: ".$data[6]."\n";
    print "File size in bytes: ".$data[7]."\n";
    print "Time the data was last accessed: ".$data[8]."\n";
    print "Time the data was last modified: ".$data[9]."\n";
    print "Time the iNode was last modified: ".$data[10]."\n";
    print "Preferred block size for filesystem I/O: ".$data[11]."\n";
    print "Allocated blocks: ".$data[12]."\n";

This isn't ideal, since – unless you memorize the order the data is given in – its not very clear what each index in the array is or represents. As such the following trick is often used:

    ($dev, $ino, $mode, $nlink, $uid, $gid,
      $rdev, $size, $atime, $mtime, $ctime, $blksize, $blocks) = lstat($filename);

What do all these values mean, though?

*   **Device Number:** the numeric identifier of the device upon which the iNode this file corresponds to is stored.
*   **INode Number:** the numeric identifier of the iNode. Combined with the device number, this creates a unique identifier for this particular file.
*   **Mode:** The mode is a 16-bit number. Its first four bits define the type of the file, followed by the _suid bit_, the _sguid bit_, the _sticky bit_, and then 9 bits representing the permissions on this file. We'll talk more about the permission bits later in this tutorial.
*   **No. of Hard Links:** Each iNode keeps track of the number of hard links which exist to it; that is, the number of entries in directory files which point to this iNode.
*   **User id of owner:** The numeric identifier of the file's owner. (usually the user who created it) We'll be using this later…
*   **Group id:** The numeric identifier of the group the file belongs to. (usually the group to which the owner belonged when the file was created) We'll also be using this later…
*   **Device Identifer:** Used only for special device files.
*   **File size:** ... in bytes
*   **Last Access Time:** When the file's contents were last read.
*   **Last Modification Time:** When the file's contents were last changed.
*   **iNode's Last Modification Time:** When the iNode's info was last changed. (what's the difference?)

The other fields aren't as important for now.

### Why Are We Using `lstat` Instead of `stat`?

If you're familiar with Perl, you might know that there are two functions like this; `stat` and `lstat`. The difference is that `stat` won't give you the information for a symbolic link file; it will follow the link and give you information from the actual file. `lstat` doesn't do that, and since we want to be able to distinguish between symbolic link files and "real" files, we're going to use `lstat` instead.

## Linux Command Line – `ls` – (again)

So we've already seen how to write a script which behaves like the Linux command line tool `ls` and we're now going to expand on it some more to include some switches.

### Command Line: Switches (or Options)

On the Linux Command Line, `man` the `ls` command. The man page for `ls` includes a list of options, such as `-a`, `-b`, `-c`, `-l`, etc. These are options (also called switches) which you can use to change the behavior of the `ls` tool. So, for example, if I want to list the files and directories in `/home/r_leguen` I could type `ls /home/r_leguen` but if I want to also get a list of all the directories found in the directories in that folder, I could use the `-R` option, `ls -R /home/r_leguen`.

Note that switches are unique to every executable. Just because `-R` does one thing for `ls` doesn't mean it will have the same affect (or any effect!) on another program.

We're going to look at two switches for the `ls` tool: `-i` and `-l`, and then we're going to add them to our `ls` Perl script from tutorial #1.

### The `-l` and `-i` Switches for `ls`

When you execute `ls` and specify the `-l` option, `ls -l`, a long list format is used. For each file, the `ls` command will display its permissions, the number of hard links to its iNode, the file's owner, group, and size, the date the file was last modified, as well as the file's name.

When you execute `ls` and specify the `-i` option, `ls -i`, a long list format is used. For each file, the `ls` command will display the file's iNode number. we can specify both options by typing either `ls -l -i` on the command line, or `ls -li` on the command line.

## Options in Perl

So what if we want to take our `ls` Perl script from tutorial #1? For reference purposes, here is the original `ls` script we wrote:

    @allFiles = glob("*"); # a list of all files
    for($i=0; $i<@allFiles; $i++) {
    	print $allFiles[$i]."\n";
    }
    print "\n";

In order to read the command-line options (switches) we need to use the Perl module `Getopt::Std` which provides us with a function, `getopts(…)` which allows us to populate a hash's keys with the switches which have been set.

### The Getopt::Std Module

Before we add switches (or options) to our `ls` script, we're going to write a script to demonstrate the Getopt::Std module. As stated above, Getopt::Std provides a function, `getopts` which populates the keys of a hash with the command-line switches specified. This function takes two parameters though; the first is a string consisting of all valid options (options can only be a single character using Getopt::Std) and the second is our hash reference:

    use Getopt::Std;

    my %options = ();
    getopts("asdf", \%options);	# So this script accepts -a -s -d and -f as switches.
    				# Any others, and we'll
    				# get an "Unknown option" message,
    				# and then option will be discarded.
    foreach my $key (keys %options) {
    	print $key." => ".$options{$key}."\n";
    }

So – returning to the Perl script to behave like the `ls` tool – the valid switches we want to use are `-i` and `-l`. So the first parameter for our call to `getopts` will be either "il" or "li".

    use Getopt::Std;

    my %options = ();
    getopts("il", \%options);
    @allFiles = glob("*"); # a list of all files
    for($i=0; $i<@allFiles; $i++) {
    	print $allFiles[$i]."\n";
    }
    print "\n";

We can now enable/disable our `ls` Perl script from displaying extra information using switches… except that we still don't actually read the extra information. In order to achieve this, we need to use the `lstat` function. But which of all the values `lstat` returns do we need to implement our own version of `ls -l`? Let's take a look at a single row of the output from `ls -l`.

    -rw-r--r-x 2 r_leguen r_leguen   289 2009-01-13 15:01 myFile.txt

So, on the far left are the file's type (represented by a single character; see the ['Symbolic Notation' section of the wikipedia article on modes and permissions](http://en.wikipedia.org/wiki/File_permissions#Symbolic_notation)) and the last 9 bits in the file's modem, which the `lstat` function returns at index 2\. Those last nine bits represent: (starting with the most significant bit)

1.  if the file's owner has permission to read this file
2.  if the file's owner has permission to write to this file
3.  if the file's owner has permission to execute this file
4.  if users in the same group as the file's owner have permission to read this file
5.  if users in the same group as the file's owner have permission to write to this file
6.  if users in the same group as the file's owner have permission to execute this file
7.  if users who are neither the owner, nor in the same group as the file's owner have permission to read this file
8.  if users who are neither the owner, nor in the same group as the file's owner have permission to write to this file
9.  if users who are neither the owner, nor in the same group as the file's owner have permission to execute this file

So, in the case of the row we selected above:

    -rw-r--r-x 2 r_leguen r_leguen   289 2009-01-13 15:01 myFile.txt

We see that the file's owner has read and write permission; users in the owner's group have read permissions; and all other users have permissions to read and execute.

The next value (the '2' in our example row) is the number of hard links to this file's inode; each inode keeps track of the number of times it is listed in any directories.

The next two columns we get from `ls -l` are the owner and the owner's group. In Perl, the `lstat` function doesn't return us the name of the owner and group, but it does return their numeric ids, so we'll have to work some magic to get around that if we want to include this column in our `ls -i -l` implementation. That magic comes in the form of the `getpwuid` and `getgrgid` functions, which read the operating system's password file entry and return user information:

    ($dev, $ino, $mode, $nlink, $uid, $gid,
      $rdev, $size, $atime, $mtime, $ctime, $blksize, $blocks) = lstat($filename);
    ($username, $passwd, $uid, $groupid) = getpwuid($uid);
    	# don't get too excited; the password is encrypted
    print "The owner of the file is: ".$username."\n";
    ($groupname, $passwd, $gid, $members) = getpwuid($gid);
    print "The file belongs to the group: ".$groupname."\n";

Returning to the single row of ourput from `ls -l`, The group information for the file is followed by the file's size in bytes, the date when it was last modified, and the filename. We can format the date modified using `localtime` in scalar context, which allows us to format a string:

    $mod_date = localtime($mtime);
    print $mod_date."\n";

(the `localtime` function can also be used to return an array of information about a timestamp… but its more challenging to format it then…)

    ( $sec, $min, $hour, $mday,
    	$month, $year, $wday, $yday, $isdst ) = localtime($mtime);

So now, we know what fields we would include, its all just a matter of formatting.

I don't have space enough to write all the code for `ls -l` in this tutorial, so I will only demo how to add the `-i` option to your `ls` script in full:

    use Getopt::Std;

    my %options = ();
    getopts("il", \%options);
    @allFiles = glob("*"); # a list of all files
    for($i=0; $i<@allFiles; $i++) {
    	if($options{'i'}) {
    		($dev , $ino) = lstat($allFiles[$i]); # the left side of this
    					 # assignment looks weird…
    					 # I'm essentilly only reading
    					 # the 1st and 2nd values of the array,
    					 # and discarding all others.
    		print $ino." "; # $ino received the value of the iNode number.
    	}
    	print $allFiles[$i]."\n";
    }
    print "\n";

To run your Perl script and specify an option, specify the options _after_ the name of the script.

    perl Script.pl -i

If you put the options before the file name, they are instead applied to the interpreter:

    perl -i Script.pl	# This is wrong!
    			# you're running the Perl interpreter
    			# with the -i option,
    			# which does something… different.

Or, if your script has executable permissions:

    ./Script.pl -i
