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
    st.title("Tổng quan về Ung thư Vú di căn Xương")
    st.markdown("---")

    # I. Ung thư vú di căn Xương là gì?
    st.markdown("## Ung thư Vú di căn Xương là gì?")
    st.markdown("""
<div style="
    font-size: 22px;
">
    Ung thư vú là tình trạng các tế bào vú phát triển bất thường, không kiểm soát được và hình thành khối u ác tính.
</div>
    """, unsafe_allow_html=True)

    # II. Tình hình trên thế giới và tại Việt Nam
    st.markdown("## Tình hình trên thế giới và tại Việt Nam:")

    img_path = Path("media/graphic-asr-inc-both-sexes-in-2022-breast.png")
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
                    <p style="font-size:18px; color:gray; margin-top: 6px;">Tỉ lệ mắc ung thư vú toàn cầu</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Hình ảnh chưa được thêm.")
    # if img_path.exists():
    #     img_base64 = base64.b64encode(open(img_path, "rb").read()).decode()
    #     st.markdown(
    #         f"""
    #         <div style="text-align: center;">
    #             <img src="data:image/png;base64,{img_base64}" width="1000">
    #             <p style="font-size:14px; color:gray;">Tỉ lệ mắc ung thư vú toàn cầu</p>
    #         </div>
    #         """,
    #         unsafe_allow_html=True
    #     )
    # else:
    #     st.info("Hình ảnh chưa được thêm.")

    st.markdown("""
    <div style="font-size:20px;">
      
      Ung thư vú là loại ung thư phổ biến thứ hai trên thế giới với hơn 2,2 triệu ca mới năm 2022, chiếm 11,5% tổng số ca mắc ở cả hai giới. Ở nữ giới, đây là ung thư phổ biến nhất, chiếm 23,8% tổng số ca mới. Ung thư vú gây hơn 666.000 ca tử vong, đứng thứ tư trong các loại ung thư gây tử vong toàn cầu.  
      
      
      
      Việt Nam ghi nhận 24.563 ca mắc ung thư vú mới, chiếm 28,9% tổng số ca ung thư ở nữ giới, đứng thứ 1 về số ca mắc ung thư ở nữ giới và cả hai giới, đưa ung thư vú trở thành bệnh lý ác tính có tỷ lệ mắc cao nhất, vượt qua cả ung thư gan và ung thư phổi.  

      
      
      Xu hướng ung thư vú ngày càng gia tăng, trẻ hóa và mức độ nguy hiểm cao của ung thư vú tại Việt Nam, đòi hỏi phải đẩy mạnh công tác tầm soát sớm và nâng cao nhận thức cộng đồng về phòng ngừa và điều trị kịp thời.
    </div>
    """, unsafe_allow_html=True)

    # III. Ung thư Vú di căn Xương
    st.markdown("## Ung thư Vú di căn Xương")
    st.markdown("""
    <div style="font-size:20px;">
      
      Tỷ lệ bệnh nhân được chẩn đoán ban đầu có di căn xương chiếm khoảng 3.6% trên tổng số bệnh nhân ung thư vú, nhưng trong nhóm bệnh nhân di căn thì di căn xương chiếm tới trên 60%.  

      Di căn xương thường gây ra các biến chứng nghiêm trọng như đau xương, gãy xương bệnh lý, chèn ép tủy sống, ảnh hưởng lớn đến chất lượng cuộc sống và tỷ lệ sống còn của bệnh nhân.
    </div>
    """, unsafe_allow_html=True)

    # IV. Các phương pháp phát hiện
    st.markdown("## Các phương pháp phát hiện")
    st.markdown("""
    <div style="font-size:20px;">
      
      Chẩn đoán ung thư vú di căn xương hiện nay dựa trên sự kết hợp của nhiều phương pháp hình ảnh như chụp cắt lớp vi tính (CT), chụp xạ hình xương, cộng hưởng từ (MRI), và PET/CT. Sinh thiết xương có thể được áp dụng để xác định chẩn đoán và đánh giá thụ thể phân tử khi cần thiết.  

      Tuy nhiên, phương pháp hình ảnh như chụp xạ hình xương có độ phân giải thấp và tỷ lệ dương tính giả cao, trong khi CT/MRI có thể bỏ lỡ các tổn thương nhỏ hoặc gặp khó khăn trong phân biệt lành tính và ác tính. PET/CT mặc dù hiệu quả nhưng có chi phí cao và khả năng tiếp cận hạn chế. Sinh thiết xương có tỷ lệ thất bại cao, thường cần thực hiện nhiều lần, gây đau cho bệnh nhân và mẫu thu được có thể không đại diện cho toàn bộ tổn thương.  

      Những hạn chế này dẫn đến nguy cơ chẩn đoán muộn hoặc không chính xác, ảnh hưởng đến hiệu quả điều trị. Phương pháp sử dụng dấu ấn sinh học trong chẩn đoán ung thư vú di căn xương dựa trên việc phát hiện các dấu ấn sinh học đặc hiệu trong máu, giúp nhận biết sớm di căn ít xâm lấn.  

      So với các phương pháp truyền thống, các chỉ thị sinh học có ưu điểm xét nghiệm đơn giản, nhanh, theo dõi được tiến triển bệnh và đánh giá hiệu quả điều trị. Tuy nhiên, các chỉ thị sinh học vẫn cần kết hợp với phương pháp khác để giúp bổ sung và hoàn thiện cho nhau, khắc phục những hạn chế của mỗi phương pháp khi được sử dụng riêng lẻ, tăng tính chính xác trong chẩn đoán và theo dõi ung thư vú di căn xương.
    </div>
    """, unsafe_allow_html=True)


show()
menu()
