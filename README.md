 # Wires Logic Gate Evaluator

 ## Overview
 This project implements a visual and programmatic simulation of digital logic gates using ASCII circuit diagrams.  
 It can:
 - Load a circuit diagram from a `.txt` file.
 - Parse it into a grid.
 - Evaluate the output of the circuit given specific boolean inputs.
 - Support logic gates such as **NOT, AND, OR, NOR, XOR, NAND**.

 The logic circuits are represented in ASCII art form and stored in the `circuits/` directory.

 ## Project Structure
 ```
 wires_question/
 │
 ├── circuits/               # ASCII diagrams for logic gates
 │   ├── and.txt
 │   ├── nand.txt
 │   ├── nor.txt
 │   ├── not.txt
 │   ├── or.txt
 │   └── xor.txt
 │
 ├── wires.py                 # Main logic for parsing and evaluating circuits
 └── tests.py                 # Unit tests for circuit evaluation
 ```

 ## Requirements
 - Python 3.7+
 - No additional external libraries required (uses only standard Python libraries)

 ## Running the Code

 ### 1. Evaluate a Logic Gate Manually
 You can use `evaluate_function` from `wires.py` to test a specific circuit:
 ```python
 from wires import get_board, evaluate_function

 board = get_board("and")       # Load AND gate
 output = evaluate_function(board, True, False)
 print(output)  # Expected: False
 ```

 ### 2. Run Unit Tests
 Unit tests are provided in `tests.py` to verify all logic gates:
 ```bash
 cd wires_question
 python3 tests.py
 ```

 The tests cover:
 - **NOT gate** – single input
 - **AND, OR, NOR, XOR, NAND gates** – two inputs

 ## Circuit File Format
 Each `.txt` file in `circuits/` contains an ASCII representation of a logic gate.  
 Special characters:
 - `A`, `B` – Input nodes
 - `G` – Gate representation
 - `X` – Output node
 - `|`, `-` – Wires

 Example (`and.txt`):
 ```
 A---G---X
     |
 B---|
 ```

 ## Author
 Piyush Goenka
