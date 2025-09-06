import streamlit as st
from datetime import date, timedelta

# 基本的な使い方
selected_date = st.date_input("好きな日付を選んでね")
st.write(f"選んだ日付: {selected_date}")

# デフォルト値と範囲の設定
today = date.today()
next_week = today + timedelta(days=7)
next_month = today + timedelta(days=30)

event_date = st.date_input(
    "イベントの日付はいつ？",
    value=next_week,  # 最初に表示される日付
    min_value=today,  # これより前の日付は選べないよ
    max_value=next_month  # これより後の日付は選べないよ
)
st.write(f"イベント日: {event_date}")