# My Threadpool project
Simplify threadpool operations

## Usage
Override `Job` do your work in the `execute` method, set `result` to `JobCompletionStatus` when it's done.  
The actual thread will use this to determine what to do next.

A `MemoryJobQueue` is provided, override `JobQueue` to handle specific cases, like db queues, etc.  
The `ThreadPool` object sometimes doesn't exit correctly, and python task needs to be killed - known bug,  working on it.  
Most of the time it works fine with no issues.
Check the unit tests for more usage details   


## Building
`python -m build `

## Deploying
`python -m twine upload --repository testpypi dist/*`