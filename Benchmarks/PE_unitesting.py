import timeout_decorator
from PE_Benchmark import get_languages, get_PE_dir, LANGUAGES, define_function


def get_args_and_ans(testline):
    _, arguments, answer = testline.split(":")
    if "," in arguments:
        arguments = map(int, arguments.split(","))
    else:
        arguments = [int(arguments)]
    return arguments, int(answer)


def is_solved(PE, language):

    filename = 'PE_{:0>3}'.format(PE)
    f = define_function(PE)
    path = get_PE_dir(PE)
    answer_fil = open(path + "/Tests/" + filename + "_test_01.txt")
    _, arguments, answer = get_2_args_and_ans(answer_fil.readlines(0)[0])

    if language.lower() == 'python':
        return f(*arguments) == answer


def unit_tests_python(PE, language, function = None, unit_test=2):
    path = get_PE_dir(PE) + '/Tests/'
    testname = "PE_{:0>3}_test_{:0>2}.txt".format(PE, unit_test)

    try:
        function()
    except:
        f = define_function(PE)

    unit_test_results = []
    for line in open(path + testname).read().splitlines():
        args, ans = get_args_and_ans(line)
        is_correct, is_timeout = is_solved_within_x(f, args, ans)
        if is_timeout:
            break
        unit_test_results.append(is_correct)
    return unit_test_results


def write_2_solutionfile(PE, language):
    return PE


def is_solved_within_x(function, arguments, answer, x=60):
    @timeout_decorator.timeout(x)
    def is_answer(function, arguments, answer):
        return function(*arguments) == answer
    try:
        return is_answer(function, arguments, answer), False
    except:
        return False, True


PE = 4
language = 'python'
function = None
unit_test = 2
print(unit_tests_passed(PE, language, function, unit_test))


