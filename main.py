"""
간단한 사칙연산 콘솔 프로그램
Arithmetic 클래스를 사용하여 사칙연산을 수행합니다.
"""

from src.arithmetic import Arithmetic


def get_integer_input(prompt):
    """정수 입력을 받는 함수"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("올바른 정수를 입력해주세요.")


def get_operator_input():
    """연산자 입력을 받는 함수"""
    valid_operators = ['+', '-', '*', '/', '÷']
    while True:
        operator = input("연산자>>").strip()
        if operator in valid_operators:
            return operator
        print(f"올바른 연산자를 입력해주세요. ({', '.join(valid_operators)})")


def calculate(arithmetic, a, operator, b):
    """연산자를 기반으로 계산을 수행하는 함수"""
    if operator == '+':
        return arithmetic.add(a, b)
    elif operator == '-':
        return arithmetic.subtract(a, b)
    elif operator == '*':
        return arithmetic.multiply(a, b)
    elif operator == '/' or operator == '÷':
        try:
            return arithmetic.divide(a, b)
        except ArithmeticError as e:
            raise e
    else:
        raise ValueError(f"지원하지 않는 연산자: {operator}")


def format_result(a, operator, b, result):
    """결과를 포맷팅하는 함수"""
    # 연산자 표시 통일 (÷를 /로 변환)
    display_operator = operator if operator != '÷' else '/'
    return f"{a}{display_operator}{b}={result}입니다."


def main():
    """메인 함수"""
    arithmetic = Arithmetic()
    
    # 입력 화면
    first_number = get_integer_input("첫번째 정수값>>")
    operator = get_operator_input()
    second_number = get_integer_input("두번째 정수값>>")
    
    # 결과 뷰 화면
    print("=" * 34)
    # 연산자 표시 통일
    display_operator = operator if operator != '÷' else '/'
    print(f"{first_number} {display_operator} {second_number}을 계산합니다.")
    print("=" * 34)
    
    try:
        result = calculate(arithmetic, first_number, operator, second_number)
        print(format_result(first_number, operator, second_number, result))
    except ArithmeticError as e:
        print(f"오류: {e}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()

