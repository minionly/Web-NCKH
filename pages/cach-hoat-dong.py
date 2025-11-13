import streamlit as st
from app import menu
from Config import Config
from pathlib import Path
import base64

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
)

def show():
    st.title("Cách hoạt động")
    st.markdown("---")

    st.markdown("##  Dấu ấn sinh học tiềm năng")
    st.markdown("""
<div style="font-size:20px;">

Dấu ấn sinh học là các đặc điểm trong cơ thể, như gen, protein hoặc các phân tử khác, có thể đo lường được để chỉ ra một tình trạng sinh học cụ thể, ví dụ như một bệnh lý hoặc phản ứng của cơ thể với điều trị. Chúng đóng vai trò quan trọng trong việc chẩn đoán, sàng lọc, theo dõi và lựa chọn phương pháp điều trị tối ưu cho bệnh, đặc biệt là trong lĩnh vực ung thư.

Việc tích hợp các mô hình học máy với dữ liệu dấu ấn sinh học (biomarkers) đã tạo ra một bước tiến đáng kể trong lĩnh vực chẩn đoán sớm ung thư. Dấu ấn sinh học, bao gồm các thông số di truyền, protein, chuyển hóa hoặc các đặc điểm hình ảnh y tế, thường tạo thành các tập dữ liệu có tính chiều cao (high-dimensional) và chứa nhiều nhiễu, vượt quá khả năng phân tích chính xác của các phương pháp thống kê truyền thống. 

Trong bối cảnh này, mô hình học máy đóng vai trò là công cụ phân tích mạnh mẽ để xử lý, sàng lọc và tối ưu hóa các dấu ấn sinh học tiềm năng. Sự kết hợp này cho phép xây dựng các hệ thống chẩn đoán ít hoặc không xâm lấn, có khả năng phát hiện bệnh trước khi các triệu chứng lâm sàng rõ rệt, từ đó nâng cao đáng kể tỷ lệ sống sót và hiệu quả điều trị.
</div>
    """, unsafe_allow_html=True)

    st.markdown("## Mô hình học máy dự đoán bệnh")
    st.markdown("""
<div style="font-size:20px;">


  Học máy (Machine Learning - ML), một phân ngành quan trọng của Trí tuệ Nhân tạo (Artificial Intelligence - AI), tập trung vào việc phát triển các thuật toán cho phép hệ thống máy tính cải thiện hiệu suất thông qua việc học từ từ dữ liệu đầu vào, mà không cần lập trình cụ thể. 

  Chức năng cốt lõi của học máy là tự động hóa quá trình rút trích đặc trưng, phân loại và dự đoán, từ đó tạo ra cơ sở cho việc ra quyết định dựa trên bằng chứng trong nhiều lĩnh vực khoa học và kỹ thuật khác nhau.
</div>
    """, unsafe_allow_html=True)
    
    img_path = Path("media/13195_2023_1304_Fig2_HTML.png")
    if img_path.exists():
        img_base64 = base64.b64encode(open(img_path, "rb").read()).decode()
        st.markdown(
            f"""
            <div style="
                display: flex;
                justify-content: center;
                margin: 16px 0 32px 0;
            ">
                <div style="
                    text-align: center;
                    border: 1px solid #ddd;
                    border-radius: 12px;
                    padding: 8px 0;
                    background-color: #FFFFFF;
                ">
                    <img src="data:image/png;base64,{img_base64}" style="border-radius: 8px;" width="1000">
                    <p style="font-size:18px; color:gray; margin-top: 12px;">Sơ đồ minh họa quy trình nghiên cứu</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Hình ảnh chưa được thêm.")


show()
menu()
