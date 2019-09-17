"""""""""""""""""""""""""""""
패키지
"""""""""""""""""""""""""""""

# 패키지 내부의 모듈을 읽어 들이기(1)
import test_package.module_a as a
import test_package.module_b as b
print(a.variable_a)
print(b.variable_b)


# 패키지 내부의 모듈을 읽어 들이기(2)
from test_package import *
print(module_a.variable_a)
print(module_b.variable_b)