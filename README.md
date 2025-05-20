# 🐍 Lekans Compiler

A lightweight compiler for a minimal, educational programming language inspired by Python and functional languages. This project demonstrates core compiler concepts such as parsing, SSA transformation, optimization, and code generation.

## 🚀 Overview

lekans is a dynamic-typed, expression-oriented language with a Pythonic syntax and a strong emphasis on simplicity. The Compiler translates `.dbk` source files to optimized assembly or bytecode for a custom virtual machine.

This project is ideal for those studying compiler design, language implementation, or working on educational language projects.


## ✨ Features

- Lexer and parser (auto generation with lalrpop)
- AST generation
- dynamic type checking
- Intermediate representation in SSA form
- Basic optimizations (constant folding, dead code elimination)
- Essential optimization: Register allocation & runtime type-check removal
- Backend code generation (x86_64)

## 🐍 .dbk Syntax Example

```snk
def main(x):
  let x = x[0] in
  def factorial(n):
    if n == 0: 1 else: n * factorial(n - 1)
  in
  factorial(x)
