import streamlit as st
import numpy as np
from app import menu
from ui import apply_global_styles
from Config import Config
import math

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

apply_global_styles()

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

    with st.form(key="prediction_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            ptpn11_input = st.number_input(
                "Biểu hiện gene PTPN11 đã chuẩn hóa Z-score",
                min_value=-10.0, max_value=10.0, value=0.12, step=0.01, format="%.9f"
            )
            st.caption("Protein Tyrosine Phosphatase Non-receptor Type 11")
        with col_b:
            mical2_input = st.number_input(
                "Biểu hiện gene MICAL2 đã chuẩn hóa Z-score",
                min_value=-10.0, max_value=10.0, value=0.12, step=0.01, format="%.9f"
            )
            st.caption("Molecule Interacting with CasL 2")
        submitted = st.form_submit_button(label="Tính toán")

    risk_score = None
    prediction = None
    if submitted:
        risk_score, prediction = logistic_regression_predict(ptpn11_input, mical2_input)

    st.markdown("### Kết quả dự đoán")
    if risk_score is not None:
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
    else:
        st.info("Nhập thông số và bấm 'Tính toán' để xem kết quả.")
    ###

    st.warning("""
    **⚠️ Lưu ý quan trọng:** Đây là công cụ nghiên cứu và chỉ mang tính chất tham khảo. 
    Không thể thay thế chẩn đoán lâm sàng của bác sĩ. Kết quả cần được đánh giá kết hợp với 
    các yếu tố lâm sàng, hình ảnh học và xét nghiệm khác.
    """)

    st.markdown("---")
    st.markdown("### Mô hình 3D Cấu trúc Protein")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("PTPN11 (Protein Tyrosine Phosphatase Non-receptor type 11) giữ một vai trong việc điều hòa các con đường truyền tín hiệu nội bào. Gene này mã hóa enzyme SHP2, hoạt động như một trạm trung chuyển tín hiệu, giúp kiểm soát các quá trình sống còn của tế bào như tăng trưởng, phân chia, biệt hóa và di chuyển.")
        html_code_1 = """
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://molstar.org/viewer/molstar.js"></script>
            <style>
                body {
                    margin: 0;
                    background: #f8f9fa;
                }
                #molstar {
                    width: 100%;
                    height: 500px;
                }
            </style>
        </head>
        <body>
            <div id="molstar"></div>
            <script>
                molstar.Viewer.create(
                    document.getElementById('molstar'),
                    {
                        layoutShowControls: false,
                        layoutShowSequence: false,
                        layoutShowRightPanel: false
                    }
                ).then(viewer => {
                    viewer.loadStructureFromUrl(
                        'https://files.rcsb.org/download/8WX7.cif',
                        'mmcif'
                    );
                });
            </script>
        </body>
        </html>
        """
        st.components.v1.html(html_code_1, height=500)
        st.markdown("Ma, C., Kang, D., Gao, P., Zhang, W., Wu, X., Xu, Z., Han, H., Zhang, L., Cai, Y., Wang, Y., Wang, Y., Long, W., Crystal structure of SHP2 in complex with JAB-3186 (2024) https://doi.org/10.2210/pdb8wx7/pdb")

    with col2:
        st.markdown("MICAL2 (Molecule Interacting with CasL 2) là một enzyme có khả năng phá vỡ cấu trúc bên trong tế bào. Sự thay đổi này làm cho tế bào dễ dàng thay đổi hình dạng và di chuyển hơn.")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        html_code_2 = """
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://molstar.org/viewer/molstar.js"></script>
            <style>
                body {
                    margin: 0;
                    background: #f8f9fa;
                }
                #molstar {
                    width: 100%;
                    height: 500px;
                }
            </style>
        </head>
        <body>
            <div id="molstar"></div>
            <script>
                molstar.Viewer.create(
                    document.getElementById('molstar'),
                    {
                        layoutShowControls: false,
                        layoutShowSequence: false,
                        layoutShowRightPanel: false
                    }
                ).then(viewer => {
                    viewer.loadStructureFromUrl(
                        'https://files.rcsb.org/download/2E9K.cif',
                        'mmcif'
                    );
                });
            </script>
        </body>
        </html>
        """
        st.components.v1.html(html_code_2, height=500)
        st.markdown("Tomizawa, T., Tochio, N., Koshiba, S., Watanabe, S., Harada, T., Kigawa, T., Yokoyama, S., Solution structure of the CH domain from human MICAL-2 (deposited year unknown) https://doi.org/10.2210/pdb2e9k/pdb")
    
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

    st.markdown("""
        <div style="text-align: center; margin-top: 32px; color: #567; font-size: 0.9em;">
            <p>© 2025 Nhóm Nghiên Cứu - Trường THPT Gia Định</p>
        </div>
    """, unsafe_allow_html=True)

show()
menu()