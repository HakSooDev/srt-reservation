import argparse

def parse_cli_args():

    parser = argparse.ArgumentParser(description='SRT 예약 시스템 CLI.')

    # 사용자 인증 정보
    user_group = parser.add_argument_group('사용자 인증 정보')
    user_group.add_argument("--userid", help="사용자 ID (예: 1234567890)", type=str, metavar="사용자ID")
    user_group.add_argument("--pwd", help="비밀번호", type=str, metavar="비밀번호")

    # 여정 정보
    travel_group = parser.add_argument_group('여정 정보')
    travel_group.add_argument("--dep", help="출발역 (예: 동탄)", type=str, metavar="출발역")
    travel_group.add_argument("--arr", help="도착역 (예: 동대구)", type=str, metavar="도착역")
    travel_group.add_argument("--date", help="출발 날짜 (YYYYMMDD 형식, 예: 20220118)", metavar="날짜")
    travel_group.add_argument("--time", help="출발 시간 (24시간 형식, 예: 08, 10, 12, ...22)", type=str, metavar="시간")

    # 좌석 유형
    seat_group = parser.add_argument_group('좌석 옵션')
    seat_group.add_argument("--std", help="일반실 예약 (기본값: False)", action='store_true')
    seat_group.add_argument("--first", help="특실 예약 (기본값: False)", action='store_true')

    # 추가 옵션
    additional_group = parser.add_argument_group('추가 옵션')
    additional_group.add_argument("--trains", help="확인할 기차 수 (기본값: 3)", metavar="확인 기차 수", default=3)
    additional_group.add_argument("--waitlist", help="예약대기 사용 여부 (기본값: False)", action='store_true')
    additional_group.add_argument("--no-alert", help="알림 비활성화 (기본값: False)", action='store_true', default=False)

    args = parser.parse_args()

    return args
