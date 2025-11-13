import streamlit as st
import numpy as np
from app import menu
from Config import Config
import math

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

# Logistic regression parameters
a1 = -0.3554353
a2 = 0.4351188
b = -0.1538520
cutoff = 0.5007

def logistic_regression_predict(ptpn11, mical2):
    z = a1 * ptpn11 + a2 * mical2 + b
    p = 1 / (1 + math.exp(-z))
    prediction = 1 if p >= cutoff else 0
    return p, prediction


def show():
    st.markdown("# Mô hình dự đoán nguy cơ di căn xương")
    st.markdown('<p style="font-size:20px;">Nhập giá trị biểu hiện gene để dự đoán nguy cơ di căn xương ở bệnh nhân ung thư vú</p>', unsafe_allow_html=True)
    # st.markdown('<p style="font-size:20px;">---</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    ###
    st.markdown("## Công cụ dự đoán nguy cơ di căn xương")
    st.write('<p style="font-size:20px;">Nhập giá trị biểu hiện gene để dự đoán nguy cơ di căn xương ở bệnh nhân ung thư vú</p>', unsafe_allow_html=True)

    # Input gene expressions via text input
    ptpn11_input = st.number_input("Biểu hiện gene PTPN11 đã chuẩn hóa Z-score", min_value=-100.0, max_value=100.0, value=0.123456789, step=0.1, format="%.9f")
    st.caption("Protein Tyrosine Phosphatase Non-receptor Type 11")

    mical2_input = st.number_input("Biểu hiện gene MICAL2 đã chuẩn hóa Z-score", min_value=-100.0, max_value=100.0, value=0.123456789, step=0.1, format="%.9f")
    st.caption("Molecule Interacting with CasL 2")

    risk_score, prediction = logistic_regression_predict(ptpn11_input, mical2_input)

    st.markdown("### Kết quả dự đoán")
    color = "#10B981"
    risk_level = "Bình thường"
    recommendation = "Lịch trình kiểm tra cơ bản"

    if risk_score >= 0.5682:
        color = "#DC2626"
        risk_level = "Mắc bệnh"
        recommendation = "Kiểm tra xương nâng cao và theo dõi sát sao"

    st.markdown(f"""
    <div style="background: {color}; padding: 20px; border-radius: 12px; color: white; font-weight: bold; font-size: 24px; text-align:center;">
    {risk_level}
    </div>
    """, unsafe_allow_html=True)
    ###

    st.warning("""
    **⚠️ Lưu ý quan trọng:** Đây là công cụ nghiên cứu và chỉ mang tính chất tham khảo. 
    Không thể thay thế chẩn đoán lâm sàng của bác sĩ. Kết quả cần được đánh giá kết hợp với 
    các yếu tố lâm sàng, hình ảnh học và xét nghiệm khác.
    """)
    
    # st.markdown('<p style="font-size:20px;">---</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("## Câu hỏi thường gặp")
    
    with st.expander("Làm thế nào để đo biểu hiện gen?"):
        st.markdown("""
        <p style="font-size:18px;">
        Biểu hiện gene được đo bằng các kỹ thuật như RT-PCR, microarray, hoặc RNA sequencing 
        từ mẫu máu hoặc mô u. Giá trị thường được chuẩn hóa theo thang điểm để so sánh.
        </p>
        """, unsafe_allow_html=True)
    
    with st.expander("Ngưỡng tối ưu được xác định như thế nào?"):
        st.markdown("""
        <p style="font-size:18px;">
        Ngưỡng được tối ưu hóa dựa trên phân tích đường cong ROC, cân bằng giữa độ nhạy 
        và độ đặc hiệu để đạt hiệu suất tổng thể tốt nhất trên tập huấn luyện.
        </p>
        """, unsafe_allow_html=True)
    
    with st.expander("Nguy cơ cao có nghĩa là chắc chắn sẽ di căn?"):
        st.markdown("""
        <p style="font-size:18px;">
        Không. "Nguy cơ cao" chỉ nghĩa là xác suất di căn cao hơn trung bình, không phải 
        chắc chắn. Nhiều yếu tố khác như điều trị, thể trạng bệnh nhân cũng ảnh hưởng 
        đến kết quả thực tế.
        </p>
        """, unsafe_allow_html=True)

show()
menu()