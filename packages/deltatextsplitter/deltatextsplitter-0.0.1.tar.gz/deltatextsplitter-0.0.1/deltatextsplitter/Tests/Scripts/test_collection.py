import sys
# caution: path[0] is reserved for script path (or '' in REPL)

# Import all our tests:
from Testdeltatextsplitter import deltatextsplitter_printtest

# Next use pytest to run all of our tests. In order to get pytest to pick
# up on our tests, we have to make sure that the script name is test_*.py and
# each function needs to starts with test_*() as well. Inside such a function,
# we need to call on of our own tests using the assert-command native to python.
# It works best if we only use a single assert-command per test_*()-function.

# NOTE: Documentation can be found at:
# https://coverage.readthedocs.io/en/latest/cmd.html
# https://docs.pytest.org/en/7.1.x/getting-started.html
# https://www.sealights.io/agile-testing/test-metrics/python-code-coverage/
# And of course, the Code.sh script.

# NOTE: Add your tests here!
def test_deltatextsplitter_printtest(): assert deltatextsplitter_printtest()==True
