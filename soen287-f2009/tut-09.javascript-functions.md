JavaScript Functions
====================

We saw functions very briefly in the [last tutorial](tut-07.javascript-101.md), but we didn’t even scratch the surface. The foundation of everything Javascript lies in functions.

Once you have seen a little more on how to write functions in Javascript, we will see how to use them to catch events, allowing your HTML documents to be not only dynamic but interactive.

Functions in Javascript
-----------------------

The most popular ways of creating functions in Javascript are the declaratively, with anonymous functions, and with function literals.

### Declarative Functions

We’ve seen the declarative method of creating functions before:

    function sayHello(){
    	alert("Hello!");
    }
    sayHello();
    	
    function returnZero {
    	return 0;
    }
    document.writeln(returnZero());

### Anonymous Functions

You can also create functions dynamically in Javascript using anonymous functions. Anonymous functions look like other objects, but their constructors take Javascript code as parameters:

    var message = new Function("x", "alert(x)");
    message("Hello!");

The last parameter is the function body, and all parameters before the last declare variables passed into the function.

    var toVector = new Function("i", "j", "k", "return new Array(i, j, k);");

### Function Literals

In Javascript, you can also use what are called _function literals_. In Javascript, functions are objects, so you can assign a variable a function:

    var myFunction = function() {
    	alert("Whoa! Function Literals!!");
    };
    	
    myFunction();

You can also introduce your own function as a member of another object.

    var specialDate = new Date();
    specialDate.toHtmlTable = function() {
    	return	"<table>"+
    		 "<tr><th>Day of Month</th><th>Month</th><th>Year</th></tr>"+
    		 "<tr><td>"+this.getDate()+"</td><td>"+this.getMonth()+"</td><td>"+this.getFullYear()+"</td></tr>"+
    		"</table>";
    }
    	
    document.write(specialDate.toHtmlTable());

Take note that not all instances of Date would have a member function `toHtmlTable`: only the instance which corresponds to variable `specialDate` would have a member function `toHtmlTable`.

### Scope, Encapsulation and Functions

Variables in Javascript are global unless declared using `var` in a code block. Here are some examples which elaborate.


In the following code we see that variable `a` – declared outside of any function or code block – is visible from within a function:

    var a = "Fun with Javascript!";
    	
    function blarg() {
    	alert(a);
    }
    	
    blarg();

However, a variable declared inside a function is not visible from outside the function:

    function blarg() {
    	var a = "Fun with Javascript!";
    }
    	
    blarg();
    alert(a); // Error! a is not defined

If we have two variables with the same name – one local and one global – they will not conflict.

    var a = "Global Var";
    	
    function blarg() {
    	var a = "Fun with Javascript!";
    	alert("From blarg: "+a);
    }
    	
    blarg();
    alert("Outside blarg: "+a);

### Returning and Re-Assigning Functions

Since we can use function literals to assign functions to variables, we can also write functions which return other functions:

    var myFunc = function() {
    	return function() {
    		alert("This is the first time this funtion is called!");
    		myFunc = function() {
    			alert("Someone called myFunc again!");
    		};
    	};
    }
    	
    myFunc()();
    myFunc();
