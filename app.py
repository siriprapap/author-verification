import streamlit as st

# โหลด CSS จากไฟล์แยก
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🖋️ แอปตัวอย่าง CSS แยกไฟล์")
st.write("ทดสอบการแสดงผลด้วยฟอนต์และปุ่มที่กำหนดไว้ใน styles.css")

if st.button("คลิกฉัน"):
    st.success("🎉 คุณกดปุ่มแล้ว!")
