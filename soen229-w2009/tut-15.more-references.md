# More on References

## Pass-By-Reference

So we've seen a module, `GetOpt::Std` which provides a subroutine, `getopts`, which populates a hash:

    getopts(\%myoptions);
    # %myoptions has now had key-value pairs inserted into it.

This practice is referred to as _pass-by-reference_.

What if we want to write a subroutine which accepts pass-by-reference parameters? You might _think_ it's easy, but there's a slight twist.

We're going to write a method which accepts a reference to an array as a parameter, and populates it with the words for a simple hello world message. The first step is to declare the method: (I'm also including a call, furthur down in the code)

    sub populateArray() {

    }

    &populateArray(\@myArr);
    print @myArr;
    print "\n";

... and the second would be to check if the parameter is a valid reference to an array.

    sub populateArray() {
    	if(ref($_[0]) ne "ARRAY") {
    		print "Invalid parameter to subroutine 'populateArray'\n";
    		print "Expected a reference to an array.\n";
    		die();
    	}
    }

    &populateArray(\@myArr);
    print @myArr;
    print "\n";

You might think the last step is to de-reference our parameter, and populate it like so:

    sub populateArray() {
    	if(ref($_[0]) ne "ARRAY") {
    		print "Invalid parameter to subroutine 'populateArray'\n";
    		print "Expected a reference to an array.\n";
    		die();
    	}
    	@arr = @{$_[0]};
    	$arr[0] = "Hello";
    	$arr[1] = "World";
    }

    &populateArray(\@myArr);
    print @myArr;
    print "\n";

But this won't work. The output is blank. That's because the following line of code does not retain any relationship between the parameter which was passed into the subroutine, and the variable @arr:

    @arr = @{$_[0]};

Think about it this way: what happens when you run the following code?

    @arr1 = ("Bah", "Bah", "Black", "Sheep");
    @arr2 = @arr1;
    $arr2[2] = "White";
    print @arr1;
    print "\n";

The output is "BahBahBlackSheep" because the initialization of @arr2 in fact just copies all the elements of @arr1, and @arr2 is completey independant of @arr1.  
So likewise the following line of code just dereferences our parameter, and copies the elements of the dereferenced array into a new array.

    @arr = @{$_[0]};

If we want to manipulate the parameter which was passed in directly we have to manipulate it without assigning it to a new array:

    sub populateArray() {
    	if(ref($_[0]) ne "ARRAY") {
    		print "Invalid parameter to subroutine 'populateArray'\n";
    		print "Expected a reference to an array.\n";
    		die();
    	}
    	@{$_[0]}[0] = "Hello";
    	@{$_[0]}[1] = "World";
    }

    &populateArray(\@myArr);
    print @myArr;
    print "\n";

... and _voila_! We have now manipulated a parameter which was passed by reference. You could have also used pointer arrow notation:

    sub populateArray() {
    	if(ref($_[0]) ne "ARRAY") {
    		print "Invalid parameter to subroutine 'populateArray'\n";
    		print "Expected a reference to an array.\n";
    		die();
    	}
    	$_[0]->[0] = "Hello";
    	$_[0]->[1] = "World";
    }

    &populateArray(\@myArr);
    print @myArr;
    print "\n";

... which I encourage you to use, as it will help you understand objects a little more; both in Perl and in Java if you're lucky.

## References and Objects (optional)

Before I begin, I should emphasise that the contents of this tutorial past this point are **completely** optional. I should emphasise that 99 out of 100 times, objects in Perl are excessive. If they're _not_ useless in some project, I would be personally inclined to think you shouldn't be using Perl for that project.

### Why a Tutorial on Perl Objects if They're Useless?

When we spoke about references, I mentioned how you also use references in Java. In Java, Objects are references, and consequently are always passed by reference when used as parameters. Java does you a wonderful favor though, and hides any use of references from the developer. In Perl, however, since we've seen references up close a little, we should be able to get a better grip on what's happening.

I won't be showing you how to define classes and objects; I'll just show you a couple of lines of code which use objects in Perl.

So here's a little bit of code which uses objects in Perl. In order for it to work, you will have to download the [Dog.pm](scripts/Dog.pm) script in which I have defined class `Dog`. (we're not going to define class `Dog` together as defining objects in Perl is – in my opinion – the most digusting and nonsensical part of Perl syntax) You'll then have to `require` the 'Dog.pm' script.

    require 'Dog.pm';

    $myDog = Dog->new("Rex");	# this is usually how you 
    				# create a new object in Perl
    				# but it's not always the case…
    print $myDog." is a ".ref($myDog)." named ".$myDog->getName()."\n";

The output to this program should look something like this:

    Dog=HASH(0 × 814eb44) is a Dog named Rex

Take note that here we used pointer-arrow notation to invoke the `getName()` method. Essentially, the object is a very special reference. Take note that when we printed the `$myDog` variable, its type was "`Dog=HASH`". This is becuase thae `$myDog` object is a reference to a Hash, which has been given methods associated with a Dog. (yes, in my definition of the Dog type, I could have chosen to make Dog objects reference to arrays of scalars even… but I like hashes)

## Comparison With Java

For contrast I'm going to write very similar code in Java: (I've removed the part where we use `ref` as that touches on slightly more advanced Java topics)

    import soen229.perl.Dog;

    class DogExample {

    	public static void main(String[] argv) {
    		Dog myDog = new Dog("Rex");
    		System.out.println(myDog+" is a Dog named "+myDog.getName());
    	}

    }

The output is probably quite similar to what we got in Perl, with the the first bit being a little different…

Take note that in Java, the primitive types are quite simply information, like 'normal' scalar variables in Perl. But objects – which are passed by reference – we need to always manipulate with dot syntax, just the same way that we manipulate references in Perl using the pointer-arrow notation.

That's because, _objects in Java are references_. It's harder to see in Java – since we're not allowed to manipulate references in the same ways we do in Perl – but that's the reality.
