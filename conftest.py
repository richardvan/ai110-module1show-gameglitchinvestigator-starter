# FIX: Add conftest.py for pytest import error,  needed by because test scripts are inside a subdirectory
#      By adding conftest.py (as empty file) to the project root, pytest will be able to find the test modules
#      There are other approahces to fix pytest import errors, but this is a widely used and simple solution.