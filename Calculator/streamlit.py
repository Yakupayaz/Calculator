import streamlit as st

st.title("Hesap Makinesi")

def hesap_makinesi(a, b, işlem):
    if işlem == "Toplam":
        return a + b
    elif işlem == "Çıkarma":
        return abs(a - b)  
    elif işlem == "Çarpma":
        return a * b
    elif işlem == "Bölme":
        if b != 0:
            return a / b
        else:
            return "Sonuç tanımsız"
    elif işlem =="Kök":
        return 

işlem = st.selectbox("İşlemi seçin:", ["Toplam", "Çıkarma", "Çarpma", "Bölme"])
a = st.number_input("Birinci sayıyı girin:")
b = st.number_input("İkinci sayıyı girin:")

if st.button("Hesapla"):
    sonuç = hesap_makinesi(a, b, işlem)
    st.write(f"Sonuç: {sonuç}")