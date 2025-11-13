import streamlit as st
from app import menu

from Config import Config

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

def show():
    st.title("Phụ lục: Kết luận, Kiến nghị và Thông tin bổ sung")

    st.markdown("---")
    st.markdown("## Kết luận và Kiến nghị")

    st.markdown("### Kết luận")
    st.markdown("""
    - Mô hình **Logistic Regression** sử dụng hai dấu ấn sinh học **PTPN11** và **MICAL2** đạt hiệu suất tốt trên tập dữ liệu độc lập (**AUC = 0,774**).
    - Cách tiếp cận đơn giản, dễ diễn giải và có tiềm năng ứng dụng trong thực tế lâm sàng.
    - Kết quả cho thấy khả năng phân loại sớm bệnh nhân **nguy cơ di căn xương** để theo dõi sát sao.
    """)

    st.markdown("### Kiến nghị")
    st.markdown("""
    - Xác thực mô hình trên **dữ liệu Việt Nam** và mở rộng kích thước mẫu.
    - Kết hợp thêm **yếu tố lâm sàng** (tuổi, giai đoạn, phân nhóm thụ thể) để cải thiện độ chính xác.
    - Phát triển **bộ công cụ xét nghiệm** tiêu chuẩn hóa để triển khai trong bệnh viện.
    - Nghiên cứu **theo dõi dọc** bệnh nhân nhằm đánh giá khả năng dự đoán sớm trong thực tế.
    """)

    st.markdown("---")
    st.markdown("## Giới thiệu nhóm nghiên cứu")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Thành viên")
        st.markdown("""
        - **Học sinh thực hiện:** Trần Nguyễn Anh Thoa, Trần Ngọc Khôi Nguyên  
        - **Giáo viên hướng dẫn:** ThS. Cao Hoài Đức  
        - **Trường:** Trường THPT Gia Định, TP. Hồ Chí Minh
        """)
    with col2:
        st.markdown("### Vai trò")
        st.markdown("""
        - Thu thập và tiền xử lý dữ liệu biểu hiện gen  
        - Phân tích, sàng lọc dấu ấn sinh học  
        - Xây dựng, huấn luyện và đánh giá mô hình  
        - Viết báo cáo và phát triển công cụ minh họa
        """)

    st.markdown("---")
    st.markdown("## Câu hỏi thường gặp (FAQ)")
    with st.expander("Công cụ này có dùng để chẩn đoán lâm sàng không?"):
        st.markdown("Không. Đây là **công cụ nghiên cứu** và chỉ mang tính tham khảo; không thay thế quyết định của bác sĩ.")
    with st.expander("AUC là gì và vì sao quan trọng?"):
        st.markdown("**AUC** đo lường khả năng mô hình phân biệt giữa hai nhóm. AUC cao hơn cho thấy phân loại tốt hơn.")
    with st.expander("Vì sao chọn PTPN11 và MICAL2?"):
        st.markdown("Hai gen này cho thấy **khả năng dự đoán ổn định** và có **cơ sở sinh học** liên quan đến cơ chế di căn.")
    with st.expander("Có thể áp dụng trên dữ liệu bệnh viện Việt Nam không?"):
        st.markdown("Có tiềm năng, nhưng cần **chuẩn hóa quy trình** và **xác thực** trên dữ liệu địa phương.")
    with st.expander("Mô hình có thể cải thiện thêm?"):
        st.markdown("Có. Bằng cách kết hợp thêm **yếu tố lâm sàng** và **dữ liệu đa trung tâm**.")

    st.markdown("---")
    st.markdown("## Tài liệu tham khảo")
    st.markdown("""
    1. Sung H, et al. (2021). Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries. *CA Cancer J Clin*. 71(3):209-249.  
    2. Coleman RE. (2006). Clinical features of metastatic bone disease and risk of skeletal morbidity. *Clin Cancer Res*. 12(20 Pt 2):6243s-6249s.  
    3. Brook N, et al. (2018). Breast Cancer Bone Metastases: Pathogenesis and Therapeutic Targets. *Nat Rev Endocrinol*. 14(6):341-354.  
    4. Kang Y, Pantel K. (2013). Tumor cell dissemination: emerging biological insights from animal models and cancer patients. *Cancer Cell*. 23(5):573-581.  
    5. Paik S, et al. (2004). A multigene assay to predict recurrence of tamoxifen-treated, node-negative breast cancer. *N Engl J Med*. 351(27):2817-2826.  
    6. van de Vijver MJ, et al. (2002). A gene-expression signature as a predictor of survival in breast cancer. *N Engl J Med*. 347(25):1999-2009.  
    7. Chan BKC. (2018). Data Analysis Using R Programming. *Adv Exp Med Biol*. 1082:47-122.  
    8. Araujo JM, et al. (2020). PTPN11 and oncogenesis. *Biochem Soc Trans*. 48(2):667-676.  
    9. Terman JR, Kashina A. (2013). Post-translational modification and regulation of actin. *Curr Opin Cell Biol*. 25(1):30-38.  
    10. Beadnell TC, et al. (2018). Roles of the MICAL Family of Proteins in Cancer. *J Mammary Gland Biol Neoplasia*. 23(1-2):15-26.  
    11. Hastie T, et al. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. Springer Series in Statistics.  
    12. Chen T, Guestrin C. (2016). XGBoost: A Scalable Tree Boosting System. *KDD '16: Proceedings of the 22nd ACM SIGKDD*.  
    13. Breiman L. (2001). Random Forests. *Machine Learning*. 45(1):5-32.  
    14. Cortes C, Vapnik V. (1995). Support-vector networks. *Machine Learning*. 20(3):273-297.  
    15. Hosmer DW, Lemeshow S. (2000). *Applied Logistic Regression*. 2nd ed. New York: John Wiley & Sons.  
    16. Barrett T, et al. (2013). NCBI GEO: archive for functional genomics data sets—update. *Nucleic Acids Res*. 41(D1):D991-D995.  
    17. Athar A, et al. (2019). ArrayExpress update – from bulk to single-cell expression data. *Nucleic Acids Res*. 47(D1):D711-D715.
    """)
    st.caption("Lưu ý: Phần tham khảo có thể được cập nhật thêm các DOI/PMID khi hoàn thiện bản báo cáo.")

    st.markdown("---")
    st.markdown("## Thuật ngữ y học")
    st.markdown("""
    - **Di căn xương (Bone metastasis):** Quá trình tế bào ung thư lan sang xương.  
    - **Biomarker (Dấu ấn sinh học):** Chỉ số sinh học có thể đo lường được, dùng để đánh giá tình trạng bệnh lý.  
    - **AUC (Area Under Curve):** Diện tích dưới đường cong ROC, đo lường khả năng phân biệt của mô hình.  
    - **Sensitivity (Độ nhạy):** Tỷ lệ phát hiện đúng các ca dương tính.  
    - **Specificity (Độ đặc hiệu):** Tỷ lệ phát hiện đúng các ca âm tính.  
    - **ROC Curve:** Đường cong đặc tính hoạt động thụ thể, dùng đánh giá mô hình phân loại.  
    - **Machine Learning (Học máy):** Lĩnh vực trí tuệ nhân tạo cho phép máy tính học từ dữ liệu.  
    - **Gene Expression (Biểu hiện gen):** Quá trình thông tin di truyền được chuyển từ DNA thành protein.  
    - **PTPN11:** Gen mã hóa enzyme SHP-2, tham gia nhiều con đường tín hiệu tế bào.  
    - **MICAL2:** Gen mã hóa enzyme tham gia tái cấu trúc bộ khung tế bào.  
    - **EMT (Epithelial-Mesenchymal Transition):** Quá trình chuyển đổi biểu mô-trung mô, quan trọng trong di căn ung thư.  
    - **Transcriptome:** Tập hợp tất cả các RNA được phiên mã trong tế bào.  
    - **Osteoclast:** Tế bào phá hủy xương.  
    - **Osteoblast:** Tế bào tạo xương.
    """)

show()
menu()