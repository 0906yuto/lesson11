import streamlit as st
import streamlit_calendar as st_calendar

date=st.date_input("始めの日付")
time=st.time_input("始めの時間")
hiduke=st.date_input("終わりの日付")
zikan=st.time_input("終わりの時間")
event1={
    'id': '1', # イベントを識別するためのID。重複不可
    'title': 'Data Cloud World Tour', # イベント名
    'start': f'{date}T{time}', # 時間帯も指定する
    'end': f'{hiduke}T{zikan}', # 時間帯も指定する
}
# calendarにはイベント一覧を配列にして渡す
event_list = [event1]

# options = {
#     'initialView': 'timeGridWeek',
# }

# イベントを表示するカレンダーを作成
cal = st_calendar.calendar(events=event_list)
st.write(cal)