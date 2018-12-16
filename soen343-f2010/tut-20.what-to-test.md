What To Test
============

It’s one thing to write classes which extend `TestCase` but it’s another to write quality unit tests. Unit tests have a purpose; _to find software defects as early in the development life cycle as possible_.

How do you write tests to find defects though? Chances are if there’s a defect, it’s because of something you didn’t think of or don’t know; therefore how will you know to write a Unit Test which finds that defect?

What to Test: The Right-BICEP
-----------------------------

The following are 6 specific areas to test, as recommended by the authors of [Pragmatic Unit Testing in Java with JUnit](http://www.pragprog.com/titles/utj/pragmatic-unit-testing-in-java-with-junit):

> \[…\] Right-BICEP:
> 
> *   **Right**: Are the results **right**?
> *   **B**: Are all your **boundary** conditions CORRECT?
> *   **I**: Can you check the **inverse** relationship?
> *   **C**: Can you **cross-check** results using other means?
> *   **E**: Can you force **error conditions** to happen?
> *   **P**: Are **performance** characteristics within bounds?

We’re now going to return to the `TestCase` which tested class `RightAngleTriangle`,written in the tutorial on Writing Unit Tests With JUnit. We’re going to try and make it a better quality `TestCase` by using the Right-BICEP.

### Are the results **right**?

This is the most straightforward way to test: call a method and compare the expected (often hardcoded) results with the actual results. This is what we did in the tutorial on Writing Unit Tests With JUnit when we tested class `RightAngleTriangle` when we tested:

    	// Test area: Are the results RIGHT?
    	public void testGetHypotenuse() {
    		RightAngleTriangle triangle = new RightAngleTriangle(1, 1);
    		double expected = 1.4142135623730951;
    		double actual = triangle.getHypotenuse();
    		assertEquals("Hypotenuse should be root 2", expected, actual);
    	}

Alternately, you could use a data file which contains the inputs and expecetd outputs, but reading the file results in added complexity for your tests, risking bugs in the tests themselves. _You want your unit tests to be simple enough that there is minimal risk of bugs in the defects_.

When looking for "Are the results right?" tests to write, look to the requirements or system specification; good requirements will be a good source of tests.

### Are all your **boundary** conditions CORRECT?

This one is a biggie, because there are a lot of places where you can find boundary conditions. Looking at the `testGetHypotenuse` test alone…

*   What if we pass negative values to the constructor of `RightAngleTriangle`?
*   What if we pass zeros to the constructor of `RightAngleTriangle`?
*   What if we pass `Integer.MAX_VALUE` to the constructor of `RightAngleTriangle`?

The acronym CORRECT is used to help look for boundary conditions:

*   **C**onformance – What happens when a value doesn’t match expected formatting? Does the method expect something to be formatted as an email address? Does it expect non-negative numbers only?
*   **O**rdering – Are there any values (or operations) which are expected in a particular order or lack thereof? What happens when you change that order?(This is important when dealing with arrays and collections)
*   **R**ange – Are there conceivable minimum and maximum values?
*   **R**eference – Does your method have any external dependencies which can affect its state?
*   **E**xistence – What would happen if a value was 0 or `null`? What if the network is down, or a URL returns a 404?
*   **C**ardinality – What happens when thee are too few or too many values?
*   **T**ime – Are there any threading or concurrency concerns?

We’re going to write some quick tests which create a triangle with negative-length catheti, but wait to complete some of them until we reach "Can you force error conditions to happen?"

    	// Test area: Are all your boundary conditions CORRECT? (Conformance)
    	public void testNegativeCatheti() {
    		// more to come…
    		RightAngleTriangle triangle = new RightAngleTriangle(-1, 1);
    		// more to come…
    	}
    	
    	// Test area: Are all your boundary conditions CORRECT? (Range)
    	public void testIntegerMaxCatheti() {
    		/*
    		 *	Be VERY CAREFUL when writing tests involving Integer.MAX_VALUE
    		 *	as your tests could silently overflow and give you an incorrect pass!
    		 */
    		int catheti = 1;
    		RightAngleTriangle triangle = new RightAngleTriangle(catheti, catheti);
    		double hypotenuse = triangle.getHypotenuse();
    		/*
    		 * We can't cross-reference with the expected value, as the expected value is
    		 * out of the range of the int type, so instead we check against the mathematical reality that
    		 * the hypotenuse of a right angle triangle is never shorter than its other legs 
    		 */
    		assertTrue("Hypotenuse " + hypotenuse + "should not be shorted than catheti " + catheti, catheti<hypotenuse);
    	}
    	
    	// Test area: Are all your boundary conditions CORRECT? (Existence)
    	public void testIntegerMaxCatheti() {
    		// ...
    		RightAngleTriangle triangle = new RightAngleTriangle(Double.NaN, Double.NaN);
    		// ...
    	}

### Can you check the **inverse** relationship?

When testing if the results are right, can you double check my performing the inverse relationship? We can do this when testing angles in class `RightAngleTriangle`:

    	// Test area: Are the results right?
    	// Test area: Can you check the inverse relationship?
    	public void testGetFirstAngleInverseRelationship() {
    		RightAngleTriangle triangle = new RightAngleTriangle(5, 6);
    		
    		double oppositeCathetiExpected = 5;
    		double oppositeCathetiActual = Math.tan(triangle.getFirstAngle()) * 6;
    		
    		assertEquals("Actual opposite catheti " + oppositeCathetiActual + " was inconsistent with expected opposite catheti " + oppositeCathetiExpected, oppositeCathetiExpected, oppositeCathetiActual);
    		
    		double adjacentCathetiExpected = 6;
    		double adjacentCathetiActual = Math.tan(triangle.getFirstAngle()) * 5;
    		
    		assertEquals("Actual adjacent catheti " + adjacentCathetiActual + " was inconsistent with expected adjacent catheti " + adjacentCathetiExpected, adjacentCathetiExpected, adjacentCathetiActual);
    	}

We use our high-school trig to determine if we can inversely calculate the expected length of the catheti based on the angle given by `getFirstAngle()` method.

### Can you **cross-check** results using other means?

Is there some common functionality which has a similar function to yours? Can you use it to check the validity of your results? For example, we could change the `testGetHypotenuse()` method to cross-check the expected result with `Math.sqrt()` instead of a hard-coded value:

    	// Test area: Are the results RIGHT?
    	// Test area: Can you cross-check results using other means?
    	public void testGetHypotenuse() {
    		RightAngleTriangle triangle = new RightAngleTriangle(1, 1);
    		double expected = Math.sqrt(2);
    		double actual = triangle.getHypotenuse();
    		assertEquals("Hypotenuse should be root 2", expected, actual);
    	}

We could also cross check the angles with the lemma that all angles in a triangle add up to 180:

    	// Test area: Are the results RIGHT?
    	// Test area: Can you cross-check results using other means?
    	public void testGetHypotenuse() {
    		RightAngleTriangle triangle = new RightAngleTriangle(1, 1);
    		double expected = Math.sqrt(2);
    		double firstAngle = triangle.getFirstAngle();
    		double secondAngle = triangle.getSecondAngle();
    		
    		double expected = 180;
    		double actual = firstAngle + secondAngle + 90;
    		assertEquals("Angles should add up to 180", expected, actual);
    	}

### Can you force **error conditions** to happen?

Don’t assume everything will be sunshine and lollipops for the class under test; test how it behaves when errors occur. Force errors and make sure that the appropriate exceptions are thrown:

    	// Test area: Are all your boundary conditions CORRECT?
    	// Test area: Can you force error conditions to happen?
    	public void testNegativeCatheti() {
    		try {
    			RightAngleTriangle triangle = new RightAngleTriangle(-1, 1);
    			fail();
    		}
    		catch(ImpossibleTriangleException e) {
    			assertTrue(true);
    		}
    	}

Another area worth testing is whether exceptions cause an object to get into a bad state: for example, if we call a setter with an invalid value, does it affect the behavior of the object in the future?

    	// Test area: Are all your boundary conditions CORRECT?
    	// Test area: Can you force error conditions to happen?
    	public void testNegativeCatheti() {
    		RightAngleTriangle triangle = new RightAngleTriangle(1, 1);
    		double expected = 1.4142135623730951;
    		double actual = triangle.getHypotenuse();
    		assertEquals("Hypotenuse should be root 2", expected, actual);
    		
    		try {
    			triangle.setHypotenuse(-1);
    			fail();
    		}
    		catch(ImpossibleTriangleException e) {
    			assertTrue(true);
    		}
    		
    		// Given that setHypotenuse(…) failed, getHypotenuse() should still return root 2
    		actual = triangle.getHypotenuse();
    		assertEquals("Hypotenuse should be root 2", expected, actual);
    	}

### Are **performance** characteristics within bounds?

This isn’t a huge deal at this point in your technical formation, but know that you need to test concurrency issues; especially if you get into TomCat and web development on the Java Platform.
