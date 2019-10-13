References in Perl (February 18th, 2009)
==================

Suppose we wanted to write a subroutine in Perl which finds the highest value in a hash? (remember: in a hash, there are _keys_ which map onto _values_, so that statement is not ambiguous…) With what we know so far, we can’t, as Perl only allows us to pass scalar variables as parameters to subroutines.

Equally, what if we need a two-dimensional array? ie an array of arrays? In Perl, we’re only allowed to assign scalar values to the elements of an array, so how could we have multi-dimensional arrays?

In order to get past these problems we need to somehow be able to either turn an array (or hash) into a scalar variable. Your first guess might be to cast from one type to another, but this is totally wrong! Perl explicitly does not support type casting, and it is not considered a shortcoming, but a feature.

So instead we have to use _references_.

The idea is to have a scalar variable which references something else (possibly a non-scalar variable). By ‘references’, we mean that our scalar variable (the _reference_) holds the address in-memory of another value (the _referent_). Understanding that isn’t as important as being able to use them within the scope of this course, but I’ll elaborate on it a little more:

References: An Analogy
----------------------

In the past, the SOEN229 Professor was Dr. Atwood. Now, its Dr. Fancott. So the concept of “the SOEN229 prof” isn’t a person in and of itself. It _refers_ to someone. So we’re going to write a little Perl code, and in it we will define three variables: one which is Professor Atwood, one which is Professor Fancott, and one which is ‘the Professor of SOEN229′:

    $dr_atwood = "Professor Atwood";
    $dr_fancott = "Professor Fancott";
    $prof_of_soen229; # we're not assigning it a value just yet…
    print $prof_of_soen229;
    print "\n";

So when I took SOEN229 in… um, 2004, or something… Dr. Atwood was the professor, so I’m going to assign the variable `$prof_of_soen229` a reference to variable `$dr_atwood`:

    $dr_atwood = "Professor Atwood";
    $dr_fancott = "Professor Fancott";
    $prof_of_soen229 = \$dr_atwood; # its as easy as a slash characer!
    print $prof_of_soen229; # but the output will be weird…
    print "\n";

The output is something weird like `SCALAR(0 × 814f5c4)`, which is the location of the referant in-memory. In crazy-whacked-out-low-level computer lingo, this is kind of like where the SOEN 229 prof’s office is. It would be like if someone asked you “Hey, what’s the name of our SOEN 229 Prof?” and you said “Whoever is in office EV-3.118.” The answer is right, but not that useful.

So we need to _de-reference_ `$prof_of_soen229`. This is accomplished by putting the reference in braces `{}` and a dollar sign character (`$`) in front them:

    print ${$prof_of_soen229};

Now the output is “`Professor Atwood`” as one would expect. So we’re going to continue our program so that we re-assign the variable again:

    $dr_atwood = "Professor Atwood";
    $dr_fancott = "Professor Fancott";
    $prof_of_soen229 = \$dr_atwood; # its as easy as a slash characer!
    print ${$prof_of_soen229};
    print " in 2004-ish\n";
    $prof_of_soen229 = \$dr_fancott;
    print ${$prof_of_soen229};
    print " in 2009\n";

You know know the basics of references in Perl!

References to Arrays
--------------------

When would we want or need references to arrays? The first example which comes to mind is creating an array of arrays: Perl allows the elements of an array to contain only scalar variables. So we need to populate our array with references.

    @matrix = (); # just initializing the array.
    @row1 = ("0-0", "1-0", "2-0");
    $matrix[0] = \@row1;
    @row2 = ("0-1", "1-1", "2-1");
    $matrix[0] = \@row2;
    @row3 = ("0-2", "1-2", "2-2");
    $matrix[0] = \@row3;

But now, how do we output the contents of this two-dimensional array? Each element when we read it is a scalar:

    @matrix = (); # just initializing the array.
    @row1 = ("0-0", "1-0", "2-0");
    $matrix[0] = \@row1;
    @row2 = ("0-1", "1-1", "2-1");
    $matrix[0] = \@row2;
    @row3 = ("0-2", "1-2", "2-2");
    $matrix[0] = \@row3;
    
    for($i=0; $i<@matrix; $i++) {
    	print $matrix[$i]."\n"; # we can't loop over a scalar!
    }

So how to we de-reference `$matrix[$i]`? Before, we saw that a reference to a scalar could be dereferenced by putting it in braces and then putting a dollar sign character before them. Likewise, an array reference is dereferenced by putting a commercial at before it:

    @matrix = (); # just initializing the array.
    @row1 = ("0-0", "1-0", "2-0");
    $matrix[0] = \@row1;
    @row2 = ("0-1", "1-1", "2-1");
    $matrix[1] = \@row2;
    @row3 = ("0-2", "1-2", "2-2");
    $matrix[2] = \@row3;
    
    for($i=0; $i<@matrix; $i++) {
    	@row = @{$matrix[$i]};
    	for($j=0; $j<@row; $j++) {
    		print "| "$row[$j];
    	}
    	print "|\n";
    }

We can save ourselves some lines of code, and avoid having variables like `@row1`, `@row2` and `@row3` by using a shorthand to create references to arrays without identifiers:

    @matrix = (); # just initializing the array.
    $matrix[0] = ["0-0", "1-0", "2-0"];	# note that the right-side uses [ ]
    					# this creates an anonymous array
    					# and returns a reference to it
    $matrix[1] = ["0-1", "1-1", "2-1"];
    $matrix[2] = ["0-2", "1-2", "2-2"];

Here is the exact same code presented differently:

    @matrix = (	["0-0", "1-0", "2-0"],
    		["0-1", "1-1", "2-1"],
    		["0-2", "1-2", "2-2"]
    		);

References to Hashes
--------------------

What if we want to have a subroutine which searches a hash for its highest value? (note the difference between a hash’s _keys_ and its _values_!) Since Perl does not allow us to pass non-scalar value as parameters to subroutines, we’d have to pass a reference:

    %hash;
    $hash{"Software Process"} = 341;
    $hash{"System Software"} = 229;
    $hash{"Control Systems"} = 385;
    $hash{"Management and Quality Control"} = 384;
    $hash{"System Hardware"} = 228;
    $hash{"Design"} = 343;
    $hash{"Architecture"} = 344;
    
    &highestValueInHash(\%hash); # we are now passing a reference to the hash…
    
    sub highestValueInHash {
    	my %hashParam = %{$_[0]};
    	# ...
    }

Just like de-referencing a scalar, we used `${…}` and de-referencing an array we used `@{…}` we now see that we use `%{…}` to de-reference a hash.

As competent, responsible Java developers you should see a _big_ potential problem with the above script. If you don’t see the problem, here’s some Java code which has a similar problem. **IMPORTANT:** The code that follows is not the same code re-written in Java. It’s the same _bad programming_ being conveyed using Java.

    import soen229.perl.Hash;
    
    class ReferencesProblem {
    
    	public void highestValueInHash(Object o) {
    		Hash h = (Hash)o;
    	}
    
    }

In Java’s beautiful object oriented purity, I would say that this code is not **type safe**. What happens when someone passes in a an object which cannot be cast to a Hash?

Likewise in, Perl, what prevents me from calling my subroutine `highestValueInHash` with a scalar value parameter which is not a reference to a hash? What if its a reference to an array? What if its not really a reference at all? We need a way to double check these things if we’re going to write good re-usable code. This can be accomplished via the `ref` function.

The `ref` Function
------------------

The `ref` function takes a single scalar value as a parameter. If that value is a valid reference, it returns a string which specifies the type of the referent.

Try running this code to see how it works:

    $hashRef = \%hash;
    print ref($hashRef)."\n";
    
    $arrRef = \@array;
    print ref($arrRef)."\n";
    
    $scalarRef = \$scalar;
    print ref($scalarRef)."\n";
    
    $scalarRef2 = 10;	# so this one is an invalid reference
    			# since we're not de-referencing a variable
    print ref($scalarRef2)."\n";
    
    $refRef = \\$scalar;	# a reference to a reference… fancy stuff.
    print ref($refRef)."\n";

So we can now make our `highestValueInHash` a little safer, by checking that a valid reference has been passed in:

    %hash;
    $hash{"Software Process"} = 341;
    $hash{"System Software"} = 229;
    $hash{"Control Systems"} = 385;
    $hash{"Management and Quality Control"} = 384;
    $hash{"System Hardware"} = 228;
    $hash{"Design"} = 343;
    $hash{"Architecture"} = 344;
    
    &highestValueInHash(\%hash); # we are now passing a reference to the hash…
    
    sub highestValueInHash {
    	if(ref($_[0]) eq "HASH") {
    		my %hashParam = %{$_[0]};
    		# ...
    	}
    	else {
    		die("Invalid parameter: expected a reference to a hash. ");
    	}
    }

Multi-Dimensional Hashes
------------------------

What if we need a hash whose values are hashes? (or an array whose values are hashes?)

    %soenCourses;
    $soenCourses{"Software Process"} = 341;
    $soenCourses{"System Software"} = 229;
    $soenCourses{"Control Systems"} = 385;
    $soenCourses{"Management and Quality Control"} = 384;
    $soenCourses{"System Hardware"} = 228;
    $soenCourses{"Design"} = 343;
    $soenCourses{"Architecture"} = 344;
    
    %compSciCourses = ( # this is the quick way to initialize a hash
    		"Introduction to OOP" => 248,
    		"Programming Methodologies" => 249,
    		"Discrete Math I" => 238,
    		"Discrete Math II" => 239,
    		"Data Communication and Networking" => 445,
    		);
    
    %courses;
    $courses{"SOEN"} = \%soenCourses;
    $courses{"COMP"} = \%compSciCourses;

There is of course a shorthand to define a hash anonymously, just like an array:

    %courses;
    $courses{"SOEN"} = {	# note the squiggly braces
    			# they mean that this is an anonymous hash
    			# and we're assigning $courses{"SOEN"} a reference to it.
    		"Software Process" => 341,
    		"System Software" => 229,
    		"Control Systems" => 385,
    		"Management and Quality Control" => 384,
    		"System Hardware" => 228,
    		"Design" => 343,
    		"Architecture" => 344,
    		};
    $courses{"COMP"} = {	# note the squiggly braces
    			# they mean that this is an anonymous hash
    			# and we're assigning $courses{"COMP"} a reference to it.
    		"Introduction to OOP" => 248,
    		"Programming Methodologies" => 249,
    		"Discrete Math I" => 238,
    		"Discrete Math II" => 239,
    		"Data Communication and Networking" => 445,
    		};

Pointer-Arrow Notation
----------------------

Ever wonder why the array and hash use different brackets? If they can be distinguished by having identifiers which start with either a commercial at or a percent, why _also_ have different brackets?

    @this_is_an_array[0]; # why not @this_is_an_array{0} ?
    %this_is_a_hash{"key"}; # why not %this_is_a_hash["key"] ?

This is because references can be referred to two ways: the first way (above) involves dereferencing them, and it involves using the `@` and `%` symbols. The second way is to manipulate the referent directly using the reference, instead of dereferencing. When you do this – since the reference is always a scalar variable, and as such its variable name starts with `$` symbol – we need the different brackets to distinguish between what type we’re manipulating the referent as.

All this to say you can manipulate the referent directly using the reference using pointer-arrow notation, just like pointers in C.

    @chars = ("a", "b", "c");
    $ref = \@chars;
    print $ref->[0]; # prints "a"
    print "\n";

Let’s take a closer look at the line `print $ref->\[ 0 \];`. Specifically, we’re interested in `$ref->\[ 0 \]` which says “take `ref`, go to whatever it references (which is what the `->` means) and treat it like an array.”

Since, by contrast, a hash uses braces `{}` to refer to its elements, we can distinguish between hashes and arrays fairly easily:

    %retiredHabsNumbers;
    $retiredHabsNumbers{"Jacques Plante"} = 1;
    $retiredHabsNumbers{"Doug Harvey"} = 2;
    $retiredHabsNumbers{"Bob Gainey"} = 23;
    # ...
    $ref = \%retiredHabsNumbers;
    print $ref->{"Jacques Plante"}; # prints "1"
    print "\n";

Let’s take a closer look again. This time, at the line `print $ref->{‘Jacques Plante’};`. Specifically, we’re interested in `$ref->{‘Jacques Plante’}` which says “take `ref`, go to whatever it references (which is what the `->` means) and treat it like a hash.”

References to Subroutines
-------------------------

Elaborating a little more on what we saw in arrow-pointer notation, if you look at the syntax for the identifiers for non-scalar types, its always some non-letter character specifying type, followed by a name, an open-bracket, something, and then a corresponding close bracket.

    @myArrayVar[0];
    	# some non-letter character specifying type: @ for array
    	# followed by a name: myArrayVar
    	# an open-bracket: [
    	# something: the index 0
    	# and then a corresponding close bracket: ]
    %thisIsAHash{"lookup"};
    	# some non-letter character specifying type: % for hash
    	# followed by a name: thisIsAHash
    	# an open-bracket: {
    	# something: the key, "lookup"
    	# and then a corresponding close bracket: }

The same can be said of our user-defined subroutines:

    &mySuboutine($params);
    	# some non-letter character specifying type: & for subroutine
    	# followed by a name: mySuboutine
    	# an open-bracket: (
    	# something: the parameter(s) $params
    	# and then a corresponding close bracket: )

So in the end, our subroutine calls are non-scalar identifiers, and as such we can manipulate them via references! We can do this by de-referencing them with `&{…}` like this:

    sub I_cant_believe_it_works {
    	print $_[0]."\n";
    	print "HOLY CRAP THAT IS COOL.\n";
    }
    
    $myReference = \&I_cant_believe_it_works; # returns a reference to the subroutine.
    &{$myReference}("Does it work?");

Or, we can also use pointer-arrow notation:

    sub I_cant_believe_it_works {
    	print $_[0]."\n";
    	print "HOLY CRAP THAT IS COOL.\n";
    }
    
    $myReference = \&I_cant_believe_it_works;
    $myReference->("Does it work?");

We could even just reference a subroutine with a scalar variable set to its name:

    sub I_cant_believe_it_works {
    	print $_[0]."\n";
    	print "HOLY CRAP THAT IS COOL.\n";
    }
    
    $subroutineName = "I_cant_believe_it_works"; # this variable isn't a
                                                 # reference to a subroutine,
                                                 # but we can treat it as such.
                                                 # This isn't a great idea though…
    &{subroutineName}("Does it work?");

… and that concludes this week’s tutorial on references in Perl! There’s more this week though; we learned to use references in Perl so we could see the `Getopt::Std` module to read command line switches and options.
