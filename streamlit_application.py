import streamlit as st
import streamlit_calendar as st_calendar
if 'count'not in st.session_state:
    st.session_state.count=0
if 'event_list' not in st.session_state:
    st.session_state.event_list=["0"]
def event(y,d,t,h,z):
    event_x={
        'id': f'{st.session_state.count}', # イベントを識別するためのID。重複不可
        'title': y, # イベント名
        'start': f'{d}T{t}', # date time
        'end': f'{h}T{z}', # hiduke zikan
    }
    if st.session_state.count==0:
        st.session_state.event_list[st.session_state.count]=event_x
    else:
        st.session_state.event_list.append(event_x)
yotei=st.text_input("予定の名前")
date=st.date_input("始めの日付")
time=st.time_input("始めの時間")
hiduke=st.date_input("終わりの日付")
zikan=st.time_input("終わりの時間")

# calendarにはイベント一覧を配列にして渡す

# options = {
#     'initialView': 'timeGridWeek',
# }
if st.button("予定を更新"):
    event(yotei,date,time,hiduke,zikan)
    st.session_state.count += 1
    st.success("予定を更新しました")
# イベントを表示するカレンダーを作成
cal = st_calendar.calendar(events=st.session_state.event_list)
st.write(cal)