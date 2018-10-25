The Document Object Model
=========================

We’re not going to go in-depth into the Document Object MOdel, we’re going to cover the basics.

The Document Object Model (DOM) is an object-oriented, hierarchical view of an HTML document, with objects representing HTML elements. DOM scripting consists of advanced JavaScript that manipulates your HTML document.

JavaScript provides you with methods and objects which represent all the elements in your document. By manipulating these objects you affect your document.

For an example, let’s make a Hello World DOM scripting page. Use the HTML following HTML:

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
    <head>
    <title>Hello World DOM</title>
    <script type="text/javascript" src="HelloDom.js"></script>
    </head>
    <body>
    <div id="HelloDOM">
      Try me: <input type="button" id="TheButton" value="Click!" />
    </div>
    </body>
    </html>

Let’s say that when we click the button we want to add a message to the `HelloDOM`; "Hello World". To do this we need to manipulate the HTML document after it is finished loading in the browser, so we need to use DOM scripting.

More specifically, what we need to do is add a special text element nested inside div with `id="HelloDOM"`; the text between tags is really a special kind of element.

So the steps we’re trying to achieve are:

1.  manipulate the document with JavaScript
2.  get an object which represents the <div> with id ‘HelloDOM’
3.  create a new special text element
4.  add it as a child to the <div> with id ‘HelloDOM’

The `document` Object
---------------------

JavaScript provides you with `document` object, and it’s a predefined variable. Put the following in any HTML file and it should work even though you haven’t initialized `document`:

    <script type="text/javascript">
     alert(document);
    </script>

The `document` object provides you with an means by which to get an object which represents any element in your document: the `getElementById` method.

Try adding the following to the bottom of the above HTML:

    <script type="text/javascript">
     var outputDiv = document.getElementById("HelloDOM");
     alert(outputDiv);
    </script>

Once you have an object which represents an element, you can manipulate all its attributes like instance variables. In the file 1HelloDom.js1 write the following JavaScript:

### JavaScript

    window.onload = function() {	// Since we link to this JavaScript file in the <head>,
    					// The HTML elements it manipulates aren't yet created when it is executed,
    					// so we need to use event handling to catch the onload event
     alert("Executing the window.onload event handler!");
     var outputDiv = document.getElementById("HelloDOM");
     outputDiv.title = "The HlloDOM Example";
     outputDiv.className = "example";	// 'class' is a reserved term in JavaScript,
    					// so to change the class attribute you use the 'className' instance variable
     // manipulating the style attribute
     outputDiv.style.height = "200px";
     outputDiv.style.width = "200px";
     outputDiv.style.float = "right";
     outputDiv.style.backgroundColor = "red";
     outputDiv.style.color = "green";
     outputDiv.style.fontVariant = "small-caps";
    };

You’ll see that when the document loads, you’ll get a popup alert message, and when you click "ok" the `HelloDOM` element’s style will visibly change.

What we want to do, however, is add new content to the element. To do this we need to create a _text node_ which is a special object used in the Document Object Model to represent text in your HTML document.

    var text_node = document.createTextNode("Hello World");

… and we need to then append it as a child to the object outputDiv, which represents the element with `id="calculatorOutput"`

    outputDiv.appendChild(text_node);

If we want to do this when the button is clicked we need to handle the `onclick` event:

### JavaScript

    window.onload = function() {	// Since we link to this JavaScript file in the <head>,
    					// The HTML elements it manipulates aren't yet created when it is executed,
    					// so we need to use event handling to catch the onload event
     document.getElementById("TheButton").onclick = function() {
       var outputDiv = document.getElementById("HelloDOM");
       var text_node = document.createTextNode("Hello World");
       outputDiv.appendChild(text_node);
     }
    };

Using DOM To Read Input
-----------------------

What if we want this to be a little more interactive? What if we want to let someone input their name and get a personalized message?

### HTML

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
    <head>
    <!-- You know the drill… -->
    <script type="text/javascript" src="HelloDom.js"></script>
    </head>
    <body>
    <div id="HelloDOM">
      What's your name?: <input type="text" id="YourName" /> <input type="button" id="TheButton" value="Click!" /><br />
    </div>
    </body>
    </html>

We can use the `document.getElementById` method to get an object representing the input text box, and then read its `value` instance variable to read user input:

### JavaScript

    window.onload = function() {	// Since we link to this JavaScript file in the <head>,
    					// The HTML elements it manipulates aren't yet created when it is executed,
    					// so we need to use event handling to catch the onload event
     document.getElementById("TheButton").onclick = function() {
       var outputDiv = document.getElementById("HelloDOM");
       var name = document.getElementById("YourName").value;
       var text_node = document.createTextNode("Hello "+name+"!");
       outputDiv.appendChild(text_node);
     }
    };

Adding More Than Text
---------------------

What if you wanted to add more than just text?

You can create almost any non-plain-text element using the `document.createElement` method, or the `document.createTextNode` method:

### JavaScript

    window.onload = function() {	// Since we link to this JavaScript file in the <head>,
    					// The HTML elements it manipulates aren't yet created when it is executed,
    					// so we need to use event handling to catch the onload event
     document.getElementById("TheButton").onclick = function() {
       var outputDiv = document.getElementById("HelloDOM");
       var name = document.getElementById("YourName").value;
       var hyperLink = document.createElement("a"); // we create an anchor element
       hyperLink.href = "http://www.google.ca"; // we set its href attribute
       var text_node = document.createTextNode("Hello "+name+"!");
       hyperLink.appendChild(text_node); // Put some text inside it
       outputDiv.appendChild(hyperLink); // and add it as a child of the HelloDOM element
     }
    };

More tutorials on DOM scripting to come…
