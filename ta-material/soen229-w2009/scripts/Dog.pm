
{
	package Dog;	# because Perl uses packages as classes.
			# ... and it's disgusting.

	sub new {	# Not all classes will define a new() method.
			# but you'll see them often included.
		my($class) = shift;
		my($name) = shift;
		return bless {"name" => $name}, $class;	# bless takes the first parameter
							# (a reference; take note of the braces { }
							# which mean we're creating a
							# reference to an anonymous hash)
							# and 'blesses' the reference with methods.
	}

	sub getName() {
		my $self = shift;	# There is no 'this' keyword in Perl
					# So when you call a method the instance
					# is the first parameter.
		if(!ref($self)) {
			die("Dog::getName() is an instance method.");
		}
		return $self->{'name'};	# if you look at the new subroutine above,
					# you'll see that a Dog is actually a hash,
					# with methods.
	}
}
1;

