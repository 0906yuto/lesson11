import streamlit as st
import streamlit_calendar as st_calendar


event1={
    'id': '1', # イベントを識別するためのID。重複不可
    'title': 'Data Cloud World Tour', # イベント名
    'start': '2025-09-08T09:00:00', # 時間帯も指定する
    'end': '2025-09-08T20:00:00', # 時間帯も指定する
}
# calendarにはイベント一覧を配列にして渡す
event_list = [event1]

# options = {
#     'initialView': 'timeGridWeek',
# }

# イベントを表示するカレンダーを作成
cal = st_calendar.calendar(events=event_list)
st.write(cal)