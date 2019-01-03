AssertionFailedEror: Class has no public constructor
====================================================

If you are consistently getting a red bar and a `junit.framework.AssertionFailedError` in your Failure trace which looks a little like this:

    Class YourTestCase has no public constructor YourTestCase(String name) or YourTestCase()

… then you have a problem with the visibility of your constructor or of the entire class.

Visibility Of The Constructor
-----------------------------

Your JUnit Test Case always has to have either a default public constructor:

    public class YourtestCase extends TestCase {
    	
    	public YourtestCase() { }	// if you include no constructors,
    					// a default constructor is included implicitly
    	
    }

Or a public constructor which takes a `String` as an argument:

    public class YourtestCase extends TestCase {
    	
    	public YourtestCase(String name) { }
    	
    }

If you don’t specify one of these you will get the `no public constructor` failure described above.

**The following is a Fail:**

    public class YourtestCase extends TestCase {
    	
    	protected YourtestCase() { }
    	YourtestCase(String name) { }
    	
    	public YourtestCase(Object wtv) { }
    	
    	// There isn't a constuctor which is both public,
    	// and takes either nothing or a String as an argument
    	
    }

Visibility Of The Class
-----------------------

The other problem could be with the visibility of the entire class. \*Note the presence of the word `public` before the keyword `class` in the following:

    public class YourtestCase extends TestCase {
    	
    	// ...
    	
    }

If you neglect it, your class doesn’t have public visibility and JUnit cannot use it as a Test Case:

**The following is a Fail:**

    class YourtestCase extends TestCase {
    	// This class doesn't have public visibility!
    	
    	public YourtestCase(String name) { }
    	
    }
