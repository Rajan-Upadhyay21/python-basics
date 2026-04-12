Python Basics — Core Programming Concepts from the Ground Up

A structured, beginner-to-intermediate Python reference repository covering essential programming constructs, data modeling patterns, and object-oriented design principles — implemented through clean, well-commented, executable code.


Overview
This repository documents a deliberate, ground-up exploration of the Python programming language — from primitive data types and control flow through functions, scope, and the full object-oriented programming paradigm. Every concept is implemented as a focused, self-contained script that prioritizes readability and conceptual clarity over brevity.
Python is the lingua franca of modern software engineering, data science, and artificial intelligence. Mastering its fundamentals is not merely a prerequisite for these fields — it is the foundation upon which every higher-order abstraction, from NumPy array operations to neural network training loops, is ultimately built. This repository treats that foundation with the seriousness it deserves.
Each module in this repository is written with two goals in mind: first, to produce working, executable code that demonstrates the concept in isolation; second, to serve as a durable personal reference that remains useful long after the initial learning phase is complete.

What This Repository Covers
Variables & Data Types

Variable declaration, assignment, and reassignment
Numeric types — int, float, complex — and arithmetic precision
String type — immutability, indexing, slicing, f-string formatting
Boolean type — truthiness, falsy values, and short-circuit evaluation
None type — null representation and identity comparison with is
Dynamic typing and runtime type introspection with type() and isinstance()
Type casting — explicit conversion between int, float, str, and bool
The distinction between mutable and immutable types and why it matters

Basic Operations

Arithmetic operators — +, -, *, /, // (floor division), % (modulo), ** (exponentiation)
Comparison operators — ==, !=, <, >, <=, >=
Logical operators — and, or, not with truth table examples
Assignment operators — +=, -=, *=, /=, //=, **=
Bitwise operators — &, |, ^, ~, <<, >>
Operator precedence and the use of parentheses for explicit control
String operations — concatenation, repetition, membership testing with in

Data Structures

Lists — ordered, mutable sequences; indexing, slicing, appending, inserting, removing, sorting, list comprehensions
Tuples — ordered, immutable sequences; use cases, packing/unpacking, named tuples
Dictionaries — key-value stores; creation, access, update, deletion, iteration, dictionary comprehensions, nested dicts
Sets — unordered collections of unique elements; union, intersection, difference, symmetric difference
Strings as sequences — iteration, membership, built-in string methods (split, join, strip, replace, find, format)
Choosing the right data structure — performance and semantic tradeoffs

Conditions & Control Flow

if, elif, else — branching logic and nested conditionals
Ternary (conditional) expressions — value_if_true if condition else value_if_false
match / case — structural pattern matching (Python 3.10+)
Guard clauses and early returns for reducing nesting depth
Truthiness-based conditions — idiomatic Python boolean checks

Loops & Iteration

for loops — iterating over lists, strings, dictionaries, ranges, and arbitrary iterables
while loops — condition-driven repetition, infinite loop prevention
Loop control — break, continue, pass, and else clauses on loops
range() — start, stop, step patterns for numeric iteration
enumerate() — simultaneous index and value access
zip() — parallel iteration over multiple iterables
reversed() and sorted() — non-destructive iteration patterns
Nested loops — 2D iteration, matrix traversal, early exit strategies
List comprehensions — concise, readable single-line loop-and-filter expressions
Generator expressions — memory-efficient lazy iteration

Functions

Function definition with def — parameters, return values, docstrings
Positional vs. keyword arguments — call-site flexibility
Default parameter values — design considerations and mutable default anti-patterns
*args and **kwargs — variadic functions for flexible interfaces
Scope and the LEGB rule — Local, Enclosing, Global, Built-in resolution order
The global and nonlocal keywords — when and why to use them
Lambda functions — anonymous single-expression callables
Higher-order functions — passing and returning functions, map(), filter(), sorted() with key functions
Recursion — base cases, recursive cases, stack depth, and the factorial/Fibonacci canonical examples
Decorators — function wrappers for cross-cutting concerns like logging and timing
Closures — functions that capture and carry enclosing scope variables

Object-Oriented Programming (OOP)

Classes and instances — the blueprint vs. object distinction
The __init__ constructor — instance initialization and attribute binding
Instance methods and the self parameter — per-object behavior
Class attributes vs. instance attributes — shared vs. per-instance state
@classmethod and @staticmethod — alternative constructors and utility methods
Properties with @property — controlled attribute access with getters and setters
Encapsulation — public, protected (_), and private (__) naming conventions
Inheritance — single inheritance, method overriding, super() delegation
Multiple inheritance and the Method Resolution Order (MRO)
Polymorphism — duck typing and method overriding in practice
Magic (dunder) methods — __str__, __repr__, __len__, __eq__, __lt__, __add__, __iter__
Abstract base classes with abc.ABC — enforcing interface contracts
Composition over inheritance — building flexible object relationships


Tech Stack
ToolPurposePython 3.10+Core language runtimeJupyter NotebookInteractive concept exploration and output visualizationVS Code / PyCharmScript editing with syntax highlighting and debugging
No third-party libraries are required. This repository intentionally uses only Python's standard library to keep the focus on language fundamentals rather than framework specifics.

Repository Structure
bashpython-basics/
├── 01_variables_and_datatypes/
│   ├── variables.py               # Declaration, assignment, dynamic typing, type introspection
│   ├── numeric_types.py           # int, float, complex — arithmetic and precision behavior
│   ├── strings.py                 # Immutability, slicing, f-strings, built-in string methods
│   ├── booleans.py                # Truthiness, falsy values, short-circuit evaluation
│   └── type_casting.py            # Explicit conversion between int, float, str, bool
│
├── 02_basic_operations/
│   ├── arithmetic.py              # All arithmetic operators with precedence examples
│   ├── comparison_logical.py      # Comparison and logical operators, truth tables
│   ├── assignment_operators.py    # Compound assignment — +=, -=, *=, //=, **=
│   └── string_operations.py       # Concatenation, repetition, membership, formatting
│
├── 03_data_structures/
│   ├── lists.py                   # Mutable sequences — CRUD, slicing, comprehensions
│   ├── tuples.py                  # Immutable sequences — packing, unpacking, use cases
│   ├── dictionaries.py            # Key-value stores — access, iteration, comprehensions
│   ├── sets.py                    # Unique collections — set operations and algebra
│   └── data_structure_choice.py   # When to use which structure — performance tradeoffs
│
├── 04_conditions/
│   ├── if_elif_else.py            # Branching logic with nested and chained conditions
│   ├── ternary_expressions.py     # Single-line conditional expressions
│   ├── pattern_matching.py        # match/case structural pattern matching (Python 3.10+)
│   └── guard_clauses.py           # Early return patterns for cleaner branching
│
├── 05_loops/
│   ├── for_loops.py               # Iterating over sequences, ranges, and dicts
│   ├── while_loops.py             # Condition-driven loops, break/continue/pass
│   ├── loop_control.py            # break, continue, pass — behavior and use cases
│   ├── enumerate_zip.py           # Pythonic parallel and indexed iteration
│   ├── comprehensions.py          # List, dict, and set comprehensions
│   └── generators.py              # Generator expressions and lazy evaluation
│
├── 06_functions/
│   ├── basics.py                  # def, parameters, return values, docstrings
│   ├── args_kwargs.py             # *args and **kwargs — variadic function signatures
│   ├── scope_legb.py              # Local, Enclosing, Global, Built-in scope resolution
│   ├── lambda_functions.py        # Anonymous callables with map, filter, sorted
│   ├── higher_order.py            # Functions as arguments and return values
│   ├── recursion.py               # Factorial, Fibonacci, and recursive thinking
│   ├── decorators.py              # Function wrapping — logging, timing, access control
│   └── closures.py                # Capturing enclosing scope — counter and factory patterns
│
├── 07_oop/
│   ├── classes_instances.py       # Class definition, __init__, instance creation
│   ├── instance_class_attrs.py    # Per-object vs. shared state, class variables
│   ├── methods.py                 # Instance, class (@classmethod), and static methods
│   ├── properties.py              # @property — getters, setters, and validation
│   ├── encapsulation.py           # Public, protected, private naming conventions
│   ├── inheritance.py             # Single inheritance, method overriding, super()
│   ├── multiple_inheritance.py    # MRO, diamond problem, mixin patterns
│   ├── polymorphism.py            # Duck typing and behavioral substitution
│   ├── dunder_methods.py          # __str__, __repr__, __eq__, __len__, __iter__, __add__
│   ├── abstract_classes.py        # abc.ABC — enforcing interface contracts
│   └── composition.py             # Building objects from objects — composition vs. inheritance
│
├── notebooks/
│   ├── python_basics_tour.ipynb   # Interactive walkthrough of all core concepts
│   └── oop_deep_dive.ipynb        # Object-oriented patterns with live examples
│
├── exercises/
│   ├── practice_problems.py       # Curated exercises covering all topics
│   └── solutions.py               # Reference solutions with explanations
│
├── requirements.txt               # Standard library only — no external dependencies
└── README.md

Getting Started
Prerequisites

Python 3.10 or higher
No external packages required for core scripts

Installation
bash# Clone the repository
git clone https://github.com/Rajan-Upadhyay21/python-basics.git
cd python-basics

# Verify your Python version
python --version   # Should be 3.10 or higher

# Run any script directly
python 01_variables_and_datatypes/variables.py

# Or launch Jupyter for interactive notebooks
pip install notebook
jupyter notebook notebooks/

Sample Code
Mutable vs. Immutable — A Critical Distinction
python# Strings are immutable — every operation returns a new object
name = "rajan"
upper_name = name.upper()
print(name)         # "rajan"   — original unchanged
print(upper_name)   # "RAJAN"   — new string object

# Lists are mutable — operations modify in place
scores = [85, 92, 78]
scores.append(95)
print(scores)       # [85, 92, 78, 95] — original modified

# This distinction affects how arguments behave inside functions
def add_score(score_list, score):
    score_list.append(score)   # modifies the ORIGINAL list — no copy made

add_score(scores, 100)
print(scores)       # [85, 92, 78, 95, 100]

The LEGB Scope Rule
pythonx = "global"              # Global scope

def outer():
    x = "enclosing"       # Enclosing scope

    def inner():
        x = "local"       # Local scope
        print(x)          # "local" — innermost scope wins

    inner()
    print(x)              # "enclosing"

outer()
print(x)                  # "global"

OOP — Building a Meaningful Class Hierarchy
pythonfrom abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    @abstractmethod
    def speak(self) -> str:
        """Every concrete animal must implement its own sound."""
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', species='{self.species}')"


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name, species="Canis lupus familiaris")
        self.breed = breed

    def speak(self) -> str:
        return f"{self.name} says: Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Meow!"


# Polymorphism — same interface, different behavior
animals = [Dog("Rex", "Labrador"), Cat("Whiskers", "Felis catus")]
for animal in animals:
    print(animal.speak())
# Rex says: Woof!
# Whiskers says: Meow!

Decorators — Adding Behavior Without Changing Functions
pythonimport time
import functools

def timer(func):
    """Decorator that measures and prints function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} completed in {elapsed:.4f}s")
        return result
    return wrapper

@timer
def compute_sum(n: int) -> int:
    return sum(range(n))

total = compute_sum(10_000_000)
# compute_sum completed in 0.1823s

List Comprehensions vs. Traditional Loops
pythonnumbers = range(1, 21)

# Traditional loop — verbose but explicit
squares_of_evens = []
for n in numbers:
    if n % 2 == 0:
        squares_of_evens.append(n ** 2)

# List comprehension — idiomatic, readable, faster
squares_of_evens = [n ** 2 for n in numbers if n % 2 == 0]

print(squares_of_evens)
# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

Core Concepts Quick Reference
ConceptKey InsightDynamic TypingVariables hold references to objects, not typed containers — types live on objects, not variablesMutabilityLists, dicts, and sets are mutable; strings, tuples, and ints are immutable — affects aliasing behaviorLEGB RulePython resolves names from innermost (Local) to outermost (Built-in) scope — never outward*args / **kwargsAllows functions to accept arbitrary positional and keyword arguments — enables flexible APIsList Comprehension[expr for item in iterable if condition] — concise, readable, and faster than equivalent for-loopsself in OOPAn explicit reference to the current instance — Python does not inject it implicitly like some languagessuper()Delegates method calls to the parent class — essential for correct cooperative multiple inheritanceDuck Typing"If it walks like a duck and quacks like a duck, it's a duck" — Python cares about behavior, not typeDecoratorA function that takes a function and returns a new function — enables non-invasive behavior extensionGeneratorA lazy iterator that yields values one at a time — far more memory-efficient than materializing full lists

Why Python Fundamentals Matter
Every advanced Python concept — from NumPy's vectorized array operations to PyTorch's autograd engine, from FastAPI's dependency injection to LangChain's chain orchestration — is built on the foundations covered in this repository. Closures power decorators. Dunder methods make custom objects feel native. Generators underpin memory-efficient data pipelines. Comprehensions appear throughout modern ML preprocessing code.
Investing deeply in Python fundamentals does not merely make you a better Python programmer. It makes every framework, library, and abstraction you encounter more transparent, debuggable, and ultimately more yours to control.

Roadmap

 Error handling — try/except/finally, custom exception classes, exception chaining
 File I/O — reading, writing, and parsing text, CSV, and JSON files
 Modules and packages — import system, __init__.py, relative imports
 Standard library deep dive — itertools, functools, collections, pathlib, datetime
 Context managers — with statement, __enter__/__exit__, contextlib
 Concurrency basics — threading, multiprocessing, and asyncio fundamentals
 Type hints and static analysis — mypy, typing module, annotated function signatures


Author
Rajan M Upadhyay
MS Computer Science — Roosevelt University
LinkedIn · GitHub · rajanupadhyay2121@gmail.com
