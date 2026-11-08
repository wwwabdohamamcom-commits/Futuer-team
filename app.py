import streamlit as st
import requests

st.set_page_config(page_title="FUTUER TEAM", page_icon="🚀", layout="centered")

st.title("🚀 FUTUER TEAM")
st.subheader("Smart Fault Detection System")

st.divider()

st.header("📲 Telegram تنبيهات")

bot_token = st.text_input("Telegram Bot Token", type="password")
chat_id = st.text_input("Chat ID")
message = st.text_area("رسالة التنبيه", value="تم اكتشاف عطل في النظام :FUTUER TEAM ⚠️")

if st.button("إرسال التنبيه إلى Telegram"):
    if bot_token and chat_id:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                st.success("تم إرسال التنبيه بنجاح! 🚀")
            else:
                st.error(f"فشل الإرسال. التأكد من البيانات: {response.text}")
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال: {e}")
    else:
        st.warning("يرجى إدخال Bot Token و Chat ID أولاً.")

st.divider()
st.caption("FUTUER TEAM | Electronics Engineering | Smart Fault Detection System")
