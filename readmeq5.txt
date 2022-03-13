Q5 - Loops
Programming Exercise
Krusty has difficulties tracking the total number of orders he has taken and have requested that the software tracks this. Write a program to allow Krusty to repeatedly take in new orders until there are no orders left for the session. 

The program must prompt the user if there are new orders. All user inputs are from standard input.

If the user enters N or n, the program must display the total orders taken during the session, see Sample Program Input/Output.

If the user enters Y or y, the program must go through the entire process of greet the customer, show the menu, take orders and display the order summary. The program behavior is the same as Q2 - Inputs, Process, Outputs and Q3 - Functions.

If the user enters any other inputs other than the aforementioned values, the program must repeatedly prompt if there are new orders until a valid input is given by the user.

Important: The auto-grader will only start krusty_loop.py. Ensure that your file name is correct!

Sample Program Input/Output

The user inputs are appended by # and not part of the specification. 

Example 1 

$ python3 krusty_loop.py
​New Order[Y/N]: #n
****************
Total orders: 0
****************
Example 2

$ python3 krusty_loop.py
New Order[Y/N]: #y
Welcome to Krusty Burgers!
Krusty Burger                                    $ 5.10
Milkshake                                        $ 3.50
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $10.50

Enter order for Krusty Burger: #1
Enter order for Milkshake: #1
Enter order for Krusty Meal Set[Burger + Drink + Krusty Laugh]: #2

Order Summary
Krusty Burger                                    $  5.10 x  1
Milkshake                                        $  3.50 x  1
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $ 10.50 x  2
Sub-total                                        $ 29.60
GST                                              $  1.48
Total                                            $ 31.08

New Order[Y/N]: #Y
Welcome to Krusty Burgers!
Krusty Burger                                    $ 5.10
Milkshake                                        $ 3.50
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $10.50

Enter order for Krusty Burger: #200
Enter order for Milkshake: #100
Enter order for Krusty Meal Set[Burger + Drink + Krusty Laugh]: #50

Order Summary
Krusty Burger                                    $  5.10 x 200
Milkshake                                        $  3.50 x 100
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $ 10.50 x 50
Sub-total                                        $1895.00
GST                                              $ 94.75
Total                                            $1989.75

New Order[Y/N]: #AS
New Order[Y/N]: #n
****************
Total Orders: 2
****************
 Expand (42 lines) 
Skills-based Test - Sample Questions 
Describe the main components required for a while loop to work. 

What is an infinite loop? 

There are two types of loops - count-controlled and event-controlled. Explain the difference between both types and state the type of loop that is present in your program.