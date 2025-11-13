import streamlit as st
import pandas as pd
from app import menu
from pathlib import Path
import base64
from Config import Config

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

def load_image_base64(path: Path):
    if path.exists():
        return base64.b64encode(open(path, "rb").read()).decode()
    return None


def show():
    st.title("Kết quả nghiên cứu")
    st.markdown("---")

    st.markdown("## Kết quả sàng lọc dấu ấn sinh học")
    
    st.markdown("""
    <span style="font-size:20px;">
    Sau quá trình phân tích và sàng lọc, chúng tôi xác định được 14 probeset đại diện cho <strong>10 genes</strong> có khả năng dự đoán di căn xương:
    </span>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    img1_path = Path("media/VENN2.png")
    img2_path = Path("media/VENN1.png")  # second image

    img1_base64 = base64.b64encode(open(img1_path, "rb").read()).decode() if img1_path.exists() else None
    img2_base64 = base64.b64encode(open(img2_path, "rb").read()).decode() if img2_path.exists() else None

    if img1_base64 and img2_base64:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <div style="display: inline-flex; justify-content: center; gap: 20px;">
                    <img src="data:image/png;base64,{img1_base64}" width="450">
                    <img src="data:image/png;base64,{img2_base64}" width="450">
                </div>
                <p style="font-size:18px; color:gray; margin-top: 0px;">
                    Giản đồ Venn thể hiện các probeset biểu hiện khác biệt chung giữa 
                    hai phương pháp DEGs và AUC
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Một hoặc cả hai hình ảnh chưa được thêm.")
    
    genes = ["NFYC", "CEP57", "CD44", "ABCC5", "TGFB1I1", "PTPN11", "SMARCA2", "MICAL2", "SLC36A1", "ZXDA"]

    cols = st.columns(5)
    for i, gene in enumerate(genes):
        with cols[i % 5]:
            if gene in ["PTPN11", "MICAL2"]:
                st.info(f"**{i+1}. {gene}**")
            else:
                st.markdown(f"**{i+1}. {gene}**", unsafe_allow_html=True)
    
    st.success("**Đặc biệt chú ý:** Hai gen **PTPN11** và **MICAL2** được xác định là các dấu ấn sinh học quan trọng nhất, có khả năng dự đoán cao và ổn định trên nhiều tập dữ liệu.")

    
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

    
    st.markdown("---")
    st.markdown("## So sánh hiệu suất các mô hình")
    
    st.markdown("Chúng tôi đã huấn luyện và so sánh 7 mô hình học máy khác nhau:")
    
    model_data = {
        "Mô hình": ["Logistic Regression", "SVM", "KNN", "XGBoost", "AdaBoost", "Random Forest", "Decision Tree"],
        "Tổ hợp gene tối ưu": ["PTPN11, MICAL2", "PTPN11, MICAL2", "ABCC5, TGFB1I1, PTPN11, SLC36A1", "ABCC5, TGFB1I1, SMARCA2, SLC36A1", "ABCC5, TGFB1I1, PTPN11, MICAL2, SLC36A1", "PTPN11, MICAL2", "MICAL2, NFYC, CD44"],
        "AUC Tập Kiểm Tra": [0.68, 0.66, 0.728, 0.659, 0.685, 0.746, 0.735],
        "AUC Tập Độc Lập": [0.774, 0.772, 0.758, 0.747, 0.723, 0.69, 0.686],
    }

    df = pd.DataFrame(model_data)
    # Increase overall font size in the dataframe
    st.dataframe(df.style.set_properties(**{'font-size': '22px'}), use_container_width=True)
    
    st.success("Mô hình **Logistic Regression** sử dụng 2 gen PTPN11 và MICAL2 đạt hiệu suất cao nhất trên tập dữ liệu độc lập (AUC = 0,774), đồng thời có ưu điểm là đơn giản, dễ giải thích và triển khai trong thực tế.")
    
    st.markdown("---")
    st.markdown("## Đánh giá chi tiết mô hình tối ưu")

    # Paths to your images
    violin_images = [
        Path("media/vioplot_test.png"),
        Path("media/vioplot_ex.png")
    ]

    roc_images = [
        Path("media/violin_square.png")
    ]

    conf_matrix_images = [
        Path("media/tapkiemtra.png"),
        Path("media/tapdoclap.png")
    ]

    # Create tabs
    st.markdown(
        """
        <style>
        /* Increase font size of tab labels */
        div[data-testid="stTabs"] button[role="tab"] {
            font-size: 24px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    tab1, tab2, tab3 = st.tabs(["Violin Plot", "Biểu đồ ROC và AUC", "Ma trận nhầm lẫn"])

    # --- Violin Plot Tab ---
    with tab1:
        images_base64 = [load_image_base64(p) for p in violin_images]
        if all(images_base64):
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <div style="display: inline-flex; justify-content: center; gap: 20px;">
                        <img src="data:image/png;base64,{images_base64[0]}" width="400">
                        <img src="data:image/png;base64,{images_base64[1]}" width="400">
                    </div>
                    <p style="font-size:18px; color:gray; margin-top: 20px;">
                        Biểu đồ Violin thể hiện sự khác biệt về điểm nguy cơ di căn xương giữa hai nhóm di căn và không di căn xương ở hai tập dữ liệu
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.info("Một hoặc cả hai hình ảnh Violin Plot chưa được thêm.")

    # --- ROC and AUC Tab ---
    with tab2:
        img_base64 = load_image_base64(roc_images[0])
        if img_base64:
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_base64}" width="400">
                    <p style="font-size:14px; color:gray; margin-top: 10px;">
                        Đường cong ROC thể hiện khả năng dự đoán di căn xương ở bệnh nhân ung thư vú trên hai tập dữ liệu kiểm tra và độc lập
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.info("Hình ảnh ROC/AUC chưa được thêm.")

    # --- Confusion Matrix Tab ---
    with tab3:
        images_base64 = [load_image_base64(p) for p in conf_matrix_images]
        if all(images_base64):
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <div style="display: inline-flex; justify-content: center; gap: 20px;">
                        <img src="data:image/png;base64,{images_base64[0]}" width="350">
                        <img src="data:image/png;base64,{images_base64[1]}" width="350">
                    </div>
                    <p style="font-size:14px; color:gray; margin-top: 10px;">
                        Ma trận nhầm lẫn của tập kiểm tra và tập độc lập
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.info("Một hoặc cả hai hình ảnh ma trận nhầm lẫn chưa được thêm.")
    
    st.markdown("### Chỉ số hiệu suất trên tập độc lập")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("AUC", "0.774", "9% so với tập kiểm tra")
    with col2:
        st.metric("Độ chính xác", "71.5%", "8.9% so với tập kiểm tra")
    with col3:
        st.metric("Độ nhạy", "77.8%", "12.8% so với tập kiểm tra")
    with col4:
        st.metric("Độ đặc hiệu", "65.2%", "8.5% so với tập kiểm tra")
    
    
    st.markdown("### Sự cải thiện của mô hình")
    st.markdown("""
    <ul style="font-size:20px;">
        <li>AUC tăng từ 0,69 (tập kiểm tra) lên 0,774 (tập độc lập)</li>
        <li>Độ nhạy 77,8% đảm bảo phát hiện được phần lớn ca di căn</li>
        <li>Mô hình ổn định và tổng quát tốt trên dữ liệu mới</li>
    </ul>
    """, unsafe_allow_html=True)

show()
menu()