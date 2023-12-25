# SRT 예약 자동화 시스템

이 프로젝트는 한국의 고속철도인 SRT의 티켓 예약을 자동화하는 파이썬 기반 CLI(Command Line Interface) 어플리케이션입니다.

## 시작하기

본 프로그램은 Python 3으로 작성되었습니다.

사용하기 전에 Python 3가 설치되어 있는지 확인하세요.

### 설치 방법

1. 먼저, 이 리포지토리를 클론하거나 다운로드합니다.

   ```
   git clone [your-repository-url]
   ```

2. 필요한 패키지들을 설치합니다.
   ```
   pip3 install -r requirements.txt
   ```

### 사용 방법

SRT 공식 웹사이트의 사용자 로그인 ID와 비밀번호가 필요합니다.

프로그램을 실행하기 위해, 다음과 같은 명령어를 사용합니다:

```
python3 quickstart.py --userid [사용자ID] --pwd [비밀번호] --dep [출발역] --arr [도착역] --date [출발 날짜] --time [출발 시간] --std --first --trains [확인 기차 수] --waitlist --no-alert
```

## 주요 인자 설명

### 필수 인자

- `--userid`: 사용자 ID (예: `1234567890`)
- `--pwd`: 비밀번호
- `--dep`: 출발역. 선택 가능한 역: 수서, 동탄 등
- `--arr`: 도착역. 선택 가능한 역: 부산, 동대구 등
- `--date`: 출발 날짜 (YYYYMMDD, 최대 한 달 내)
- `--time`: 출발 시간 (24시간 형식, 예: `00`, `02`, `04`, ... `22`)
- `--std`: 일반실 예약 (기본값: False)
- `--first`: 특실 예약 (기본값: False)

일반실과 특실 중 적어도 하나는 필수 선택. 둘다 선택시 일반실 우선 순위.

선택 가능한 역: 수서, 동탄, 평택지제, 곡성, 공주, 광주송정, 구례구, 김천(구미), 나주, 남원, 대전, 동대구, 마산, 목포, 밀양, 부산, 서대구, 순천, 신경주, 여수EXPO, 여천, 오송, 울산(통도사), 익산, 전주, 정읍, 진영, 진주, 창원, 창원중앙, 천안아산, 포항

### 선택 인자

- `--trains`: 확인할 기차 수 (기본값: 3)
- `--waitlist`: 예약대기 사용 여부 (기본값: False)
- `--no-alert`: 알림 비활성화 (기본값: False)

## 예시

1. **일반실 예약, 기본 설정**:

   ```
   python3 quickstart.py --userid 1234567890 --pwd mypassword --dep 수서 --arr 부산 --date 20230115 --time 10 --std
   ```

   수서에서 부산까지 2023년 1월 15일 10시에 출발하는 일반실을 예약합니다.

2. **특실 예약, 알림 비활성화**:

   ```
   python3 quickstart.py --userid 9876543210 --pwd anotherpassword --dep 동탄 --arr 동대구 --date 20230220 --time 14 --first --no-alert
   ```

   동탄에서 동대구까지 2023년 2월 20일 14시에 출발하는 특실을 예약합니다. 예약 시 알림이 비활성화됩니다.

3. **일반실 및 특실 예약 확인, 추가 기차 확인**:

   ```
   python3 quickstart.py --userid 1122334455 --pwd yetanotherpwd --dep 전주 --arr 서울 --date 20230310 --time 16 --std --first --trains 5
   ```

   전주에서 서울까지 2023년 3월 10일 16시에 출발합니다. 일반실과 특실 중 가능한 좌석을 우선적으로 예약합니다. 일반실이 우선적으로 확인됩니다.

4. **일반실 예약, 예약 대기 사용**:

   ```
   python3 quickstart.py --userid 5566778899 --pwd newpassword --dep 광주송정 --arr 대전 --date 20230415 --time 09 --std --waitlist
   ```

   광주송정에서 대전까지 2023년 4월 15일 9시에 출발하는 일반실을 예약합니다. 예약이 불가능할 경우 예약 대기를 활성화합니다.

## 기능

이 프로그램은 다음과 같은 기능을 제공합니다:

- 사용자 로그인
- 기차 검색 및 예약
- 좌석 유형 선택 (일반석/특실)
- 예약 대기 기능
- 예약 성공 시 알림

## 실행 결과

![hello](/img/img1.png){ width=200px height=150px }

![image1](/img/img1.png)![image2](/img/img2.png)

## 문의 및 기능 제안

버그 신고, 문제점 제기 또는 새로운 기능에 대한 제안이 있으시다면, 언제든지 <Haksoo.j.kim@gmail.com> 으로 연락 주시기 바랍니다. 사용자 여러분의 의견을 듣고 프로젝트를 개선하는 데 큰 도움이 됩니다.

## 개발자 및 기여자 정보

본 프로젝트는 [kminito](https://github.com/kminito/srt_reservation)의 SRT 예약 시스템 코드를 기반으로 하여 재구성 및 개선되었습니다.

## 라이센스

[LICENSE](/LICENSE) 파일을 참조하세요.
