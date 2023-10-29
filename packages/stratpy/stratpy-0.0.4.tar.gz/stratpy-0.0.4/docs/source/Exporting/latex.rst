# Exporting to latex

To export to your game model to latex, use the export_latex() method of the game class.

>>> example_game.export_latex()

.. autofunction:: example_game.export_latex(scale, file_path)

| parameters:
| ``scale:`` An optional scale in float, scaling the final resulting latex figure (default 2.5)
| ``file_path:`` an optional filepath and filename of the output.tex file

Example:

>>> # Exports the game with scale 1.5 as figure.tex in an output folder
>>> example_game.export_latex(1.5, "output/figure.tex")
>>> game.export_latex() # exports the raw latex code to the terminal

Make sure the output folder is created, or an error will occur.

After creating the latex, further styling can be done manually.
Instead of bogging the function down with optional parameters,
simplicity was favored.
