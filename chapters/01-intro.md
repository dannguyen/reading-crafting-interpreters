# Introduction

These notes follow *Crafting Interpreters*, Chapter 1: Introduction

https://craftinginterpreters.com/introduction.html

-------------

- Nystrom assumes that this is our "first foray into languages"
- Because implementing 2 interpreters is a lot of code, he says "this text is lighter on theory than others"



## 1.1 Why Learn This Stuff?

https://craftinginterpreters.com/introduction.html#why-learn-this-stuff


### 1.1.1 Little languages are everywhere

https://craftinginterpreters.com/introduction.html#little-languages-are-everywhere

- For every general-purpose language, Nystrom says there "are a thousand successful niche ones", which includes everything from **Make** to **sed** to **JSON**.
- Even though it's best to reuse an existing, proven language/format, sometimes we need to create custom parsers to fit our needs.


### 1.1.2 Languages are great exercise

- Nystrom compares implementing a language to a runner training in high altitudes and strapping on weights -- "a real test of programming skill"
- Concepts that must be mastered include: recursion, trees, graphs, and hash tables.
- "You probably use hash tables at least in your day-to-day programming, but how well do you really understand them?"


## 1.2 How the Book is Organized

https://craftinginterpreters.com/introduction.html#little-languages-are-everywhere

- First part is intro and getting oriented to concepts, including the "Lox" language that we will implement.
- 2nd and 3rd parts are each devoted to creating a complete interpreter
- Nystrom intends for us to know every line of code used to build the interpreters
- The coding style might not always follow best practices for writing "maintainable production software"; Nystrom says he wants "to keep the code easier on your eyes"
- Snippets will be "quite precise"
- Nystrom says the book has nermous asides relating to historical background and extended topics of study.
- Every chapter ends with a few exercises "to help you learn *more* than what's in the chapter"
- The "**design notes**" at the end of chapters reflect Nystron's belief that programmers must understand the "softer, human side of the equation" when it comes to design decisions and tradeoffs.


## 1.3 The First Interpreter

https://craftinginterpreters.com/introduction.html#the-first-interpreter

The first interpreter, named **jlox**, will be implemented in Java. The focus will be on "concepts" and writing the "simplest, cleanest code".

Java is a good language for this, Nystrom says, because it's high-level while having explicit features like static types. He says he chose Java "specifically because it is an object-oriented language", and that most readers will be familiar with that way of thinking. 


## 1.4 The Second Interpreter

https://craftinginterpreters.com/introduction.html#the-second-interpreter

The second implementation will focused on not just being correct, but fast. Nystrom says:

> C is the perfect language for understanding how an implementation really works, all the way down to the bytes in memory and the code flowing through the CPU.


## Challenges 

https://craftinginterpreters.com/introduction.html#challenges

(skipping these, because he's asking me to re-familiarize myself with Java and C and I just don't want to right now :p)


## Design Note: What's in a name?

https://craftinginterpreters.com/introduction.html#design-note

Naming things is hard, and Nystrom says that one of his hardest challenges was coming up for a name with the language that we'll implement. He says he went through "pages of candidates" before settling on Lox, a name that isn't already used (in computer science or by a culture), and easy to pronounce and search for. 

