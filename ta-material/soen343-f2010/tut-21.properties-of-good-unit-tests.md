Properties of Good Unit Tests
=============================

So now we know What to Test, but ♫ it ain’t what you do, it’s the way that you do it. ♫. If tests are written poorly, then they’re not worth it; either they won’t help find defects or you’ll spend too much time maintaining your tests as opposed to developing. [Pragmatic Unit Testing in Java with JUnit](http://www.pragprog.com/titles/utj/pragmatic-unit-testing-in-java-with-junit) suggests 5 properties for good unit tests:

> Good tests have the following properties, which makes them A-TRIP:
> 
> *   **A**utomatic
> *   **T**horough
> *   **R**epeatable
> *   **I**ndependant
> *   **P**rofessional

Automatic
---------

This is where the JUnit framework comes in; if you have to do more than click one button to run _all_ your unit tests, _you’re doing it wrong._ In an ideal world, you wouldn’t even click that button; the code would automatically be compiled and the tests run at regular intervals; any failed tests would result in developer notification.

You don’t have access to the technology necessary for that at ENCS though, but you can still write Test Suites.

A Test Suite is like a collection of Test Cases you run at the same time. In JUnit, any class can be used as a test suite, so long as it has a method `public static Test suite()`:

    import junit.framework.Test;
    import junit.framework.TestSuite;
    	
    public class MyTests {
    	
    	public static Test suite() {
    		TestSuite suite = new TestSuite("Test for default package");
    		suite.addTestSuite(MyTestCase1.class);
    		suite.addTestSuite(MyTestCase2.class);
    		return suite;
    	}
    	
    }

The attentive student will note that there is both the Test Suite and the `junit.framework.TestSuite`.

In Eclipse, you will be able to run this class as a JUnit Test, and JUnit will then execute all the Test Cases and Test Suits you added.

Try to always have one suite which can be used to execute _all_ tests.

Thorough
--------

Good tests test as much as is possible; the more you test the more defects you might find. How much your tests test is described as _coverage_ and coverage can be broken down into three dimensions:

*   **Code coverage**: Are all execution paths and methods tested? While it’s hard to determine if all code paths are executed, you absolutely must have at least one test for every (`public`) method. (Whether you need tests for non-`public` methods is debated.)
*   **Scenario coverage**: Are all possible situations covered? This is where CORRECT boundary conditions become important.
*   **Specification coverage**: Are all the requirements covered? If your requirements are good, they’ll all have clearly defined pass criterion, which you can test.

In the future (when you’re working professionally as opposed to studying) tools will be available which help you determine how much coverage you’ve achieved.

Repeatable
----------

Your Unit Tests should not require modification every time they run. For example:

**The following is a fail:**

    public void testTime() {
    	long expected = 1284345035933;
    	long actual = MyClock.getCurrentDateAndTime();
    	assertEquals("Clock time didn't match expected time", expected, actual);
    }

… is a bad test, as the expected time tends to change. (duh!) A more appropriate example of an unrepeatable test though is the following:

**The following is a fail:**

    public void testDelete() {
    	Item i = Mapper.find(100)
    	i.delete();
    	
    	i = Mapper.find(100)
    	assertNull("Item with id 100 should be deleted", i);
    }

This is a bad test because I can’t run it again without changing it (as item with id will be deleted). _This doesn’t mean you can’t test this delete() method._ It just means it’s _harder_ to test; in a situation like this you should use a mock object to remove the persistent storage… but that’s a more advanced subject.

Independent
-----------

To say tests should be independent is to say they should be small. _Don’t test everything all at once._ Test only one method. If you have several methods which equate to one feature which needs testing, make sure you also test those methods separately. Either way _never_ write tests like this:

**The following is a fail:**

    public void testTooMuchAtOnce() {
    	BankAccount acct = new BankAccount(819415);
    	acct.withdraw(200);
    	acct.deposit(20);
    	acct.transferToCreditCard(500);
    	int balance = acct.getBalance();
    	
    	assertEquals("Account balance was not the expected balance", 31415925654, balance);
    }

The problem here is that too much is happening at the same time and there is no way to determine exactly which method is the source of the defect. If you have to write a test like this one make sure you include sufficient JUnit asserts:

    public void testTooMuchAtOnce() {
    	BankAccount acct = new BankAccount(819415);
    	int balance = acct.getBalance();
    	assertEquals("Account balance was not the expected balance", 9876543210123457469, balance);
    	
    	acct.withdraw(200);
    	balance = acct.getBalance();
    	assertEquals("Account balance was not the expected balance", 9876543210123457269, balance);
    	
    	acct.deposit(20);
    	balance = acct.getBalance();
    	assertEquals("Account balance was not the expected balance", 9876543210123457289, balance);
    	
    	acct.transferToCreditCard(500);
    	balance = acct.getBalance();
    	assertEquals("Account balance was not the expected balance", 9876543210123456789, balance);
    }

Professional
------------

Don’t write stupid tests. Tests have to be written with the same professionalism you practice when developing. For example, avoid redundant code and don’t copy-paste the same code from one test method to the next; use the JUnit `setUp` and `tearDown` methods instead.

Only write tests for relevant, non-trivial code; you’re not writing tests just for the sake of writing tests, but you need them as a means by which to find defects. For example, don’t waste your time writing unit tests for trivial methods such as Getters and Setters; your other tests will be using those anyways (unless you application design sucks) and if they’re broken _you should notice very quickly_.
