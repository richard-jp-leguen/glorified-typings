Catching Events in JavaScript
=============================

HTML elements have special attributes which you can use to identify Javascript code which should execute on certain events, such as when an element is clicked etc. For example if you want an `alert()` to pop up when someone clicks on some text you can do the following:

    <script type='text/javascript'>
    	function message() {
    		alert("Popup!");
    	}
    </script>
    	
    Click <a onclick="message();">here</a> to see a pop up window.

You may notice that the cursor doesn’t become a pointer finger when you mouse over this `<a>` element. To force this to happen use CSS stylings to apply the `cursor:pointer;` property-value to the anchor.

Other popular events are the `mouseover` and `mouseout` events:

    <img src='http://www.google.ca/intl/en_ca/images/logo.gif'
    	onmouseover="this.src = 'http://www.google.mu/intl/en_com/images/logo_plain.png';"
    	onmouseout="this.src = 'http://www.google.ca/intl/en_ca/images/logo.gif';"
    	 />

Writing a Javascript Calculator
-------------------------------

We’re going to use some HTML input elements to create a simple Javascript calculator. The user will be able to hit buttons corresponding to numbers and simple mathematical operations (+-x/) and we will just use an `alert()` to display the result.

We’re going to take this one step at a time, first writing the HTML, then the CSS, and finally adding the Javascript event handling.

### The HTML

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
    <body>
    <div id="calculator">
     <div id="calculatorOperations">
      <input type='button' value='+' id='additionButton' />
      <input type='button' value='-' id='subtractionButton' />
      <input type='button' value='x' id='multiplicationButton' />
      <input type='button' value='/' id='divisionButton' />
     </div>
     <div id="calculatorNumbers">
      <input type='button' value='9' id='numericButton9' />
      <input type='button' value='8' id='numericButton8' />
      <input type='button' value='7' id='numericButton7' />
      <input type='button' value='6' id='numericButton6' />
      <input type='button' value='5' id='numericButton5' />
      <input type='button' value='4' id='numericButton4' />
      <input type='button' value='3' id='numericButton3' />
      <input type='button' value='2' id='numericButton2' />
      <input type='button' value='1' id='numericButton1' />
      <input type='button' value='0' id='numericButton0' />
     </div>
     <input type='button' value='=' id='evaluateButton' />
    </div>
    </body>
    </html>

### Adding CSS

In terms of appearance, we want to make the calculator look more or less like the numpad on a keyboard, which means a 4 by 4 grid of buttons, with the ’0′ being bigger. In terms of horizontal alignment, we’re also going to center the calculator in the middle of the page. We also want to ensure all the buttons the same size.

To accomplish all this, add the following CSS to your document:

    <style>
    <!--
    #calculator {
    	margin:auto; /*	according to standard,
    			this is how you center a block level element */
    	width:400px;
    }
    body {
    	text-align:center;/*	according to Microsoft IE,
    				you center a block level element
    				with the 'text-align' of its parent */
    }
    input {
    	/*
    	Since all the inputs on our page are buttons,
    	I'm just going to size all input elements 
    	*/
    	width:99px;
    	height:99px;
    }
    #calculatorOperations {
    	width:100px; /* only wide enough for one button */
    	float:right; /*	'float' means positioned to the right,
    			with content wrapping around it. */
    }
    #calculatorNumbers input {
    	float:right; /*	by making them float right, the buttons
    			will be positioned right to left, top to bottom */
    	font-size:12px; /* We'll be playing with this later… */
    	color:black; /* We'll be playing with this later… */
    }
    #calculatorNumbers input#numericButton0 {
    	float:left;
    	width:199px;
    }
    -->
    </style>

#### Javascript Events: `onmouseover` and `onmouseout`

When Javascript was first released it was annoying, and not very useful. It was used for pop-up advertising and cheesy unprofessional animations on a web page.

To every `<input>` element in the HTML document, add the following attributes:

    onmouseover="this.style.fontSize='20px';this.style.color='blue';"
    onmouseout="this.style.fontSize='12px';this.style.color='black;'"

You can actually do the same thing with some more advanced CSS but we’re not going to cover that here.

Congratulations, you have just written your first page using Javascript events. The `onmouseover` and `onmouseout` are actually Javascript events, and their values are javascript code which executes when the cursor passes over or leaves the element.

It’s not advisable to actually put Javascript directly into those attributes. A better idea is to call a method from those attributes, which we’ll do with the following example where we respond to events when the user clicks buttons.

#### Javascript Events: Pushing Buttons

So now we’re going to add a Javascript element to our page. Create a file in the same directory as your HTML calculator, and name it `Calculator.js`, then add the following to the `<head>` of your HTML:

    <script src='Calculator.js' />

In this file, `Calculator.js`, we will define (at least) 6 functions: `pressNumericButton`, `pressAdditionButton`, `pressSubtractionButton`, `pressMultiplicationButton` and `pressDivisionButton`. Once we’ve done that, we’ll change the HTML so out `<input>` buttons call these functions `onclick`.

##### Calculator.js

We’re going to define a few functions in `Calculator.js`:

    var input = 0;
    var calculated = 0;
    function noOperation() {
    	calculated = input;
    	input = 0;
    };
    var operation = noOperation;
    	
    function pressNumericButton(digit) {
    	if(digit>10) {
    		alert("Something is wrong!");	// not valid error handling,
    						// but it will do for now.
    	}
    	input = (input*10)+digit;
    }
    	
    function pressAdditionButton() {
    	
    }
    	
    function pressSubtractionButton() {
    	
    }
    	
    function pressMultiplicationButton() {
    	
    }
    	
    function pressDivisionButton() {
    	
    }
    	
    function pressEvaluateButton() {
    	
    }

Note that since it’s a Javascript file, you don’t need to include `<script>` tags.

We now fill out those fucntions. The logic behind how the calculator works will be simplified: we will discard order of operation (BEDMAS) and just carry out mathematical operations from left to right. So, for example, if a user inputs 1+2 × 5/7 it will be evaluated as ((1+2)x5)/7 instead of respecting mathematical order of operations.

Since this tutorial is about Javascript and not calculators, I have simply filled out the functins below:

    var input = 0;
    var calculated = 0;
    function noOperation() {
    	calculated = input;
    	input = 0;
    };
    var operation = noOperation;
    	
    function pressNumericButton(digit) {
    	if(digit>10) {
    		alert("Something is wrong!");	// not valid error handling,
    						// but it will do for now.
    	}
    	input = (input*10)+digit;
    }
    	
    function pressAdditionButton() {
    	operation();
    	function addition() {
    		alert(calculated+" + "+input);
    		calculated = calculated + input;
    		input = 0;
    	}
    	operation = addition;
    }
    	
    function pressSubtractionButton() {
    	operation();
    	function subtraction() {
    		calculated = calculated – input;
    		input = 0;
    	}
    	operation = subtraction;
    }
    	
    function pressMultiplicationButton() {
    	operation();
    	function multiplication() {
    		calculated = calculated * input;
    		input = 0;
    	}
    	operation = multiplication;
    }
    	
    function pressDivisionButton() {
    	operation();
    	function division() {
    		calculated = calculated + input;
    		input = 0;
    	}
    	operation = division;
    }
    	
    function pressEvaluateButton() {
    	operation();
    	alert(calculated);
    	input = 0;
    	calculated = 0;
    	operation = noOperation;
    }

##### The HTML

We now need to add event handler attributes to our HTML `<input>` elements. While we will see other ways to add event handlers from Javascript later, without modifying the HTML elements, for now we’re going to use the onclick attribute to invoke our event handler:

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
    <head>
    <style>
    <!--
    /* ... */
    -->
    </style>
    <script src='Calculator.js' />
    </head>
    <body>
    <div id="calculator">
     <div id="calculatorOperations">
      <input type='button' value='+'
    	id='additionButton' onclick='pressAdditionButton()' />
      <input type='button' value='-'
    	id='subtractionButton' onclick='pressSubtractionButton()' />
      <input type='button' value='x'
    	id='multiplicationButton' onclick='pressMultiplicationButton()' />
      <input type='button' value='/'
    	id='divisionButton' onclick='pressDivisionButton()' />
     </div>
     <div id="calculatorNumbers">
      <input type='button' value='9'
    	id='numericButton9' onclick='pressNumericButton(9)' />
      <input type='button' value='8'
    	id='numericButton8' onclick='pressNumericButton(8)' />
      <input type='button' value='7'
    	id='numericButton7' onclick='pressNumericButton(7)' />
      <input type='button' value='6'
    	id='numericButton6' onclick='pressNumericButton(6)' />
      <input type='button' value='5'
    	id='numericButton5' onclick='pressNumericButton(5)' />
      <input type='button' value='4'
    	id='numericButton4' onclick='pressNumericButton(4)' />
      <input type='button' value='3'
    	id='numericButton3' onclick='pressNumericButton(3)' />
      <input type='button' value='2'
    	id='numericButton2' onclick='pressNumericButton(2)' />
      <input type='button' value='1'
    	id='numericButton1' onclick='pressNumericButton(1)' />
      <input type='button' value='0'
    	id='numericButton0' onclick='pressNumericButton(0)' />
     </div>
     <input type='button' value='='
    	id='evaluateButton' onclick='pressEvaluateButton()' />
    </div>
    </body>
    </html>

For simplicity and clarity, I have excluded the `onmouseover` and `onmouseout` attributes we added above.

The Problem: `document.write`
-----------------------------

So we can now execute Javascript in response to a user-event. This is good, but what happends when we try the following:

    <script type='text/javascript'>
    	function message() {
    		document.writeln("NOT a popup…");
    	}
    </script>
    	
    Click <a onclick="message();" style="cursor:pointer;">here</a> to see a pop up window.

The entire page’s contents disappear! This is because the `document.write` method can only be executed before the page is finished loading. If you call if again later, the page currently loaded is discarded and the browser acts like it’s loading a new page.

In order to get around this, we have to make use of the [Document Object Model](tut-10.dom.md).
