# Welcome to condor assistant!

The condor_booklist can help you submit the condor jobs efficiently!

To install the package, do:
```
$ pip install --upgrade condor-assistant
```

To test the functionality do:

```
$ example.py
```

```
class condor_booklist(Executable = '', JobType = 'default_condor', JobName = '')

Parameters:
  Executable(string): executable
  JobType(string): name of the task (optional)
  JobName(string): name of the job (optional)
```
and

```
def submit(with_arguments=True)

submit the condor jobs that are booked in the booklist.

Parameters:
  with_arguments: True if argument is required for each job. False if no argument needs to be specified.
```

```
def add_Argument(Argument)

add one or more argument(s) (representing one or several job(s)) to the booklist

Parameters:
  Argument(string or a list of strings): the arguments to be specified after the executable
```

```
def set_Arguments(Arguments)

set the whole arguments (for all of the jobs that are going to be submitted)

Parameters:
  Arguments(list of strings): the argument list
```

```
def add_BlankArgument()

if there is no argument to be specified in a certain job. usually used when there is only one job per list
```

```
def initialdir_in_arguments()

add the initial directory path as the first argument (before all of the specified arguments)
```

```
def set_JobFlavour(JobFlavour)

setup the allowed running time.

Parameters:
  JobFavour = 'espresso'     => 20min
            = 'microcentury' => 1hr
            = 'longlunch'    => 2hr
            = 'workday'      => 8hr
            = 'tomorrow'     => 1d
            = 'testmatch'    => 3d
            = 'nextweek'     => 1w
```
```
def summary(keyword='')

print out the summary of the current condor booklist

Parameters:
  Keyword = ''(default) => all
          = 'basic'     => basic
```
More options can be found in the source codes.
