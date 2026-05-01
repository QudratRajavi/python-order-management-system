Built an interactive command-line ordering system in Python focused on one core principle:
never trust user input. Every input point is treated as a potential failure, 
validated before moving forward, and handled with a specific recovery path.

Identified that a single generic error catch masked the real problem. 
So, I created three separate exception classes for three distinct failure types: 
invalid menu item, invalid quantity, and invalid confirmation. 
This made it possible to pinpoint exactly where input broke down and respond precisely. 
Added a general fallback exception at the end of every block to catch anything unexpected, 
ensuring the program never crashes from an unanticipated failure 
and always stays in a controlled, recoverable state.

Recognized that prompting once and moving on was a reliability risk. 
So, I designed a continuous loop that keeps asking the user 
if they want to order anything else after every item,
holding the program in a controlled state until the user explicitly signals they are done, 
then accumulating all quantities and prices accurately before proceeding.

Determined that printing output only to the screen left no audit trail. 
So, I added file output to write a formatted order summary to disk at the end of every session, 
creating a persistent record that survives after the program closes.
