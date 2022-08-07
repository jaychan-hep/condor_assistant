from condor_assistant import condor_booklist

# setup the condor bookklist with executable, jobtype(optional) and jobname(optional)
condor_list = condor_booklist('example.sh', 'example', 'test')

# add an argument to the booklist
condor_list.add_Argument('Hello World')

# add multiple arguments to the booklist
Arguments = ['Monkey', 'Badgers']
condor_list.add_Argument(Arguments)

# setup requested running time (default is 'tomrrow' => one day)
condor_list.set_JobFlavour('longlunch')

# print out the condor setting
condor_list.summary('Basic')

# submit the scheduled jobs
condor_list.submit()
