import re

# 주민등록번호 유효성을 확인하는 함수
def is_valid_resident_number(resident_number):
    # 정규 표현식 패턴을 정의합니다.
    pattern = r'^\d{6}-[1-2]\d{6}$'
    # 주어진 주민등록번호가 패턴과 일치하는지 확인합니다.
    return re.match(pattern, resident_number) is not None

# 10개의 샘플 주민등록번호를 생성합니다.
sample_resident_numbers = [
    "920101-1234567",  # 유효한 예시
    "990202-2345678",  # 유효한 예시
    "880303-3456789",  # 유효한 예시
    "750404-4567891",  # 유효한 예시
    "800505-5678912",  # 유효한 예시
    "690606-6789123",  # 유효한 예시
    "071212-1234567",  # 유효하지 않은 예시 (연도가 잘못됨)
    "950613-234567",   # 유효하지 않은 예시 (일자가 짧음)
    "820705-34567A9",  # 유효하지 않은 예시 (올바르지 않은 문자 포함)
    "7008101234567",    # 유효하지 않은 예시 (구분자 '-'가 빠짐)
]

# 샘플 주민등록번호의 유효성을 검사하고 결과를 출력합니다.
for resident_number in sample_resident_numbers:
    if is_valid_resident_number(resident_number):
        print(f"{resident_number}은(는) 유효한 주민등록번호입니다.")
    else:
        print(f"{resident_number}은(는) 유효하지 않은 주민등록번호입니다.")
