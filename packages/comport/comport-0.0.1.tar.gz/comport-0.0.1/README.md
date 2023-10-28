# comport

`comport` is a modern library for writing [business-driven development (BDD)](https://en.wikipedia.org/wiki/Behavior-driven_development) tests in Python. `comport` provides a type-safe way to implement tests using the [Gherkin language](https://cucumber.io/docs/gherkin/).

## What's different about `comport`?

`comport` is built on top of pydantic, and provides several benefits over other Python BDD testing frameworks.

### Support for modern tooling

`comport` uses pyproject.toml for tooling, and has configurable discovery. You have control over where your tests and step implementations are stored.

### Better editor support

`comport`'s test context is typed using `pydantic`, and has controllable mutability. It's common for testing frameworks to treat the test context as a big, mutable bag of state; this leads to poor editor support ('was context.temp_dir a string, a path, or a `tempfile.TemporaryDirectory`?'). Typing context variables ahead of time makes your
test steps easier to write.

### Better setup and teardown

Another side effect of the 'big bag of state' model is convoluted teardown ('ah, I've added temporary tables in this step, I'll need to add a teardown for those in `after_scenario`'). `comport` gets around this by enabling control for variable scope.

### Contextual contexts

`comport`'s test contexts are more granular than other testing frameworks. You can configure separate test contexts for different steps, to make it clear what their
requirements are.


## What are the requirements?

`comport` requires Python 3.10+ and pydantic 2+.