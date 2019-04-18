from io import StringIO # import java.io.InputStreamReader;
from pathlib import Path

import utils.cli




class Lox:
    """A Lox interpreter"""

    def cli():
        utils.cli.main()
        """define the CLI interface here"""

















"""
Based off of Chapter 4.1: The Interpreter Framework
https://craftinginterpreters.com/scanning.html#the-interpreter-framework


Java code:

```java
package com.craftinginterpreters.lox;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Lox {
  public static void main(String[] args) throws IOException {
    if (args.length > 1) {
      System.out.println("Usage: jlox [script]");
      System.exit(64);
    } else if (args.length == 1) {
      runFile(args[0]);
    } else {
      runPrompt();
    }
  }
}
```
"""
