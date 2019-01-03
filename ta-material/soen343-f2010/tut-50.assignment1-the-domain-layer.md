Assignment #1 Preparation: The Domain Layer
===========================================

In this tutorial we’re going to write a tool with observable parallels to the first assignment.

The Tool
--------

> You are in charge of developing a Student Manager system that will help users manage  
> the Students and the grades they are given. It will allow a professor or a tutor to assign students a letter grade.
> 
> All students have a students ID, which never changes. There is also a distinction between two types of students: normal students and students who complain. Students who complain expect certain grades; when they are assigned grades other than those they expect, an external system should be notified to create an appointment during office hours.
> 
> A professor or tutor should be able to view all students, change their grades and add students.

The Domain Model
----------------

First thing we’ll want to do is draw up a domain model:

![Domain Model])assets/tut-51.domain-model.1.jpg)

Note that – even as early as our Domain Model – we have taken the first step towards applying the [Polymorphism GRASP Pattern](http://en.wikipedia.org/wiki/GRASP_%28object-oriented_design%29#Polymorphism): since the behavior of students varies by type, we have different types of students to which responsibility for the behavior will be given.

We can’t say we’ve _already_ applied the polymorphism pattern, because polymorphism is defined by the variation of _behavior_ by type, while a Domain Model contains only attributes, which are data, _not_ behavior. Therefore, we haven’t yet actually applied the Polymorphism pattern.

Class Diagram
-------------

From this you can create a preliminary class diagram:

![Class diagram])assets/tut-51.class-diagram.1.jpg)

### Pattern: Polymorphism

Here we can see the [Polymorphism GRASP Pattern](http://en.wikipedia.org/wiki/GRASP_%28object-oriented_design%29#Polymorphism) in action: a class diagram includes methods, which define the behavior of an object. Classes (or types) `Student` and `StudentWhoComplains` are required to vary in behavior, so they both implement `setGrade(char)`.

Development
-----------

### Write a Test

From here, we can start writing tests. Since this is a TDD approach, that means never writing an untested implementation, which means _even_ writing tests for getters and setters.

Even if we weren’t testing getters and setters, we don’t only have simple getters and setters: since there is more complex logic happening when a `StudentWhoComplains` has their grade changed, `setGrade(char)` is a good place to start writing tests.

    package studentmanager.tests;
    	
    import studentmanager.domain.Student;
    import junit.framework.TestCase;
    	
    public class TestStudent extends TestCase {
    	
    	public void testSetGrade() {
    		Student toddBowden = new Student(555555);
    		char expected = 'A';
    		toddBowden.setGrade(expected);
    		char actual = toddBowden.getGrade();
    		assertEquals(expected, actual);
    	}
    	
    }

### Write Implementation

Implementation is not provided in this tutorial; you should be able to use your Eclipse Quick-Fix light bulbs and the class diagram to write the classes needed.

You should be able to continue with the TDD cycle and write the two classes currently in your class diagram.

More Patterns
-------------

So you’ve written two domain model classes, as per your class diagram. Now what? Can we start writing the UI layer?

No, we’re still missing domain logic. For example, looking at the description of the Student Manager we’ll see:

> be able to view all students

In order to view _all_ students (or more than one) we need some kind of source/collection of students; we need a repository of students, but it’s not in our Domain Model nor our Class Diagram yet.

What should we do? What if we add a `static` list of all students to class `Student` like so?

**The following is a fail:**

![Class diagram])assets/tut-51.class-diagram.1.5.jpg)

While this could work, it’s a bad idea; we’re making class Student less cohesive and less representative of its nature as a domain model entity.

What we need is a repository of students, but we need to justify adding it to the solution when it’s not in the Domain Model, and does not represent a problem domain concept.

### Pattern: Pure Fabrication

A repository is a classic example of the [Pure Fabrication GRASP Pattern](http://en.wikipedia.org/wiki/GRASP_%28object-oriented_design%29#Pure_Fabrication) where we add something to our solution which is not in the Domain Model, so as to support high cohesion and low coupling in our other domain-relevant classes:

![Class diagram])assets/tut-51.class-diagram.2.jpg)

Write a Test
------------

So we’re going to apply the pure fabrication pattern and introduce a Student repository. Write a new test:

    package studentmanager.tests;
    	
    import java.util.Collection;
    	
    import studentmanager.domain.Student;
    import studentmanager.domain.StudentRepository;
    import junit.framework.TestCase;
    	
    public class TestStudentRepository extends TestCase {
    	
    	public void testAllStudents() {
    		StudentRepository tehRepository = new StudentRepository();
    		Collection<Student> allStudents = tehRepository.allStudents();
    		assertTrue(allStudents.isEmpty());
    	}
    }

Write Implementation
--------------------

Again, implementation is not provided in this tutorial; you should be able to use your Eclipse Quick-Fix light bulbs and the class diagram to write the classes needed.

You should be able to continue with the TDD cycle and write both the tests for the rest of class `StudentRepository` as well as its implementation.

One More Pattern
----------------

So you’ve written two domain model classes, and a pure fabrication repository. Now what? Can we start writing the UI layer?

No! We’re still missing our three functionalities:

*   View all students
*   Change their grades
*   Add student(s)

### Pattern: Controller

According to the inside cover of your textbook, [Applying UML and Patterns](http://www.amazon.com/Applying-UML-Patterns-Introduction-Object-Oriented/dp/0130925691), the [GRASP Controller Pattern](http://en.wikipedia.org/wiki/GRASP_%28object-oriented_design%29#Controller) is the first object beyond the UI layer which receives and coordinates a system operation.

The simplest controller simply has one method per system operation, and that is the implementation we’ll go with:

![Class diagram])assets/tut-51.class-diagram.3.jpg)

Write a Test
------------

Testing a controller is tricky:you have to isolate the controller from the rest of the system, which is where mock objects etc come in… but, given our system is fairly small, we can cut corners for now. If we use TomCat in the future, though, expect to have to use mock objects.

    package studentmanager.tests;
    	
    import junit.framework.TestCase;
    import studentmanager.application.StudentMngrController;
    import studentmanager.domain.StudentRepository;
    	
    public class TestController extends TestCase {
    	
    	public void testAddStudent() {
    		StudentRepository tehRepository = new StudentRepository();
    		StudentMngrController controller = new StudentMngrController(tehRepository);
    		
    		int studentID = 123456789;
    		
    		controller.addStudent(studentID);
    		
    		assertNotNull(tehRepository.student(studentID));
    	}
    	
    }

Write Implementation
--------------------

Once you’ve written your Controller class in its entirety, as per the Class Diagram, you’re ready to write some of the swing UI.
