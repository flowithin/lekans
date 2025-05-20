# 🐍 SnakeLang Compiler

A lightweight compiler for **SnakeLang** — a minimal, educational programming language inspired by Python and functional languages. This project demonstrates core compiler concepts such as parsing, SSA transformation, optimization, and code generation.

## 🚀 Overview

SnakeLang is a statically-typed, expression-oriented language with a Pythonic syntax and a strong emphasis on simplicity. The SnakeLang Compiler (`snakec`) translates `.snk` source files to optimized assembly or bytecode for a custom virtual machine.

This project is ideal for those studying compiler design, language implementation, or working on educational language projects.

## ✨ Features

- Lexer and parser (handwritten or using ANTLR/flex+bison)
- AST generation
- Static type checking
- Intermediate representation in SSA form
- Basic optimizations (constant folding, dead code elimination)
- Backend code generation (x86_64 or VM bytecode)
- Custom standard library with built-in functions
- REPL for interactive execution

## 🐍 SnakeLang Syntax Example

```snk
let x = 10
let y = 20
let sum = fn(a, b) => a + b
print(sum(x, y))
