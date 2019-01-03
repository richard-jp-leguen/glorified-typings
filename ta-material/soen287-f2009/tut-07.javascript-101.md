JavaScript 101
==============

We’re now going to look at client side scripting with ECMAscript, usually just referred to as Javascript. (in reality Javascript is merely one implementation of ECMAscript, but noone seems to care about the distinction)

This tutorial will be a very brief and to the point to just get you on your feet.

What Is Javascript?
-------------------

Javascript is a client-side scripting language, which runs in the browser: once the browser downloads an HTML file, it finds any `<script>` elements and executes the code therein. It can be used to make your HTML pages dynamic, without having to refresh the page.

Why "Java"-script?
------------------

The name ‘Javascript’ was chosen for marketing purposes to benefit from the rising popularity of Java when Javascript was first being developed. The syntax for writing Java and Javascript is comparable, but that’s where it stops; Javascript has nothing to do with Java.

How Do I Add Javascript To An HTML Document?
--------------------------------------------

You add Javascript using the `<script>` element. Provide an attribute which specifies which ‘type’ of script this is; assign it a value of `text/javascript`:

    <script type='text/javascript'>
    // this is a Javascript comment!
    </script>

You can (and usually should) put javascript in external files, just like hos you can put style rules in an external CSS file and link to it. To use an external javascript file, provide a `src` attribute to your `<script>` tag:

    <script type='text/javascript' src='MyFile.js'></script>

Note that the conventional file extension for a Javascript file is `.js`.

For now we’re not going to think about the browser; we’re going to use a Javascript console to familiarize ourselves with Javascript a little more independantly of HTML documents and web development.

Firebug and the Google Code Playground
--------------------------------------

Since Javascript executes as part of an HTML document, it’s hard to "see" and hard to debug. So we’re going to use a Javascript console to play with Javascript for a while before we start relating it to HTML documents, let alone web development.

The most popular Javascript console comes with a Firefox extension called [Firebug](http://getfirebug.com) and it is hopefully installed on the Concordia machines.

If not, you can also use the [Google Code Playground](http://code.google.com/apis/ajax/playground/#conditional_assignment). During the in-lab tutorial for this Javascript 101, I will explain how to use FireBug, but in these written tutorials I will assume you are using the Google Code Playground, in case you don’t have FireBug installed at home (or don’t even use Firefox).

Take note that while the Google Playground is good for your first scripts, as you try and write more complex scripts it will no longer suit you.

### The Google Code Playground

Navigate to [Google Code Playground](http://code.google.com/apis/ajax/playground/#conditional_assignment). You will see three panels:

*   Pick Sample (ingore this one)
*   Edit Code
*   Output

In the ‘Edit Code’ panel you can see some intermediate Javascript, and you can edit it if you want. Lastly, the ‘Output’ panel has two rather self-explanatory buttons, ‘Debug Code’ and ‘Run Code’.

Writing Javascript Code
-----------------------

### Basic Output – Hello World

Now that we have an environment to work in, we’re going to write some Javascript! Try the following in the the [Google Code Playground](http://code.google.com/apis/ajax/playground/#conditional_assignment):

    alert("Hello Popup!");
    document.writeln("Hello Plain Text! ");
    document.writeln("<strong>Hello HTML markup!</strong>");
    document.writeln("<div style='background:yellow;'>Hello stylized HTML markup!</div>");
    document.writeln("<!-- Hello HTML comments! -->");

You should see a popup dialog, and some output written to the Output panel, but maybe not what you expected.

Here are some important things to take from your first dabble in Javascript:

*   The `alert()` function alerts the user with a little popup window.
*   You can use the `document` object the same way you use `System.out` in Java to produce output.
*   The `document.write()` and `document.writeln()` methods write to the HTML document, and can include HTML markup.

### Variables

In Javascript, variables are declared using the `var` keyword. Try it with the following Javascript code:

    var myVar = 0;
    while(myVar<10) {
    	myVar++;
    	alert("Annoying popups! "+myVar+" of 10");
    }
    myVar = new String("The script is done executing");
    document.write(myVar);

You may have noticed that we re-assign variable `i` from an integer value to a String Object. Javascript, unlike Java, is dynamically typed, so any variable can be of any type at runtime.

### Control Flow and Arrays

Javascript grants you access to all the normal control flow constructs that you are used to: if-else, while loops, for loops…

    if(confirm("Do you like pie?")) {
    	document.writeln("<p>You like pie!</p>");
    }
    else {
    	document.writeln("<p>You don't like pie!!</p>");
    	while(!confirm("Do you like it now?")) {
    		document.writeln("<p>I will keep nagging you until you cave!</p>");
    	}
    }
    	
    var pies = new Array("Apple", "Pecan", "Lemon", "Strawberry-Ruhbarb");
    document.writeln("<p>These are my favorite pies:<ul>");
    for(var i=0; i<pies.length; i++) {
    	document.writeln("<li>"+pies[i]+"</li>");
    }
    document.writeln("</ul>");

Here we also see arrays in Javascript. In Javascript array elements don’t need to be of a particular type, and the array need not have a declared size:

    var myArr = new Array();
    myArr[0] = "Index 0";
    myArr[2] = new Date();
    myArr[50] = 10;

### Functions

You can define functions in Javascript using the `function` keyword:

    function HelloWorld() {
    	alert("Hello World!");
    }

Like in other laguages, you can include parameters for a function, and return a value:

    function invertString(stringInput) {
    	var outputString = "";
    	for(var i=stringInput.length-1; i>=0; i--) {
    		outputString += inputString.charAt(i);
    	}
    	return outputString;
    }
    	
    document.writeln(invertString("Race Car"));

Putting the Scripts in an HTML Document
---------------------------------------

Try putting the scripts into an HTML document, like so:

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    	"http://www.w3.org/TR/html4/loose.dtd">
    <html>
    <head><!-- ... --></head>
    <body>
    <h1>My First Javascript Enhanced HTML Document!</h1>
    <script type='text/javascript'>
    	alert("Hello Popup!");
    	document.writeln("Hello Plain Text! ");
    	document.writeln("<strong>Hello HTML markup!</strong>");
    	document.writeln("<div style='background:yellow;'>Hello stylized HTML markup!</div>");
    	document.writeln("<!-- Hello HTML comments! -->");
    </script>
    </body>
    </html>

Save the above in an HTML document, and give it a `.html` extension. Open the file with Firefox (or any other web browser) and you should be able to see that the script executes as soon as you open the file, and its output appears in the rendered document.

Objects in Javascript
---------------------

At this point we will not see how to create our own custom objects in Javascript, but we’re going to look at a built in Javascript object, just to see how to manipulate Javascript objects.

### The Date Object

One of the most popular Javascript objects, the `Date` object is used to represent and manipulate date/time information. It has several constructors:

    var today = new Date();
    var bDay = new Date(1986, 02, 16);
    var firstDayOfClasses = new Date("Tuesday, September 8, 2009");
    var timeStamp = new Date(1234567890000);

You can also use getters/setters on a `Date` object to change the date:

    var myDate = new Date();
    document.write("<ul>");
    for(var i=0; i<365; i++) {
    	document.write("<li>");
    	document.write(myDate.toString());
    	document.write(" or ");
    	document.write(myDate.getDate()+"/"
    			+(myDate.getMonth()+1)+"/"
    			+myDate.getFullYear());
    	document.write("</li>");
    	myDate.setDate(myDate.getDate()+1);
    }
    document.write("</ul>");

### The Array Object

We’ve already seen the Array object briefly above. An alternative syntax for creating an array is using literal syntax with square braces `[]` like so:

    	var fellowship = ["Frodo", "Sam", "Merry", "Pippin", "Gandalf",
    				"Aragorn", "Legolas", "Gimli", "Boromir"];
    	var dwarves = [	"Thorin",
    			"Dwalin",
    			"Balin",
    			"Kili",
    			"Fili",
    			"Dori",
    			"Nori",
    			"Ori",
    			"Oin",
    			"Gloin",
    			"Bifur",
    			"Bofur",
    			"Bombur" ];

The `Array` object has a property (like an instance variable) called `length`, just like in Java:

    alert("Array 'dwarves' is of length "+dwarves.length);

Since Javascript is dynamically typed, you can easily create multi-dimensional arrays:

    var matrix = [[11, 21, 31], [12, 22, 32], [13, 23, 33]];
    document.writeln("<table>");
    for(var i=0; i<matrix.length; i++) {
    	document.writeln("<tr>");
    	for(var j=0; j<matrix[i].length; j++) {
    		document.writeln("<td>"+matrix[i][j]+"</td>");
    	}
    	document.writeln("</tr>");
    }
    document.writeln("</table>");

You can also push/pop and shift/unshift items on and off your array:

    var stack = new Array();
    stack.push("One");
    stack.push("Two");
    stack.push("Three");
    document.writeln(stack.pop()+", "); // Three
    document.writeln(stack.pop()+", "); // Two
    document.writeln(stack.pop()+", "); // One

### The Math Object

The Javascript object Math is very similar to the Java class of the same name (`java.lang.Math`) and provides methods to perform various mathematical operations.

Unlike other Javascript objects, you don’t instantiate Math objects; you call the methods ‘statically’, just like with `java.lang.Math`:

    var minimum = Math.min(x, y, z);
    var maximum = Math.max(x, y, z);
    var tenToTheTwo = Math.exp(10, 2);
    var random = Math.random();	// random decimal number
    				// between 0 and 1
    var absoluteValue = Math.abs(x);
    alert("PI is ".Math.PI);
    alert("Square Root of 2 is ".Math.SQRT2);
