<p align="center">
    <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fredrikofstad/stratpy/blob/main/res/stratpy-dark.png?raw=true">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/fredrikofstad/stratpy/blob/main/res/stratpy-light.png?raw=true">
    <img alt="stratpy logo" src="https://github.com/fredrikofstad/stratpy/blob/main/res/stratpy-light.png?raw=true">
    </picture>
</p>

## Stratpy - A python library for Game Theory written in rust

Read the documentation [here!](https://stratpy-docs.readthedocs.io/en/latest/)

 <!-- start info -->
### Motivation:
- Create an easy to use python package for game theory catering to alternate disciplines like polisci.
- Backend created in rust offering a modern fast and memory-safe language, while python allows for an easy api for 
the scientific community.

### Features:

- Normal form and Extensive form games (including incomplete information)
- Solve games using user-ordered preferences (unknown but orderable variables)
- Easily export games to latex and other formats
 <!-- end info -->

 <!-- start quickstart -->
### Installation

```bash
$ pip install stratpy
```

### Usage

```python
>>> from stratpy import *
>>> 
>>> game1 = Game("Title")

```
 <!-- end quickstart -->
Read more about how to use the library [here!](https://stratpy-docs.readthedocs.io/en/latest/)
