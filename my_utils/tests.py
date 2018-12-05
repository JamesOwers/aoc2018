import os


def test_function(fun, test_data, expand=False):
    """Utility function for testing
    
    Arguments
    ---------
    fun : function, the function to perform the test on
    test_data : dict, dictionary with two keys - 'inputs' and 'outputs'. Each
        value in the dict is a list. dict['inputs'][ii] is the input to the
        function fun for which the expected output is dict['outputs'][ii]
    expand : bool, whether to expand dict['inputs'][ii] i.e. evaluate
        fun(*dict['inputs'][ii]), or fun(dict['inputs'][ii]). This is to allow
        the supply of a list of arguments.
    
    Returns
    -------
    nr_errors : int, the number of tests that failed
    """
    nr_errors = 0
    for kk, vv in zip(test_data['inputs'], test_data['outputs']):
        if expand:
            ans = fun(*kk)
        else:
            ans = fun(kk)
        if ans != vv:
            print('fun({}) != {} (={})'.format(kk, vv, ans))
            nr_errors += 1
    return nr_errors


def test_and_solve(test_datas, functions, puzzle_input=None, 
                   test_functions=None, expand=False):
    if test_functions is None:
        test_functions = functions
    for ii, (test_data, fun) in enumerate(zip(test_datas, test_functions)):
        nr_errors = test_function(fun, test_data, expand)
        if nr_errors == 0:
            print('Pt. {} Tests Passed'.format(ii+1))

    if puzzle_input is not None:
        for ii, fun in enumerate(functions):
            ans = fun(puzzle_input)
            print('Pt. {} Solution: {}'.format(ii+1, ans))