Annex B
Computational Thinking Exercise: "Smart Vending Machine"

Section: 9-Pinatubo Score:____________

C# / Name: 24 - Trisha Mayelle Z. Fos Date: 8/16/26


Scenario

Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

Sometimes the machine does not give the correct change.
Items run out, but the machine doesn't notify anyone.
Students press the wrong buttons and get the wrong item.
The machine is slow when multiple students use it in succession.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem
Main Problem: The vending machine does not always work correctly, causing problems with payments, item selection, item availability, and machine speed.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. The machine gives incorrect change after payment.
2. The machine does not notify students when an item is sold out.
3. Students may press the wrong button and receive the wrong item.
4. The machine becomes slow when multiple students use it at the same time.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

| Sub-problem | CT Skills | Example Solutions |
|------------|-----------|-------------------|
| 1. The machine gives incorrect change after payment. | Algorithms | We can use algorithms to use subtraction for payment. The equation would be *money given - price of item = change*. After this, we can make the machine dispense change using the biggest bill first. |
| 2. The machine does not notify the students when an item is sold out. | Abstraction | We can set up a counter for each item and when one is sold out, it can display an "OUT OF STOCK" sign either on the LCD or beside the price of the item in the vending machine (if there's no LCD.) |
| 3. Students may press the wrong button and receive the wrong item. | Pattern Recognition | We can add a confirmation screen with the picture of the item and the price. |
| 4. The machine slows down when it is used continuously by student after student. | Algorithm (?) | We can add a quick cooldown timer so that the vending machine can fully clear its memory before the next order. |

 Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

assume item = price of what the student wants
              money = how much the student gives 
              change = money-item (amount of change to be given by the machine)

if item is picked:

              if change==0:
                            drop item
                            does not print and drop change
              elif: change>0:
                            drops item
                            prints and drops change
              else: 
                            break
