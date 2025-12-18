"""
Calculator Presenter
MVP 패턴의 Presenter - View와 Model(Service) 사이의 중재자

SOLID 원칙:
- SRP: UI 로직과 비즈니스 로직 연결만 담당
- DIP: View와 Service 모두 추상화(인터페이스)를 통해 통신
"""

from typing import Optional
from .calculator_window import CalculatorWindow
from ..service.calculator_service import CalculatorService


class CalculatorPresenter:
    """
    계산기 Presenter - View와 Service 사이의 중재자
    
    MVP 패턴의 Presenter 역할:
    - View로부터 사용자 입력을 받음
    - Service를 통해 비즈니스 로직 실행
    - 결과를 View에 전달
    """
    
    def __init__(self, view: CalculatorWindow, service: CalculatorService):
        """
        Presenter 초기화
        
        Args:
            view: 계산기 View (CalculatorWindow)
            service: 계산기 Service (CalculatorService)
        """
        self._view = view
        self._service = service
        
        # 상태 관리
        self._current_value = "0"
        self._operand1: Optional[float] = None
        self._operator: Optional[str] = None
        self._should_reset_display = False
        
        # View의 시그널을 Presenter의 슬롯에 연결
        self._connect_signals()
    
    def _connect_signals(self):
        """View의 시그널을 Presenter의 슬롯에 연결"""
        self._view.number_clicked.connect(self._on_number_clicked)
        self._view.operator_clicked.connect(self._on_operator_clicked)
        self._view.equals_clicked.connect(self._on_equals_clicked)
        self._view.clear_clicked.connect(self._on_clear_clicked)
        self._view.decimal_clicked.connect(self._on_decimal_clicked)
    
    def _on_number_clicked(self, number: str):
        """
        숫자 버튼 클릭 처리
        
        Args:
            number: 클릭된 숫자
        """
        if self._should_reset_display:
            self._current_value = number
            self._should_reset_display = False
        else:
            if self._current_value == "0":
                self._current_value = number
            else:
                self._current_value += number
        
        self._view.update_display(self._current_value)
    
    def _on_operator_clicked(self, operator: str):
        """
        연산자 버튼 클릭 처리
        
        Args:
            operator: 클릭된 연산자
        """
        try:
            # 현재 값을 첫 번째 피연산자로 저장
            current_num = float(self._current_value)
            
            # 이미 연산자가 입력된 상태면 계산 먼저 수행
            if self._operand1 is not None and self._operator is not None and not self._should_reset_display:
                self._perform_calculation()
                current_num = float(self._current_value)
            
            self._operand1 = current_num
            self._operator = operator
            self._should_reset_display = True
            
            # 수식 표시
            expression = f"{self._operand1} {operator}"
            self._view.update_expression(expression)
            
        except ValueError:
            self._view.show_error("잘못된 숫자 형식입니다")
    
    def _on_equals_clicked(self):
        """등호 버튼 클릭 처리"""
        self._perform_calculation()
    
    def _perform_calculation(self):
        """실제 계산 수행"""
        if self._operand1 is None or self._operator is None:
            return
        
        try:
            operand2 = float(self._current_value)
            
            # Service를 통해 계산 수행 (비즈니스 로직 분리)
            result = self._service.calculate(self._operand1, self._operator, operand2)
            
            if result.is_success:
                # 결과를 정수 또는 실수로 표시
                if isinstance(result.result, float) and result.result.is_integer():
                    self._current_value = str(int(result.result))
                else:
                    self._current_value = str(result.result)
                
                # 수식과 결과 표시
                expression = f"{result.operand1} {result.operator} {result.operand2} ="
                self._view.update_expression(expression)
                self._view.update_display(self._current_value)
                
                # 상태 초기화
                self._operand1 = None
                self._operator = None
                self._should_reset_display = True
            else:
                # 오류 처리
                self._view.show_error(result.error_message)
                self._reset_state()
        
        except ValueError:
            self._view.show_error("잘못된 숫자 형식입니다")
            self._reset_state()
        except Exception as e:
            self._view.show_error(f"계산 오류: {str(e)}")
            self._reset_state()
    
    def _on_clear_clicked(self):
        """초기화 버튼 클릭 처리"""
        self._reset_state()
        self._view.update_display("0")
        self._view.update_expression("")
    
    def _on_decimal_clicked(self):
        """소수점 버튼 클릭 처리"""
        if self._should_reset_display:
            self._current_value = "0."
            self._should_reset_display = False
        else:
            if "." not in self._current_value:
                self._current_value += "."
        
        self._view.update_display(self._current_value)
    
    def _reset_state(self):
        """계산기 상태 초기화"""
        self._current_value = "0"
        self._operand1 = None
        self._operator = None
        self._should_reset_display = False
