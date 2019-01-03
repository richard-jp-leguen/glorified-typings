Assignment #1 Preparation: Java Swing and Test Driven Development
=================================================================

In this tutorial we’re going to continue writing the Student Manager system, a tool with observable parallels to the first assignment, using TDD to develop its presentation layer.

The purpose of this tutorial is to clearly demonstrate that just because you’re using a ready-to-use framework like swing, it does **not** mean you can’t test first.

I feel obliged to cite the book [‘Unit Testing in Java’ by Johannes Link](http://www.amazon.com/Unit-Testing-Java-Engineering-Programming/dp/1558608680) as being very influential in this tutorial.

The Domain Layer
----------------

This tutorial assumes you’ve followed the prior tutorial, and have a Domain Layer (and tests to go along with it) as follows:

![Class diagram](assets/tut-51.class-diagram.3.jpg)

The Presentation Layer: Java Swing
----------------------------------

Now you need a Java swing UI to allow the end user to interface with the Student Manager. Since we’re following TDD, that means we start by writing a test case.

So we’re going to add a class `StudentManagerWindow` to our class diagram; it will extend class `javax.swing.JFrame`.

From this point in the "assignment 1 preparation" tutorials, I’m not going to update the Class Diagram; I’m going to focus on how to test swing classes, and how to write swing applications using TDD.

Implementation
--------------

### Write a Test

So how do you write tests for a `JFrame`?

#### JUnit: `setUp` and `tearDown`

Writing tests for GUIs is more challenging, so before we continue you’ll need to be familiar with JUnit’s `setUp` and `tearDown` methods. If you a Test Case implements these methods, they will be called between every test method. For example, running the following as a JUnit test:

    public class Blarg extends TestCase {
    	
    	public void setUp() {
    		System.out.println("SETUP");
    	}
    	
    	public void testA() {
    		System.out.println("testA");
    	}
    	
    	public void testB() {
    		System.out.println("testB");
    	}
    	
    	public void tearDown() {
    		System.out.println("TEARDOWN");
    	}
    }

Yields the following output:

    SETUP
    testA
    TEARDOWN
    SETUP
    testB
    TEARDOWN

This allows us to write less code in each test method, and reduces the likelihood we’ll make a mistake when writing new test methods.

#### A Basic `JFrame` `TestCase`

Now, using `setUp` and `tearDown`, you are ready to write your first Java swing test:

    package studentmanager.tests;
    	
    import studentmanager.presentation.StudentManagerWindow;
    import junit.framework.TestCase;
    	
    public class TestStudentManagerWindow extends TestCase {
    	
    	StudentManagerWindow window;
    	
    	public void setUp() {
    		window = new StudentManagerWindow();
    		window.setVisible(true);
    	}
    	
    	public void tearDown() {
    		window.dispose();
    	}
    	
    	public void testIsShowing() {
    		assertTrue(window.isShowing());
    	}
    	
    }

### Write Implementation

So you’ve got a test case, and now you need to implement your class `StudentManagerWindow`, which won’t be difficult with those super-nifty Eclipse quick-fix light bulbs! The resulting class should look something like this:

    package studentmanager.presentation;
    		
    import javax.swing.JFrame;
    		
    public class StudentManagerWindow extends JFrame {
    	
    }

### Write a Test – Does the JFrame Display the Students?

We want the `StudentManagerWindow` to include some sort of visual representation of the student repository, and we want it to be visible. In the interest of being able to test that functionality, we have a `javax.swing.JTable`, `students`, declared in class `StudentManagerWindow`, allowing to test it as follows:

    	public void testStudentList() {
    		assertTrue(window.getStudents().isShowing());
    	}

### Write Implementation

So we need to add instance variable `students` of type `javax.swing.JTable` to class `StudentManagerWindow`:

    package studentmanager.presentation;
    	
    import javax.swing.JComponent;
    import javax.swing.JFrame;
    import javax.swing.JTable;
    	
    public class StudentManagerWindow extends JFrame {
    	
    	private JTable students = new JTable();
    	
    	public JComponent getStudents() {
    		return students;
    	}
    	
    }

Now your implementation matches the class diagram, but your test still doesn’t pass. The test is asserting whether students `isShowing()` so we need to add it to our `StudentManagerWindow`. We’ll do this in a constructor:

    package studentmanager.presentation;
    	
    import javax.swing.JFrame;
    import javax.swing.JTable;
    	
    public class StudentManagerWindow extends JFrame {
    	
    	private JTable students = new JTable();
    	
    	public StudentManagerWindow() {
    		this.getContentPane().add(students);
    	}
    	
    	public JComponent getStudents() {
    		return students;
    	}
    	
    }

### Write a Test – Is the "Add Student" Button Showing?

So now we have to write another test. We’re going to test whether or not the widgets necessary to add a student are available in our UI. We can do this by naming our components, and calling `getComponents()`:

A much better idea would be to write a custom `JPanel` class which contains accessors to get the `JButton` and the `JTextField` (see below). When this tutorial was first written the plan was for this named-component method to be mental stepping stone to using `getElementById` calls with HTMLUnit testing – but that idea was scrapped.

    	public void testAddStudentIsShowing() {
    		JPanel addStudentPanel = null;
    		JButton addStudent = null;
    		JTextField newStudentID = null;
    		// the expected names of the components we're looking for
    		String panelName = "add-student";
    		String buttonName = "add-student";
    		String textFieldName = "add-student:new-student-id";
    		// loop over the components in our JFrame,
    		// try to find the JTextField which accepts the new student's ID
    		// and the button to click to create the new student
    		for(Component outter:window.getContentPane().getComponents()) {
    			if(outter instanceof JPanel && panelName.equals(outter.getName())) {
    				addStudentPanel = (JPanel)outter;
    				for(Component inner:addStudentPanel.getComponents()) {
    					if(inner instanceof JButton && buttonName.equals(inner.getName())) {
    						addStudent = (JButton)inner;
    					}
    					else if(inner instanceof JTextField && textFieldName.equals(inner.getName())) {
    						newStudentID = (JTextField)inner;
    					}
    				}
    				break;
    			}
    		}
    		// assert that we found those components
    		assertNotNull(addStudentPanel);
    		assertTrue(addStudentPanel.isShowing());
    		assertNotNull(addStudent);
    		assertTrue(addStudent.isShowing());
    		assertNotNull(newStudentID);
    		assertTrue(newStudentID.isShowing());
    	}

An _even better_ idea than using `Component.getName()` would be to write a custom `JPanel` class which contains accessors to get the `JButton` and the `JTextField`:

    	public void testAddStudentIsShowing() {
    		AddStudentPanel addStudentPanel = null;
    		JButton addStudent = null;
    		JTextField newStudentID = null;
    		// the expected names of the components we're looking for
    		String panelName = "add-student";
    		String buttonName = "add-student";
    		String textFieldName = "add-student:new-student-id";
    		// loop over the components in our JFrame,
    		// try to find the JTextField which accepts the new student's ID
    		// and the button to click to create the new student
    		for(Component c:window.getContentPane().getComponents()) {
    			if(c instanceof AddStudentPanel) {
    				assertTrue(c instanceof JPanel);
    				addStudentPanel = c;
    				addStudent = c.getAddStudentButton();
    				newStudentID = c.getStudentIdTextField();
    			}
    		}
    		// assert that we found those components
    		assertNotNull(addStudentPanel);
    		assertTrue(addStudentPanel.isShowing());
    		assertNotNull(addStudent);
    		assertTrue(addStudent.isShowing());
    		assertNotNull(newStudentID);
    		assertTrue(newStudentID.isShowing());
    	}

… but I’m going to stick with the first implementation, which uses `getName()`, though you should strongly consider writing your own `JPanel`.

### Write Implementation

In order to pass this test, our `StudentManagerWindow` has to contain a `JPanel` with a name of "add-student", which in turn must contain a `JButton` and a `JTextField` with names "add-student" and "add-student:student-id", respectively.

    	public StudentManagerWindow() {
    		this.getContentPane().add(students);
    		final JPanel addStudentPanel = new JPanel();
    		final JButton addStudent = new JButton("add student");
    		final JTextField addStudentID = new JTextField(7);
    		addStudentPanel.setName("add-student");
    		addStudent.setName("add-student");
    		addStudentPanel.add(addStudent);
    		addStudentID.setName("add-student:new-student-id");
    		addStudentPanel.add(addStudentID);
    		this.getContentPane().add(addStudentPanel);
    	}

### Write a Test – Does our `JTable` Display a List of Students?

Now we want to test that our `JTable` is hooked up to our `StudentRepository`. In order to do this, we’re going to write a custom implementation of class `javax.swing.table.AbstractTableModel`… but first, we write our test.

    	public void testTableDataComesFromStudentRepository() {
    		assertTrue(window.getStudents().getModel() instanceof StudentManagerTableModel);
    	}

I’m going to breeze over this quick, but if you want to read more about `JTable` and `TableModel`, see [‘How to Use Tables’ on oracle.com](http://download.oracle.com/javase/tutorial/uiswing/components/table.html).

### Write Implementation

    package studentmanager.presentation;
    	
    import javax.swing.table.AbstractTableModel;
    import studentmanager.domain.StudentRepository;
    	
    public class StudentManagerTableModel extends  AbstractTableModel {
    	
    	private StudentRepository repository;
    	
    	public StudentManagerTableModel(StudentRepository repository) {
    		this.repository = repository;
    	}
    		
    }

Once you’ve written your custom `StudentManagerTableModel`, you will also have to call `setModel` on your `JTable` in `StudentManagerWindow`:

    	private StudentRepository repository = new StudentRepository();
    	// ..
    	public StudentManagerWindow() {
    		StudentManagerTableModel tableModel = new StudentManagerTableModel(repository);
    		students.setModel(tableModel);
    		// ...
    	}

### Write a Test – Is The `StudentManagerTableModel` Connected to the Repository?

So we have a custom table model… but it still doesn’t actually display students! (for the sake of brevity, I’m including 2 tests in this step…)

    	public void testColumnNames() {
    		StudentRepository tehRepository = new StudentRepository();
    		StudentManagerTableModel tableModel = new StudentManagerTableModel(tehRepository);
    		int expectedColCount = 2;
    		assertEquals(tableModel.getColumnCount(), expectedColCount);
    		String expectedCol0 = "Student ID";
    		assertEquals(expectedCol0, tableModel.getColumnName(0));
    		String expectedCol1 = "Grade";
    		assertEquals(expectedCol1, tableModel.getColumnName(1));
    	}
    	
    	public void testRowCount() {
    		StudentRepository tehRepository = new StudentRepository();
    		StudentManagerTableModel tableModel = new StudentManagerTableModel(tehRepository); 
    		assertTrue(tableModel.getRowCount()==0);
    		
    		tehRepository.add(new Student(555555));
    		assertTrue(tableModel.getRowCount()==1);
    		
    		tehRepository.add(new Student(6666666));
    		assertTrue(tableModel.getRowCount()==1);
    	}

### Write Implementation

To pass this test, we need to override some methods of `AbstractTableModel`:

    package studentmanager.presentation;
    	
    import javax.swing.table.AbstractTableModel;
    import studentmanager.domain.Student;
    import studentmanager.domain.StudentRepository;
    	
    public class StudentManagerTableModel extends  AbstractTableModel {
    	
    	private StudentRepository repository;
    	
    	public StudentManagerTableModel(StudentRepository repository) {
    		this.repository = repository;
    	}
    	
    	private String[] columnNames = {"Student ID", "Grade"};
    	
    	public int getColumnCount() { return 2; }
    	
    	public int getRowCount() { return repository.allStudents().size();}
    	
    	public Object getValueAt(int row, int col) {
        		Student[] allStudents = new Student[repository.allStudents().size()];
    	    	if(col==0) {
    	    		repository.allStudents().toArray(allStudents);
    	    		return allStudents[row].getStudentID();
    		}
    		else if(col==1) {
    			repository.allStudents().toArray(allStudents);
        			return allStudents[row].getGrade();
    		}
    		return null;
    	}
    	
    	public String getColumnName(int col) {
    		return columnNames[col];
    	}
    	
    }

### Write a Test – Does the `JTable` Update When "Add Student" Is Clicked?

This is where the big guns come out; we now have to write a test which enters values and clicks on our components.

It should be noted that this test is fairly long; were it not for the fact that breaking it up makes the tutorial less clear, I would break this up into 2 or 3 tests.

    	public class TestStudentManagerWindow extends TestCase {
    	// ...
    	 	public void testAddStudent() {
    			// make sure there are no rows displayed to begin with
    			assertTrue(window.getStudents().getRowCount()==0);
    			JPanel addStudentPanel = null;
    			JButton addStudent = null;
    			JTextField newStudentID = null;
    			// the expected names of the components we're looking for
    			String panelName = "add-student";
    			String buttonName = "add-student";
    			String textFieldName = "add-student:new-student-id";
    			// loop over the components in our JFrame,
    			// try to find the JTextField which accepts the new student's ID
    			// and the button to click to create the new student
    			for(Component outter:window.getContentPane().getComponents()) {
    				if(outter instanceof JPanel && panelName.equals(outter.getName())) {
    					addStudentPanel = (JPanel)outter;
    					for(Component inner:addStudentPanel.getComponents()) {
    						if(inner instanceof JButton && buttonName.equals(inner.getName())) {
    							addStudent = (JButton)inner;
    						}
    						else if(inner instanceof JTextField && textFieldName.equals(inner.getName())) {
    							newStudentID = (JTextField)inner;
    						}
    					}
    					break;
    				}
    			}
    			// assert that we found those components
    			assertNotNull(addStudent);
    			assertNotNull(newStudentID);
    			// input information
    			newStudentID.setText("555555");
    			// and click!
    			addStudent.doClick();
    			// assert that there are more rows in the table than before 
    			assertTrue(window.getStudents().getRowCount()>0);
    		}
    	}

Now we need the text field and the buttons to not only exist, but to update the `JTable` somehow.

In order for this to work we need to:

1.  Somehow connect the `JButton` to `StudentMngrController.addStudent(int)`
2.  Have the `StudentRepository` update/refresh the `JTable`

Write Implementation
--------------------

### Somehow connect the `JButton` to `StudentMngrController.addStudent(int)`

Swing offers us a pretty straightforward way to do this with `ActionListener`:

    	// ...
    	private StudentMngrController controller = new StudentMngrController(repository);
    	// ...
     	public StudentManagerWindow() {
    		this.getContentPane().add(students);
    		final JPanel addStudentPanel = new JPanel();
    		final JButton addStudent = new JButton("add student");
    		final JTextField addStudentID = new JTextField(7);
    		addStudent.addActionListener(new ActionListener() {
    		
    			@Override
    			public void actionPerformed(ActionEvent arg0) {
    				controller.addStudent(Integer.parseInt(addStudentID.getText()));
    			}
    		
    		});
    		addStudentPanel.setName("add-student");
    		addStudent.setName("add-student");
    		addStudentPanel.add(addStudent);
    		addStudentID.setName("add-student:new-student-id");
    		addStudentPanel.add(addStudentID);
    		this.getContentPane().add(addStudentPanel);
    	}

### Have the `StudentRepository` update/refresh the `JTable`

So we need `StudentRepository` – on the low end of our Domain Layer – to update our `JTable` or the `StudentManagerTableModel`, both of which are distinctly in our Presentation Layer, and we don’t want to introduce an upwards dependancy, or any coupling between `StudentRepository` and `javax.swing.*` classes. If the [Gang of Four](http://en.wikipedia.org/wiki/Design_Patterns) authors were here, maybe they’d say that we need to…

> Define a one-to-many dependancy between objects so that when one object changes state, all its dependancies are notified and updated automatically.

Which is the definition of the observer pattern.

### Pattern: Observer

So let’s take a look at Observer: in observer we have 3(ish) participants:

![The Observer Pattern](assets/tut-51.oberserver-uml.jpg)

ul >

*   The Subject, who changes state (in this case, the `StudentRepository`)
*   The Observer, an interface which de-couples the subject from the concrete observer
*   The Concrete Observer, who is notified (in this case the `StudentManagerTableModel`)

I won’t explicitly implement the observer pattern, but I will give a more final-ish Class Diagram:

![The Class Diagram](assets/tut-51.class-diagram.4.jpg)

… and the implementation of `StudentManagerTableModel.update()`:

    	public void update() {	// we can't call if notify(),
    				// notify() is a method of class Object
    		this.fireTableDataChanged();
    	}
