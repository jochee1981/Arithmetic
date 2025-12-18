"""
Calculator Window - PyQt6 GUI View
MVP (Model-View-Presenter) 패턴의 View 역할

SOLID 원칙:
- SRP: UI 표시만 담당
- DIP: Presenter를 통해 비즈니스 로직과 분리
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QPushButton, QLineEdit, QLabel
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class CalculatorWindow(QMainWindow):
    """
    계산기 메인 윈도우 (View)
    
    MVP 패턴에서 View의 역할:
    - UI 요소 표시 및 배치
    - 사용자 입력을 Signal로 전달
    - Presenter로부터 받은 데이터를 화면에 표시
    """
    
    # 시그널 정의 (View -> Presenter 통신)
    number_clicked = pyqtSignal(str)
    operator_clicked = pyqtSignal(str)
    equals_clicked = pyqtSignal()
    clear_clicked = pyqtSignal()
    decimal_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """UI 초기화"""
        self.setWindowTitle('계산기 - PyQt6')
        self.setFixedSize(400, 550)
        
        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 메인 레이아웃
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 디스플레이 영역
        self._create_display(main_layout)
        
        # 버튼 영역
        self._create_buttons(main_layout)
        
        # 스타일 적용
        self._apply_styles()
    
    def _create_display(self, parent_layout):
        """디스플레이 영역 생성"""
        display_layout = QVBoxLayout()
        
        # 수식 표시 레이블
        self.expression_label = QLabel('')
        self.expression_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.expression_label.setFixedHeight(40)
        expression_font = QFont('Arial', 14)
        self.expression_label.setFont(expression_font)
        self.expression_label.setStyleSheet("color: #666; padding-right: 10px;")
        
        # 현재 값 표시 라인에디트
        self.display = QLineEdit('0')
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(80)
        display_font = QFont('Arial', 28, QFont.Weight.Bold)
        self.display.setFont(display_font)
        
        display_layout.addWidget(self.expression_label)
        display_layout.addWidget(self.display)
        parent_layout.addLayout(display_layout)
    
    def _create_buttons(self, parent_layout):
        """버튼 그리드 생성"""
        grid = QGridLayout()
        grid.setSpacing(5)
        
        # 버튼 정의 (텍스트, 행, 열, 행스팬, 열스팬, 타입)
        buttons = [
            ('7', 0, 0, 1, 1, 'number'),
            ('8', 0, 1, 1, 1, 'number'),
            ('9', 0, 2, 1, 1, 'number'),
            ('×', 0, 3, 1, 1, 'operator'),
            
            ('4', 1, 0, 1, 1, 'number'),
            ('5', 1, 1, 1, 1, 'number'),
            ('6', 1, 2, 1, 1, 'number'),
            ('-', 1, 3, 1, 1, 'operator'),
            
            ('1', 2, 0, 1, 1, 'number'),
            ('2', 2, 1, 1, 1, 'number'),
            ('3', 2, 2, 1, 1, 'number'),
            ('+', 2, 3, 1, 1, 'operator'),
            
            ('+/-', 3, 0, 1, 1, 'function'),
            ('0', 3, 1, 1, 1, 'number'),
            ('.', 3, 2, 1, 1, 'decimal'),
            ('=', 3, 3, 1, 1, 'equals'),
            
            ('C', 4, 0, 1, 2, 'clear'),
            ('/', 4, 2, 1, 2, 'operator'),
        ]
        
        for button_info in buttons:
            text, row, col, rowspan, colspan, btn_type = button_info
            button = QPushButton(text)
            button.setFixedHeight(70)
            
            # 버튼 타입별 이벤트 연결
            if btn_type == 'number':
                button.clicked.connect(lambda checked, t=text: self.number_clicked.emit(t))
                button.setObjectName('numberButton')
            elif btn_type == 'operator':
                # × 기호를 * 로 변환
                operator = '*' if text == '×' else text
                button.clicked.connect(lambda checked, o=operator: self.operator_clicked.emit(o))
                button.setObjectName('operatorButton')
            elif btn_type == 'equals':
                button.clicked.connect(self.equals_clicked.emit)
                button.setObjectName('equalsButton')
            elif btn_type == 'clear':
                button.clicked.connect(self.clear_clicked.emit)
                button.setObjectName('clearButton')
            elif btn_type == 'decimal':
                button.clicked.connect(self.decimal_clicked.emit)
                button.setObjectName('numberButton')
            elif btn_type == 'function':
                button.setEnabled(False)  # +/- 기능은 향후 구현
                button.setObjectName('functionButton')
            
            grid.addWidget(button, row, col, rowspan, colspan)
        
        parent_layout.addLayout(grid)
    
    def _apply_styles(self):
        """스타일시트 적용"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            
            QLineEdit {
                background-color: white;
                border: 2px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                color: #333;
            }
            
            QPushButton {
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 8px;
                font-size: 22px;
                font-weight: bold;
                color: #333;
            }
            
            QPushButton:hover {
                background-color: #f5f5f5;
            }
            
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
            
            QPushButton#numberButton {
                background-color: #fff;
            }
            
            QPushButton#operatorButton {
                background-color: #ff9500;
                color: white;
                border: none;
            }
            
            QPushButton#operatorButton:hover {
                background-color: #ffad33;
            }
            
            QPushButton#operatorButton:pressed {
                background-color: #e68a00;
            }
            
            QPushButton#equalsButton {
                background-color: #007aff;
                color: white;
                border: none;
            }
            
            QPushButton#equalsButton:hover {
                background-color: #3395ff;
            }
            
            QPushButton#equalsButton:pressed {
                background-color: #0062cc;
            }
            
            QPushButton#clearButton {
                background-color: #ff3b30;
                color: white;
                border: none;
            }
            
            QPushButton#clearButton:hover {
                background-color: #ff6259;
            }
            
            QPushButton#clearButton:pressed {
                background-color: #cc2e24;
            }
            
            QPushButton#functionButton {
                background-color: #e0e0e0;
                color: #999;
            }
        """)
    
    # View 메서드 - Presenter에서 호출
    def update_display(self, value: str):
        """
        디스플레이 업데이트
        
        Args:
            value: 표시할 값
        """
        self.display.setText(value)
    
    def update_expression(self, expression: str):
        """
        수식 라벨 업데이트
        
        Args:
            expression: 표시할 수식
        """
        self.expression_label.setText(expression)
    
    def show_error(self, message: str):
        """
        에러 메시지 표시
        
        Args:
            message: 에러 메시지
        """
        self.display.setText("오류")
        self.expression_label.setText(message)
    
    def get_current_display(self) -> str:
        """
        현재 디스플레이 값 반환
        
        Returns:
            현재 표시 중인 값
        """
        return self.display.text()
