import os
import streamlit as st
from Config import Config
from pathlib import Path
import base64

def menu():
  st.sidebar.page_link('./app.py', label='Trang chủ')
  st.sidebar.page_link('./pages/tong-quan.py', label='Tổng quan')
  st.sidebar.page_link('./pages/mo-hinh-du-doan.py', label='Mô hình dự đoán')
  st.sidebar.page_link('./pages/cach-hoat-dong.py', label='Cách hoạt động')
  st.sidebar.page_link('./pages/ket-qua.py', label='Kết quả')
  st.sidebar.page_link('./pages/lien-he.py', label='Liên hệ')


if __name__ == '__main__':
  st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

  def show():
    logo_path = Path("media/logo-giadinh_2362023923-removebg-preview.png")
    if logo_path.exists():
        logo_base64 = base64.b64encode(open(logo_path, "rb").read()).decode()
    else:
        logo_base64 = ""

    # HTML layout: logo left, title right
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: center;">
            <img src="data:image/png;base64,{logo_base64}" width="226" style="margin-right: 0px; margin-left: -40px;">
            <h1 style="text-align: center; font-size: 44px;">
                ỨNG DỤNG MÔ HÌNH HỌC MÁY SỬ DỤNG DẤU ẤN SINH HỌC ĐỂ DỰ ĐOÁN UNG THƯ VÚ DI CĂN XƯƠNG
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    
    st.markdown("---")
    
    # Statistics Section
    st.markdown("## Thống kê trên thế giới")
    col1, col2, col3 = st.columns([2, 2, 2])  # side padding columns

    with col1:
        st.metric("Số ca ung thư vú mới/năm", "2.3 triệu", label_visibility="visible")
        st.markdown(
            """
            <style>
            [data-testid="stMetricLabel"] p {
                font-size: 20px !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.metric("Tỷ lệ tiến triển di căn", "25%", label_visibility="visible")
        st.markdown(
            """
            <style>
            [data-testid="stMetricLabel"] p {
                font-size: 20px !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.metric("Tỷ lệ di căn xương", "70%", label_visibility="visible")
        st.markdown(
            """
            <style>
            [data-testid="stMetricLabel"] p {
                font-size: 20px !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    img_path = Path("media/graphic-asr-mort-both-sexes-in-2022-breast.png")
    # st.image(str(img_path), caption="Tỉ lệ mắc ung thư vú toàn cầu và Việt Nam", width=1000)

    if img_path.exists():
        img_base64 = base64.b64encode(open(img_path, "rb").read()).decode()
        st.markdown(
            f"""
            <div style="
                display: flex;
                justify-content: center;
                margin: 0 0 32px 0;
            ">
                <div style="
                    text-align: center;
                    border: 1px solid #ddd;
                    border-radius: 12px;
                    padding: 8px 0;
                    background-color: #FFFFFF;
                ">
                    <img src="data:image/png;base64,{img_base64}" style="border-radius: 8px;" width="1000">
                    <p style="font-size:18px; color:gray; margin-top: 6px;">Tỉ lệ tử vong do ung thư vú toàn cầu năm 2022, theo GLOBOCAN</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Hình ảnh chưa được thêm.")
    
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## Tính mới")
        st.markdown(
            '<p style="font-size:20px;">'
            "Nghiên cứu đầu tiên tại Việt Nam áp dụng học máy để dự đoán di căn xương ung thư vú dựa trên dấu ấn sinh học"
            '</p>',
            unsafe_allow_html=True
        )
        
        st.markdown("## Tính khoa học")
        st.markdown(
            '<p style="font-size:20px;">'
            "Sử dụng phương pháp nghiên cứu nghiêm ngặt, dữ liệu công khai có thể tái lập, và đánh giá trên các tập dữ liệu độc lập."
            '</p>',
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown("## Tính thực tiễn")
        st.markdown(
            '<p style="font-size:20px;">'
            "Cung cấp công cụ hỗ trợ giai đoạn lâm sàng, giúp bác sĩ xác định bệnh nhân nguy cơ cao cần theo dõi sát sao."
            '</p>',
            unsafe_allow_html=True
        )
        
        st.markdown("## Tính cộng đồng")
        st.markdown(
            '<p style="font-size:20px;">'
            "Tiềm năng giảm chi phí theo dõi, phát hiện sớm di căn, cải thiện chất lượng cuộc sống và tỷ lệ sống còn của bệnh nhân."
            '</p>',
            unsafe_allow_html=True
        )
    
    # st.markdown("### Giới thiệu dự án")
    # st.markdown("""
    # Nghiên cứu của chúng tôi phát triển một mô hình học máy sử dụng hai dấu ấn sinh học (PTPN11 và MICAL2) để dự đoán nguy cơ di căn xương ở bệnh nhân ung thư vú. Với độ chính xác AUC 0,774 và độ nhạy 77,8%, công cụ này có tiềm năng hỗ trợ phát hiện sớm và theo dõi bệnh nhân nguy cơ cao.
    # """)
    
    # col1, col2 = st.columns(2)
    # with col1:
    #     if st.button("Thử nghiệm công cụ dự đoán", key="home_calc"):
    #         st.session_state.page = "Công cụ dự đoán"
    #         st.rerun()
    
    # with col2:
    #     if st.button("Tìm hiểu thêm", key="home_overview"):
    #         st.session_state.page = "Tổng quan"
    #         st.rerun()

  show()
  menu()
  


  
