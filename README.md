Mateus Luiz Salvi - Pedro Henrique Augustin - Bruna Casagranda Cagliari

[b]Eight queens problem:[/b]
Development of an AI using genetic code algorithm to solve the eight queens problem, where the objective is to populate a chess board with the maximum possible number of queens without attacks between them.

Aditional lib:
Matplotlib: python -m pip install -U matplotlib

Satisfatory results can be obtained using the following parameters for execution, mostly 0-1 conflicts between queens:
run_ga(200, 20, 5, 0.1, True)
200 generations, 20 participants per tournament, 5 tournaments for each generation, 1% chance of mutation and Elitism enabled.

Changes in the default algorithm:
-We opted for not leting the same participant engange on differents tournaments, once the best is found on a tournament he is removed from the participants list, ensuring variation and not leting their genetic code take over.
-We opted for not stopping the algorithm once the best individual is found (0 conflicts between queens), for data analysis and seeing how the algorithm evolves over time with generations graphs.

[b]Linear regression algorithm[/b]:
Development of and algorithm to extipulate prices of land in Alegrete - Brazil with ficctional data.

Aditional lib:
Numpy: pip install numpy

Satisfatory results can be obtained using the following parameters for ThetaA and ThetaB:
