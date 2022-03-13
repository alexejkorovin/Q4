Q4 - Conditionals
Programming Exercise
Krusty wants to award customers who have purchased over $30 of the store's products in a single receipt with a spin on the reward wheel. 

Implement a function called spin_promotion that returns a formatted string indicating the total reward spins earned by the customer. The number of spins awarded must strictly follow the requirements set in the terms and conditions of the promotion.  If no reward spins are awarded, the number of 'Reward Spins' is replaced by a sad emoji. The addition of this function must not affect the original behavior of the program in Q3 - Functions.  

The itemized bill in the Order Summary must be updated to indicate the number of 'Reward Spins' that the customer is entitled to receive, see Sample Program Input/Output.

Promotion - Terms and Conditions

A 'Reward Spin' means ONE physical turn at the wheel of rewards. 

'Reward Spins' are positive integers. 

The promotion is only valid for orders placed in a single order. 

Reward Spins are calculated based on the total, not inclusive of tax. 

All 'Reward Spins' are round down to the closest integer, if a fraction of spin exists. 

Sample Program Input/Output

 The user inputs are appended by # and not part of the specification. 

Example 1

$ python3 krusty.py
Welcome to Krusty Burgers!
Krusty Burger                                    $ 5.10
Milkshake                                        $ 3.50
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $10.50

Enter order for Krusty Burger: #5
Enter order for Milkshake: #0
Enter order for Krusty Meal Set[Burger + Drink + Krusty Laugh]: #0

Order Summary
Krusty Burger                                    $  5.10 x  5
Milkshake                                        $  3.50 x  0
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $ 10.50 x  0
Sub-total                                        $ 25.50
GST                                              $  1.28
Total                                            $ 26.78
Reward Spins                                     :(  
   

Example 2

$ python3 krusty.py
Welcome to Krusty Burgers!
Krusty Burger                                    $ 5.10
Milkshake                                        $ 3.50
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $10.50

Enter order for Krusty Burger: #0
Enter order for Milkshake: #10
Enter order for Krusty Meal Set[Burger + Drink + Krusty Laugh]: #0

Order Summary
Krusty Burger                                    $  5.10 x  0
Milkshake                                        $  3.50 x 10
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $ 10.50 x  0
Sub-total                                        $ 35.00
GST                                              $  1.75
Total                                            $ 36.75
Reward Spins                                           1

Example 3

$ python3 krusty.py
Welcome to Krusty Burgers!
Krusty Burger                                    $ 5.10
Milkshake                                        $ 3.50
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $10.50

Enter order for Krusty Burger: #0
Enter order for Milkshake: #0
Enter order for Krusty Meal Set[Burger + Drink + Krusty Laugh]: #20

Order Summary
Krusty Burger                                    $  5.10 x  0
Milkshake                                        $  3.50 x  0
Krusty Meal Set[Burger + Drink + Krusty Laugh]   $ 10.50 x 20
Sub-total                                        $210.00
GST                                              $ 10.50
Total                                            $220.50
Reward Spins                                           7