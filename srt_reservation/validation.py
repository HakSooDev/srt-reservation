from datetime import datetime, timedelta
import re


station_list = [
    "수서", "동탄", "평택지제", "곡성", "공주", "광주송정", "구례구",
    "김천(구미)", "나주", "남원", "대전", "동대구", "마산", "목포",
    "밀양", "부산", "서대구", "순천", "신경주", "여수EXPO", "여천",
    "오송", "울산(통도사)", "익산", "전주", "정읍", "진영", "진주",
    "창원", "창원중앙", "천안아산", "포항"
]

def validate_args(args):
    if not args.userid:
        raise Exception("사용자 ID를 입력해주세요.")
    if not args.pwd:
        raise Exception("비밀번호를 입력해주세요.")
    
    if args.dep not in station_list:
        raise Exception("출발역을 다시 확인해주세요.")
    if args.arr not in station_list:
        raise Exception("도착역을 다시 확인해주세요.")
    if args.dep == args.arr:
        raise Exception("출발역과 도착역이 같습니다.")
    
    try:
        input_date = datetime.strptime(args.date, "%Y%m%d")
        current_date = datetime.now()
        if input_date > current_date + timedelta(days=31):
            raise Exception("한달 이후의 날짜는 예약할 수 없습니다.")
    except ValueError:
        raise Exception("출발 날짜 형식을 다시 확인해주세요. YYYYMMDD 형식, 예: 20230115")
    
    if not re.match(r"^(0[0-9]|1[0-9]|2[0-2])$", args.time):
        raise Exception("출발 시간을 확인해주세요. 24시간 형식, 예: 08, 10, 12, ...22")

    if not args.std and not args.first:
        raise Exception("적어도 하나의 좌석 유형(일반석 또는 특실)을 선택해야 합니다.")

    if not str(args.trains).isdigit():
        raise Exception("확인할 기차 수는 숫자여야 합니다.")
    