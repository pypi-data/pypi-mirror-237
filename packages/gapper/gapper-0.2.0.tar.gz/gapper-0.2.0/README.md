# Gradescope Autograder Packer (gapper)

## What's gapper? 

GAP is a tool that allows you to create a Gradescope autograder from a decorator. It's inspired by [aga](https://github.com/rileyshahar/aga) and reconstructed from the ground up to be easier to use and maintain. 

## Usage and Demonstration

### Installation

Install from PyPI
```bash
pip install gapper
```

Install from source
```bash
git clone https://github.com/FlickerSoul/gapper.git
pip install -e gapper
```

### Usage 

Suppose you'd like to create a Gradescope autograder that tests the following function: 

```python
def add(x: int, y: int) -> int:
    return x + y
```

You can create one by adding the `@problem` decorator to the function, and then specifying the test cases using the `@test_case` or `@test_cases` decorator. 

You can notice that the `@test_case` and `@test_cases` decorators take in parameters that should be passed into the function under test. 

```python
from gapper import problem, test_case, test_cases

@test_cases([5, 6], [7, 8])  # test_cases is a decorator that takes in a list of test cases
@test_case(3, 4)             # test_case is a decorator that takes in a single test case
@test_case(1, 2)             # they together generate 4 tests, where the parameters are 
@problem                     # x=1,y=2; x=3,y=4; x=5,y=6; x=7,y=8
def add(x: int, y: int) -> int:
    return x + y
```

The following are several ways to specify test cases. 

This is how you can specify a test cases with one iterable parameter.

```python
from gapper import problem, test_cases, param
from typing import Iterable, Generator
import random

def randomly_generate_numbers(times: int) -> Generator[param, None, None]:
    for _ in range(times):
        yield param([random.randint(0, 100) for _ in range(random.randint(0, 100))])

@test_cases(*randomly_generate_numbers(10), gap_max_score=1)
@test_cases(param([1, 2]), param([3, 4]))       # param is a helper that allows you to specify parameters, in a more 
@test_cases([[5, 6]], [[7, 8]])                 # readable way. This problem has 6 test cases, where the parameters are 
@test_cases.singular_params([9, 10], [11, 12])  # [1,2]; [3,4]; [5,6]; [7,8]; [9,10]; [11,12]. The three ways of 
@problem                                        # specifying parameters are equivalent. Note that 
def sum_many(args: Iterable[int]) -> int:       # @test_case([5, 6], [7, 8]) does not work because will treat [x, y]
    return sum(args)                            # as two parameters instead of a list.
```

This is how you can specify a test cases with keyword arguments.

```python
from gapper import problem, test_cases, test_case, param

@test_cases(param(0, x = 1, y = 2), param(3, x = 4, y = 5))  # You can also specify kwargs in the param or test_case 
@test_case(6, x = 7, y = 8)                                  # decorator. Note that using param is the only way to 
@test_case(9, x = 10)                                        # specify kwargs in test_cases.
@problem()                                                   
def add(a: int, x: int, y: int = 20) -> int:
    return a * x + y
```

This is how you can override the equality check between the solution and the submission.

```python
from gapper import problem, test_cases, test_case  
from typing import Iterable

def override_check(solution_ans, submission_ans) -> bool:
    return set(solution_ans) == set(submission_ans)

@test_cases(11, 12, 13, gap_override_check=override_check)
@test_case(10, gap_override_check=override_check)
@problem()
def generate_numbers(x: int) -> Iterable[int]:
    return range(x)
```

This is how you can override how the submission should be tested.

```python
from gapper import problem, test_case, test_cases
from gapper.core.unittest_wrapper import TestCaseWrapper
from gapper.core.test_result import TestResult

def override_test(tc: TestCaseWrapper, result: TestResult, solution, submission):
    solution_answer = solution(*tc.test_param.args)
    student_answer = submission(*tc.test_param.args)
    tc.assertEqual(solution_answer, student_answer)
    
    result.set_pass_status("failed")


@test_cases([3, 4], [5, 6], gap_override_test=override_test)
@test_case(1, 2, gap_override_test=override_test)
@problem()
def add(x: int, y: int) -> int:
    if x < 0 or y < 0:
        raise ValueError("x and y must be positive")
    return x + y
```


## TODO: 

- [ ] Add support debug support 
- [ ] Dev Documentation/Wiki