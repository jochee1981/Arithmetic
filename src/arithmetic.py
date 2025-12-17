"""
TC-CMM-001: Common Module / Core Mathematical Module
산술 연산 모듈
"""


class Arithmetic:
    """산술 연산을 수행하는 클래스"""
    
    def add(self, a, b):
        """두 수의 합을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 합
        """
        return a + b
    
    def subtract(self, a, b):
        """두 수의 차를 계산합니다.
        
        Args:
            a: 첫 번째 숫자 (피감수)
            b: 두 번째 숫자 (감수)
            
        Returns:
            두 수의 차
        """
        return a - b
    
    def divide(self, a, b):
        """두 수의 정수 나눗셈을 계산합니다 (버림 처리).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            정수 나눗셈 결과 (버림)
            
        Raises:
            ArithmeticError: 제수가 0일 때 발생
        """
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b


if __name__ == "__main__":
    """모듈이 직접 실행될 때 예제 코드를 실행합니다."""
    print("=" * 50)
    print("Arithmetic Operations Module - 예제 실행")
    print("=" * 50)
    print()
    
    arithmetic = Arithmetic()
    
    # 덧셈 예제
    print("1. 덧셈 (Addition)")
    print(f"   1 + 10 = {arithmetic.add(1, 10)}")
    print(f"   0 + 1 = {arithmetic.add(0, 1)}")
    print(f"   -1 + (-10) = {arithmetic.add(-1, -10)}")
    print()
    
    # 뺄셈 예제
    print("2. 뺄셈 (Subtraction)")
    print(f"   5 - 2 = {arithmetic.subtract(5, 2)}")
    print()
    
    # 나눗셈 예제
    print("3. 나눗셈 (Division - 정수 나눗셈)")
    print(f"   5 / 2 = {arithmetic.divide(5, 2)}")
    print(f"   -10 / 2 = {arithmetic.divide(-10, 2)}")
    print()
    
    # 예외 처리 예제
    print("4. 예외 처리 (Exception Handling)")
    try:
        result = arithmetic.divide(0, 0)
        print(f"   0 / 0 = {result}")
    except ArithmeticError as e:
        print(f"   0 / 0 → {type(e).__name__}: {e}")
    print()
    
    print("=" * 50)
    print("예제 실행 완료")
    print("=" * 50)

