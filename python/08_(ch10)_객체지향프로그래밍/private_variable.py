# ------------------------------------------------------
# 실습 1: 인스탄스 메서드를 이용한 private, public 변수 접근 사례
# ------------------------------------------------------

class SomeThing:
    __prv = 'private'   # private variable
    _prt = 'protected'  # public variable

    def write_prv(self, value):  # instance method
        SomeThing.__prv = value

    def read_prv(self):
        return SomeThing.__prv


r = SomeThing()
print(r.read_prv())     # private
r.write_prv(100)
print(r.read_prv())     # 100
r._prt = 'non protected'
print(r._prt)           # non protected

r2 = SomeThing()
r2._prt = 'new'
print(r2._prt)          # new
print(r._prt)           # non protected

# print(r.__prv)  # 오류 발생. 외부에서 사적변수 접근 불가
# AttributeError: 'SomeThing' object has no attribute '__prv'

exit()
