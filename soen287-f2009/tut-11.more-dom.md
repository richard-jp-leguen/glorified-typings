DOM Scripting
=============

Download [this](assets/MyCalendar.html) HTML file, and style it to include a calendar.

Then create a JavaScript file in which we will put the code we need in order to manipulate the HTML document. We will be writing JavaScript to add an event to the calendar when the user clicks the "Add New Event" button at the bottom of the page.

For starters, since we will be DOM scripting and we are linking our HTML document to the script file in the `<head>` element (before the elements we’ll be manipulating have been created) we need our JavaScript file to define an event handler for the `window.onload` event:

### JavaScript

    window.onload = function() {
    	alert("The window has loaded");
    	// more to come…
    };

Now we’re going to want something to happen when someone pushes the "Add New Event" button. In the HTML, we can see that this button has an ‘id’ attribute of "AddNewEvent":

### HTML

    <input type="button" value="Add New Event!"  id="AddNewEvent" />

… so in our JavaScript, we’re going to use the `document.getElementById` method to obtain an object representing that button, and assign an event handler for its `onclick` event.

### JavaScript

    window.onload = function() {
    	alert("The window has loaded");
    	
    	document.getElementById("AddNewEvent").onclick = function() {
    		alert("You clicked the Add New Event Button!");
    	};
    };

Try putting it all together and open the HTML document in a web browser.

Adding an Event to the Calendar
-------------------------------

In order to add an event to the calendar, we need to determine what time it starts, get the object which represents the `<li>` which represents that time slot, and then add an `<a>` element inside that time slot.

We’re going to only add the Tuesday morning tutorial to the calendar and leave the rest of the form interaction for the assignment…

### JavaScript

    window.onload = function() {
    	alert("The window has loaded");
    	
    	document.getElementById("AddNewEvent").onclick = function() {
    		alert("You clicked the Add New Event Button!");
    	
    		var eventDuration = 100; // in minutes
    		var eventDay = "Tuesday";
    		var eventTime = "10h15";
    		var eventName = "SOEN287 Tutorial Section A";
    		// more to come…
    	};
    };

So first we need to create an object which will represent the `<a>` element which in turn represents the event:

    window.onload = function() {
    	alert("The window has loaded");
    	
    	document.getElementById("AddNewEvent").onclick = function() {
    		alert("You clicked the Add New Event Button!");
    	
    		var eventDuration = 100; // in minutes
    		var eventDay = "Tuesday";
    		var eventTime = "10h15";
    		var eventName = "SOEN287 Tutorial Section A";
    	
    		var newEventElement = document.createElement("a");
    		newEventElement.appendChild(document.createTextNode(eventName));
    								// We immediately add
    								// the text inside that <a> element
    		// more to come…
    	};
    };

… and we now need to append that new `<a>` element as a child to the corresponding `<li>` element. Take note that all `<li>` elements in the document have id attributes.

    window.onload = function() {
    	alert("The window has loaded");
    	
    	document.getElementById("AddNewEvent").onclick = function() {
    		alert("You clicked the Add New Event Button!");
    	
    		var eventDuration = 100; // in minutes
    		var eventDay = "Tuesday";
    		var eventTime = "10h15";
    		var eventName = "SOEN287 Tutorial Section A";
    	
    		var newEventElement = document.createElement("a");
    		newEventElement.appendChild(document.createTextNode(eventName));
    								// We immediately add
    								// the text inside that <a> element
    		var timeSlotId = eventDay+eventTime
    		document.getElementById(timeSlotId).appendChild(newEventElement);
    		// more to come…
    	};
    };

You can now add an event to the calendar! **BUT** it’s not the right duration. In order to control how long it looks in the calendar, we need to style the `<a>` element we’ve created:

    window.onload = function() {
    	alert("The window has loaded");
    	
    	document.getElementById("AddNewEvent").onclick = function() {
    		alert("You clicked the Add New Event Button!");
    	
    		var eventDuration = 100; // in minutes
    		var eventDay = "Tuesday";
    		var eventTime = "10h15";
    		var eventName = "SOEN287 Tutorial Section A";
    	
    		var newEventElement = document.createElement("a");
    		newEventElement.appendChild(document.createTextNode(eventName));
    								// We immediately add
    								// the text inside that <a> element
    		newEventElement.style.height = (eventDuration/15*20)+"px";
    								// Do the math: each time slot is
    								// 15 minutes long and 20px tall
    	
    		var timeSlotId = eventDay+eventTime
    		document.getElementById(timeSlotId).appendChild(newEventElement);
    		// more to come…
    	};
    };

Geting Input From the Drop Down Menus
-------------------------------------

What if we want to add out Tutorial on a day other than Tuesday? We’re now going to allow the user to choose a day to add an event to using the drop down menu `NewEventDay`.

    window.onload = function() {
    	alert("The window has loaded");
    	
    	document.getElementById("AddNewEvent").onclick = function() {
    		alert("You clicked the Add New Event Button!");
    	
    		var eventDuration = 100; // in minutes
    		var eventDay = "Tuesday";
    		var eventTime = "10h15";
    		var eventName = "SOEN287 Tutorial Section A";
    	
    		var newEventElement = document.createElement("a");
    		newEventElement.appendChild(document.createTextNode(eventName));
    								// We immediately add
    								// the text inside that <a> element
    		newEventElement.style.height = (eventDuration/15*20)+"px";
    								// Do the math: each time slot is
    								// 15 minutes long and 20px tall
    	
    		// We now need to read the eventDay from the <select> element with id &uuot;NewEventDay"
    		var newEventDaySelect = document.getElementById("NewEventDay");
    		eventDay = newEventDaySelect.options[newEventDaySelect.selectedIndex].value;
    		alert("Event day is '"+eventDay+"'");
    	
    		var timeSlotId = eventDay+eventTime
    		document.getElementById(timeSlotId).appendChild(newEventElement);
    		// more to come…
    	};
    };
