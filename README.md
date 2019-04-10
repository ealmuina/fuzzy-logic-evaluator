# Fuzzy Logic Evaluator

## Synopsis
This project implements a tool written in * Python 3 * that allows the user to:
* Define a diffuse inference system:
  - Define the input and output variables, with their respective linguistic values ​​and membership functions
  - Define the rules of inference
  - Specify the method to be used
  - Define the step size to be used in the discretization of the values ​​of the output variables
* Use the defined inference system, to obtain the values ​​of the output variables for different data sets

## Input
The program is executed by means of the command:

```bash
python main.py <data> .json <rules> .fuz [--step <step_size>]
```

`<data> .json`: file in JSON format with the specifications of the input variables and their respective values, as well as the membership functions. An example of a variable and a function would be:
```json
{
  "variables": {
    "input1": 5.3
  }
  "functions": {
    "membership_func1": [
      "Trapezoid", 10, 15, 20, 25
    ]
  }
}
```
As can be deduced from the example, the functions are specified by a list, whose first element is the type of the function and the rest are the parameters that characterize its behavior; the latter being specific to each type.
The types of supported functions are:
* __Trapezoid__:
  - `a`: Point where the monotony of the function becomes increasing, therefore` f (a) == 0`. If `a == null` it is assumed that for any` x <= a` it is fulfilled that `f (x) == 1`.
  - `b`: Minor (greater if` a == null`) value of `x` for which` f (x) == 1`.
  - `c`: Greater value of` x` for which `f (x) == 1`, if there is no such` x` finite, then `c == null`. If `a == null`, then it is the smallest value of` x` for which `f (x) == 0`.
  - `d`: Point where the monotony stops being decreasing. If it does not exist, or `a == null`, then` c == null`.
* __Triangle__: Particular case of trapezoid, with three parameters `a`,` b` and `c` representing the` x` of its 3 vertices.
* __Sigmoid__:
  - `k`: Sigmoid width
  - `x0`: Central value
* __Gaussian__:
  - `b`: Center of the bell
  - `c`: Bell width

`<rules> .fuz`: file with the specification of the rules and the inference model; Follow the following format:
```
[model] (Mamdani | Sugeno | Tsukamoto)
[t-norm] (min | product)
[t-conorm] (max | sum)
([defuzzy] (Centroid | Bisecter | Mean_max))?

input1 is val1 or input2 is val2 then output1 is val3
```
All variables defined to the left of the `then` must have an associated value in the data file (.json). It also has to happen with the linguistic values used in the rules.
In the case of using the model * Sugeno *, the value of the right part of the `then` will be an arithmetic expression that can use numerical values and input variables. The operators allowed in this case are `+`, `-`,` * `,` / `and` ** `(power).

In the `t-norm` and` t-conorm` fields the operations to evaluate the expressions `and` and` or` respectively will be indicated.

## Output
The program reports the result of evaluating the specified system. The calculated values for each of the output variables are reported by the standard output, following the format: `output1: # .000 \ n`
