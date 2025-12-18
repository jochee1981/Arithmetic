"""
PyQt6 GUI 계산기 애플리케이션
MVP 패턴과 SOLID 원칙을 적용한 리팩토링 버전

실행 방법:
    python main_gui.py

의존성:
    pip install -r requirements.txt
"""

import sys
from PyQt6.QtWidgets import QApplication
from src.service.calculator_service import CalculatorService
from src.ui.calculator_window import CalculatorWindow
from src.ui.calculator_presenter import CalculatorPresenter


def main():
    """
    GUI 계산기 애플리케이션 진입점
    
    의존성 주입 (Dependency Injection) 적용:
    1. Service 객체 생성 (Model)
    2. View 객체 생성 (View)
    3. Presenter가 Service와 View를 조합 (Presenter)
    
    이를 통해 각 계층이 독립적으로 테스트 가능하며,
    DIP(의존성 역전 원칙)를 준수합니다.
    
    MVP 패턴 구조:
    ┌──────────────┐
    │     View     │ ← 사용자 입력/출력
    │ (Window)     │
    └──────┬───────┘
           │ Signal/Slot
    ┌──────▼───────┐
    │  Presenter   │ ← UI 로직
    └──────┬───────┘
           │ Method Call
    ┌──────▼───────┐
    │    Model     │ ← 비즈니스 로직
    │  (Service)   │
    └──────────────┘
    """
    # QApplication 생성
    app = QApplication(sys.argv)
    app.setApplicationName('계산기')
    
    # 의존성 생성 (Dependency Injection Container 역할)
    service = CalculatorService()  # Model
    view = CalculatorWindow()      # View
    presenter = CalculatorPresenter(view, service)  # Presenter
    
    # View 표시
    view.show()
    
    # 이벤트 루프 시작
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
