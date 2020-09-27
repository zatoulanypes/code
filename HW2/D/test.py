from D import solution
import time
def get_testcase(file):
    with open(file) as f:
        cases = f.read().split('-'*15)
        for case in cases:
            inp, out = case.split('OUTPUT:')
            inp = inp.strip().strip('INPUT:').strip()
            out = out[1:-1]
            yield inp, out

start = time.time()
case = 1
for inp, out in get_testcase('TestCasesD.txt'):
    attempt = solution(*eval(inp))
    assert str(attempt) == out, f"Case {case} failed!\nInput:\n{inp}\nExpected:\n{out}\nGot:\n{attempt}"
    print(f'Case {case}: OK')
    case += 1
end = time.time()
assert end - start <= 2, "Time limit exceeded!"
print('All tests passed!')
