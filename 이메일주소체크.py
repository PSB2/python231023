# Python에서 정규 표현식을 다루기 위한 re 모듈을 불러옵니다.
import re

# 주어진 이메일 주소가 유효한지 확인하는 함수를 정의합니다.
def is_valid_email(email):
    # 유효한 이메일 주소 패턴을 정의합니다.
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # re.search() 함수를 사용하여 주어진 이메일 주소가 패턴과 일치하는지 확인합니다.
    return re.search(pattern, email) is not None

# 테스트할 샘플 이메일 주소들을 리스트로 정의합니다.
sample_emails = [
    "user@example.com",                   # 유효함
    "user.name@domain.com",               # 유효함
    "user123@sub.domain.com",             # 유효함
    "user_name123@domain-name.com",       # 유효함
    "user123@domain",                     # 유효하지 않음 (상위 도메인이 누락됨)
    "user@com",                           # 유효하지 않음 (도메인 이름이 누락됨)
    "user@domain..com",                   # 유효하지 않음 (도메인 이름에 두 개의 점이 연속됨)
    "@domain.com",                        # 유효하지 않음 (사용자 이름이 누락됨)
    "user@-domain.com",                   # 유효하지 않음 (도메인 이름에 특수 문자가 포함됨)
    "user@domain.c",                      # 유효하지 않음 (짧은 상위 도메인)
]

# 샘플 이메일 주소의 유효성을 검사하고 결과를 출력합니다.
for email in sample_emails:
    # is_valid_email 함수를 이용하여 현재 이메일 주소가 유효한지 검사하고 결과를 출력합니다.
    if is_valid_email(email):
        print(f"{email}은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"{email}은(는) 유효하지 않은 이메일 주소입니다.")
