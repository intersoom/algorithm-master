# 알고리즘 마스터
> 빡세게 풀어서 개발자 되기 👀

💡 **코딩 테스트 합격자 되기 책**을 따라가며, 기록한 내용입니다.

**0) 코딩 테스트를 준비하기 전에**

1. 합격자가 꼭 되고 싶은 여러분
    - 타인의 풀이를 보고 사고를 넓히기
    - 나만의 테스트 케이스 만들기
        
        → **문제 분석 단계**에서 **테스트 케이스** 만들기
        
2. 아는 것과 모르는 것을 명확하게
    - 기록하라!
        
        → 문제를 다 풀지 못해도 어디까지 생각해봤는지 우선 기록하기
        
        → 나중에 답안을 보면서 어디가 다른지 확인하며 복기
        
    - 시험 보듯 공부하라
        
        → 긴장감을 연습하기
        
    - 나만의 언어로 요약하라
        
        → 정말 이해했는지 확인하기..!
        

**1) 코딩 테스트 효율적으로 준비하기**

1. 문제 분석 연습하기
    
    50-60%는 문제를 분석하는데 쓰는 것이 좋음
    
    - 문제를 쪼개서 분석하라!
        
        → 동작 단위로 쪼개서 분석하는 것이 유리함
        
    - 제약사항을  파악하고 테스트 케이스를 추가한다
        
        → 이 과정은 어떤 알고리즘을 사용할지 고민하는데 유용 + 예외 거를 때 도움됨
        
    - 입력값을 분석하라!
        
        → 입력 값의 크기를 보면 제한 시간 내에 풀 수 있는 알고리즘을 구분할 수 있음
        
    - 핵심 키워드 파악
        
        → pg. 36 참고
        
    - 데이터 흐름이나 구성을 파악하라
        
        → 삽입 / 삭제가 빈번하면 heap
        
        → 데이터가 50개 미만이면 하드 코딩 고려
        
        이런 식으로 데이터 흐름이나 구성을 파악해서 풀이 방법을 고려해야함
        
2. 의사 코드로 설계하는 연습하기
    - 세부 구현이 아닌 동작 중심으로 작성
    - 문제 해결 순서로 작성하라
    - 충분히 테스트 하라
        
        → 구현 단계로 갈 수록 잘못된 부분을 수정하는데 드는 비용이 크기 때문에 의사코드 단계에서 충분히 테스트 해보기!
        

**2) 알고리즘의 효율 분석**

1. 시간 복잡도
    - 최악의 경우 시간 복잡도를 표현하는 빅오 표기법
        
        → 최고 차항과 차수를 제외하면 시간 복잡도가 나옴
        
    - 시간 복잡도를 코딩 테스트에 활용하는 방법
        
        → 코딩 테스트에는 제한 시간이 존재하므로 문제를 분석하고 빅오 표기법을 활용해 해당 알고리즘을 적용했을 때, 제한 시간 내에 출력 값이 나올 수 있는지 확인
        
        → 초당 연산 가능 횟수는 1억번
        
        → pg.61
        

**3) 코딩 테스트 기본 문법**

1. 코딩 테스트 코드 구현 노하우
    - 조기 반환
    - 보호 구문
    - 합성 함수
        
        → 람다식 활용
        
        ```python
        composed_function = lambda x: square(add_three(x))
        
        print(composed_function(3)) # 36
        ```

