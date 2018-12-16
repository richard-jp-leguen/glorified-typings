Updating the XHTML Sanitizer
============================

Imagine you are a junior developer working on a large scale [Web Enterprise Application](http://en.wikipedia.org/wiki/Enterprise_software) written using Java Servlets. As a junior developer, you have no design responsibilities; you’ve only been given responsibility over a small existing component: the XHTML Sanitizer.

### The XHTML Sanitizer

In this WebEA, certain end users can submit content – such as comments, forum postings, tutorial material or class slides. However, this content needs to be sanitized before output, or the system would be vulnerable to [Cross Site Scripting Attacks](http://en.wikipedia.org/wiki/Cross-site_scripting). The XHTML Sanitizer removes any content it deems unsafe.

The component was written by another junior developer who has since left the company.

Since times have changes and soon [HTML5](http://www.w3.org/TR/html5/) will be the standard, the business analysts have decided the component should now allow users to leverage new HTML5 elements.

### Test Driven Development and Unit Testing

Since your company practices [Test Driven Development](http://en.wikipedia.org/wiki/Test-driven_development), and is big on unit tests, you will have to write unit tests for **any and all** new functionality you intend to introduce **before** you’ve made your change to the component.

You are also required to run **all** old unit tests to ensure backwards compatibility. If the new code is not backwards compatible, you will be fired.

If you find any bugs which the old unit tests did not catch, you are required to write new Unit Tests for them. If the functionality is un-testable, you may make minor changes to the code, documenting and justifying them.

### The Changes

Note that the point of this activity is **not** to re-develop the component from the ground up; you have to keep your changes to a minimum. **You should be able to do this exercise – in its entirety – by changing only the value of an instance variable and modifying at most one line of code in the XHtmlSanitizer.java file.**

#### HTML5

You have to perform maintenance on the XHTML Sanitizer, and change it so it accommodates the following new HTML5 items: `<section>`, `<article>`, `<aside>`, `<hgroup>`, `<mark>`, `<meter>`, `<time>`, `<wbr>`, and the `<ol>` element’s new `reversed` attribute.

#### Case-Insensitive

Additionally, some of the users have been using Microsoft Word to create their XHTML markup. As a consequence, it is sometimes a mix of UpPeRcAsE AnD lOwErCaSe. You will have to make the sanitizer case insensitive.

#### Software Regression

While your job is only to add the functionality needed, it is essential that no old functionality be lost in the process. If any old functionality is lost, you will also be fired from your junior developer position. See [Regression Testing](http://en.wikipedia.org/wiki/Regression_testing), [Non-Regression Testing](http://en.wikipedia.org/wiki/Non-Regression_testing) and [Software Regression](http://en.wikipedia.org/wiki/Software_regression).

### The Activity

#### Step 1 – Get The Source Code

You can get the source code online from [SOEN343Lab1.tar.gz](assets/SOEN343Lab1.tar.gz).

Create a new Java Project in Eclipse, and then Import the files you downloaded as a File System.

#### Step 2 – Run the Unit Tests

The previous developer wrote a lot of Unit Tests. Run `TestXHtmlSanitizer` and `TestXHtmlBadFormatting` just to familiarize yourself with JUnit a bit.

There are many more Test Cases than just `TestXHtmlSanitizer` and `TestXHtmlBadFormatting` though, and since good unit tests are automatic, you’ll want to write a Test Suite. Be sure to add _all_ Test Cases currently in the project to the Test Suite, and then run it.

##### Create A New Class And Give It Only One Method; `public static Test suite()`

    package soen343.lab1.test;
    	
    import junit.framework.Test;
    import junit.framework.TestSuite;
    	
    public class XHtmlSanitizerTestSuite {
    	
    	public static Test suite() {
    		TestSuite suite = new TestSuite("Test for soen343.lab1.test");
    		// ...
    		return suite;
    	}
    	
    }

##### Add Test Cases to Your Test Suite

Add all the classes you want to run (ie all of them) to the Test Suite using the `TestSuit.addTestSuite(…)` method:

    public static Test suite() {
    	TestSuite suite = new TestSuite("Test for soen343.lab1.test");
    	suite.addTestSuite(TestXHtmlSanitizer.class);
    	suite.addTestSuite(TestXHtmlBadFormatting.class);
    	/* ... */
    	return suite;
    }

Complete the code, adding all Test Cases in the project to the test suite using the `addTestSuite()` method.

Alternately – this is probably what we’ll show you in tutorial for the sake of efficient use of time – you can use the Eclipse menus to create a new Test Suite.

##### Run the Unit Tests

Use `Run As > JUnit Test` to run all the tests in the Test Suite.

#### Step 3 – Prepare new Unit Tests

You’re now going to write a new Unit Test class which will test the changes you intend to make. Until these tests pass, don’t add them to the larger test Suite.

##### Create A New Class Which Extends `junit.framework.TestCase`

Call your new class something like "TestHtml5Elements".

##### Write Test Methods

With JUnit, any method which starts with "test" is used as a test. So create new methods, whose names begin with "test", to test the functionality you are adding to the sanitizer.

For example…

    public void testSectionElement() throws XHtmlBadFormatException {
    	String input = " <section>This is a test</section> ";
    	String expected = " <section>This is a test</section> ";
    	String output = XHtmlSanitizer.sanitize(input);
    	assertEquals("Expected output did not match actual output.", expected, output);
    }
    	
    public void testOlReversedAttribute() throws XHtmlBadFormatException {
    	String input = " <ol reversed=\"reversed\"><li>Reversed list!</li></ol> ";
    	String expected = " <ol reversed=\"reversed\"><li>Reversed list!</li></ol> ";
    	String output = XHtmlSanitizer.sanitize(input);
    	assertEquals("Expected output did not match actual output.", expected, output);
    }

Also write tests to test whether tag names are cAsE sEnSiTiVe.

It should be noted that when practicing true TDD you should only write one test method, and then proceed with implementation necessary to pass that test, before writing another test method. For the purposes of this tutorial, however, it is easier to explain a slightly more waterfall-ish approach.

Run your Unit Tests; they should fail since you haven’t changed the XHtml Sanitizer to accommodate the new features.

#### Step 4 – Make Your Changes to the Code

Since you have tests which are failing, it means you have to make changes to the system.

Looking at the XHTML Sanitizer, you may have noticed an array `String[] whiteList` which looks like it is used for configuration; any `<!ELEMENT >` items in this array allow a new element (tag) to be in the content and `<!ATTLIST >` allows an attribute. Add items to this to accommodate the following new HTML5 tags and attributes:

*   The `<section>` element.
*   The `<article>` element
*   The `<aside>` element
*   The `<hgroup>` element
*   The `<mark>` element
*   The `lt;meter>` element
*   The `<time>` element
*   The `<wbr>` element
*   The ordered list `<ol>` element’s new `reversed` attribute

#### Step 5 – Run All Tests Again.

This time, things should be a little different.

If then original tests fail but some of your new HTML5 tests pass, don’t panic – everything is good. You’re doing fine; the Unit Tests have just helped you uncover a software fault, which has now resulted in errors and into failures. (for an explination of the difference between a "fault", "error" and "failure" see [What is a software fault in testing?](http://stackoverflow.com/questions/494498/what-is-a-software-fault-in-testing) on Stack Overflow)

Since you both have to retain all old functionality while introducing new functionality, you will have to [use the Eclipse Debugging tools](tut-31.debugging-with-eclipse.md) to determine why they are failing and fix any defects causing the problem.
