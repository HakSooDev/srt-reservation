import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from audioplayer import AudioPlayer

class SRT:
    def __init__(self, args):
        # 사용자 인증 정보
        self.user_id = args.userid
        self.pwd = args.pwd
    
        # 여정 정보
        self.dep = args.dep
        self.arr = args.arr
        self.date = args.date
        self.time = args.time

        # 좌석 유형
        self.std = args.std
        self.first = args.first

        # 추가 옵션
        self.trains = int(args.trains)
        self.waitlist = args.waitlist
        self.alert = not args.no_alert

        self.driver = None
        self.is_booked = False  # 예약 완료 되었는지 확인용
        self.cnt_refresh = 0  # 새로고침 회수 기록

    def run_driver(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)

            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(10)

            self.driver = driver
        except WebDriverException as e:
            raise Exception("크롬을 찾을 수 없습니다. 크롬을 설치해주세요.")

    def login(self):
        self.driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
        self.driver.find_element(By.ID, 'srchDvNm01').send_keys(str(self.user_id))
        self.driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(str(self.pwd))
        self.driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()

    def check_login(self):
        print("로그인 확인 중")
        try:
            # 환영하세요 텍스트가 나올 때까지 기다림
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.login_wrap > span"), "환영합니다")
            )
            print("로그인 성공")
        except Exception as e:
            raise Exception("로그인 실패. 아이디와 비밀번호를 확인해주세요.")

    def go_search(self):
        # 기차 조회 페이지로 이동
        self.driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')

        # 출발지 입력
        elm_dpt_stn = self.driver.find_element(By.ID, 'dptRsStnCdNm')
        elm_dpt_stn.clear()
        elm_dpt_stn.send_keys(self.dep)

        # 도착지 입력
        elm_arr_stn = self.driver.find_element(By.ID, 'arvRsStnCdNm')
        elm_arr_stn.clear()
        elm_arr_stn.send_keys(self.arr)

        # 출발 날짜 입력
        elm_dpt_dt = self.driver.find_element(By.ID, "dptDt")
        select_elm_dpt_dt = Select(elm_dpt_dt)
        select_elm_dpt_dt.select_by_value(self.date)

        # 출발 시간 입력
        elm_dpt_tm = self.driver.find_element(By.ID, "dptTm")
        self.driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dpt_tm)
        Select(self.driver.find_element(By.ID, "dptTm")).select_by_visible_text(self.time)

        print("기차를 조회합니다")
        print(f"출발역:{self.dep} , 도착역:{self.arr}\n날짜:{self.date}, 시간: {self.time}시 이후\n{self.trains}개의 기차 중 예약")
        if self.std and self.first:
            print("좌석 유형: 일반석 + 특실")
        elif self.std:
            print("좌석 유형: 일반석")
        elif self.first:
            print("좌석 유형: 특실")
        print(f"예약대기 사용 여부: {self.waitlist}")
        print(f"알림재생 여부: {self.alert}")

        self.driver.find_element(By.XPATH, "//input[@value='조회하기']").click()

    def book_ticket(self, seat_td_element):        
        if "예약하기" in seat_td_element.text:
            print("예약 가능 클릭")
            
            book_anchor = seat_td_element.find_element(By.TAG_NAME, "a")
            self.driver.execute_script("arguments[0].click();", book_anchor)

            # 예약이 성공하면
            if self.driver.find_elements(By.ID, 'isFalseGotoMain'):
                self.is_booked = True
                print("예약 성공")

                if(self.alert):
                    self.play_sound()
            else:
                print("잔여석 없음. 다시 검색")
                self.driver.back()  # 뒤로가기
    

    def refresh_result(self):
        submit = self.driver.find_element(By.XPATH, "//input[@value='조회하기']")
        self.driver.execute_script("arguments[0].click();", submit)
        self.cnt_refresh += 1
        print(f"새로고침 {self.cnt_refresh}회")
        time.sleep(0.5)

    def reserve_ticket(self, reservation_element):
        if "신청하기" in reservation_element.text:
            print("예약 대기 완료")

            reserve_anchor = reservation_element.find_element(By.TAG_NAME, "a")
            self.driver.executae_script("arguments[0].click();", reserve_anchor)

            self.play_sound()

            self.is_booked = True
            return 

    def check_result(self):
        while not self.is_booked:
            for i in range(1, self.trains + 1):
                try:
                    first_seat_elm = self.driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(6)")
                    standard_seat_elm = self.driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)")
                    reservation_elm = self.driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(8)")
                except Exception:
                    raise Exception("조회 결과가 없습니다. 조회 조건을 변경해주세요.")

                if self.std:
                    self.book_ticket(standard_seat_elm)
                
                if self.first:
                    self.book_ticket(first_seat_elm)

                if self.waitlist:
                    self.reserve_ticket(reservation_elm)

                if self.is_booked:
                    break 
                else:
                    time.sleep(randint(2, 4))
                    self.refresh_result()

    def play_sound(self):
        AudioPlayer("./sound.mp3").play(block=True)


    def run(self):
        self.run_driver()
        self.login()
        self.check_login()
        self.go_search()
        self.check_result()


