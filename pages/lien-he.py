import streamlit as st
from app import menu
from Config import Config

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

def show():
    st.markdown("""
        <style>
            .contact-header {
                text-align: center;
                margin-bottom: 40px;
            }
            .contact-header h1 {
                color: #000000;
                # font-size: 2.0em;
                # margin-bottom: 10px;
            }
            .contact-header p {
                color: #000000;
                font-size: 1.1em;
            }
            .team-container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 24px;
                margin-top: 30px;
            }
            .team-card {
                background: white;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.08);
                padding: 24px;
                text-align: center;
                transition: transform 0.3s, box-shadow 0.3s;
                border: 1px solid #E6E8EA;
            }
            .team-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 20px rgba(0,0,0,0.12);
            }
            .team-card-image {
                width: 120px;
                height: 120px;
                margin: 0 auto 16px;
                border-radius: 50%;
                background: linear-gradient(135deg, #0066CC, #00AA66);
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 48px;
                font-weight: bold;
            }
            .team-card-name {
                font-size: 1.3em;
                font-weight: 700;
                color: #000000;
                margin-bottom: 4px;
            }
            .team-card-role {
                font-size: 0.95em;
                color: #000000;
                font-weight: 600;
                margin-bottom: 14px;
            }
            .team-card-divider {
                height: 2px;
                background: #E6E8EA;
                margin: 14px 0;
            }
            .team-card-contact {
                font-size: 0.9em;
                color: #567;
                margin-bottom: 8px;
            }
            .team-card-contact-label {
                font-weight: 600;
                color: #1A1A1A;
            }
            .category-title {
                font-size: 1.5em;
                font-weight: 700;
                color: #000000;
                margin-top: 32px;
                margin-bottom: 18px;
                border-left: 4px solid #00AA66;
                padding-left: 12px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="contact-header">
            <h1>Liên Hệ Với Chúng Tôi</h1>
            <p>Nhóm nghiên cứu về Xây dựng mô hình học máy sử dụng dấu ấn sinh học để dự đoán ung thư vú di căn xương</p>
        </div>
    """, unsafe_allow_html=True)

    # Team data
    team_members = [
        {
            "category": "Học sinh",
            "name": "Trần Nguyễn Anh Thoa",
            "role": "Lớp 12CTin trường THPT Gia Định",
            "phone": "0909 418 823",
            "email": "anhthoa7128@gmail.com",
            "initials": "AT"
        },
        {
            "category": "Học sinh",
            "name": "Trần Ngọc Khôi Nguyên",
            "role": "Lớp 12CTin trường THPT Gia Định",
            "phone": "0896 497 400",
            "email": "nguyenngockhoitran@email.com",
            "initials": "KN"
        },
        {
            "category": "Giáo viên",
            "name": "ThS. Cao Hoài Đức",
            "role": "Giáo viên hướng dẫn",
            "phone": "0834 501 020",
            "email": "Hoaiducsn@gmail.com",
            "initials": "CD"
        },
        {
            "category": "Cố vấn khoa học",
            "name": "TS. Nguyễn Minh Nam",
            "role": "Trưởng Bộ môn Kỹ thuật Y sinh – Trường Đại học Khoa học Sức Khoẻ, Đại học Quốc gia Thành phố Hồ Chí Minh",
            "phone": "0904 972 804",
            "email": "nmnam@uhsvnu.edu.vn",
            "initials": "MN"
        },
        {
            "category": "Cố vấn khoa học",
            "name": "KS. Ngô Ngọc Hải",
            "role": "Genetics Data",
            "phone": "0329 407 417",
            "email": "ngongochai2202003@gmail.com",
            "initials": "NH"
        }
    ]

    # Group by category
    students = [m for m in team_members if m["category"] == "Học sinh"]
    teacher = [m for m in team_members if m["category"] == "Giáo viên"]
    advisors = [m for m in team_members if m["category"] == "Cố vấn khoa học"]

    # Students section
    st.markdown('<div class="category-title"> Học sinh thực hiện</div>', unsafe_allow_html=True)
    cols = st.columns(len(students))
    for idx, member in enumerate(students):
        with cols[idx]:
            st.markdown(f"""
                <div class="team-card">
                    <div class="team-card-image">{member['initials']}</div>
                    <div class="team-card-name">{member['name']}</div>
                    <div class="team-card-role">{member['role']}</div>
                    <div class="team-card-divider"></div>
                    <div class="team-card-contact">
                        <span class="team-card-contact-label">📞 Điện thoại:</span><br>
                        {member['phone']}
                    </div>
                    <div class="team-card-contact">
                        <span class="team-card-contact-label">📧 Email:</span><br>
                        <a href="mailto:{member['email']}" style="color: #0066CC; text-decoration: none;">{member['email']}</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Teacher section
    st.markdown('<div class="category-title"> Giáo viên hướng dẫn</div>', unsafe_allow_html=True)
    cols = st.columns(len(teacher))
    for idx, member in enumerate(teacher):
        with cols[idx]:
            st.markdown(f"""
                <div class="team-card">
                    <div class="team-card-image">{member['initials']}</div>
                    <div class="team-card-name">{member['name']}</div>
                    <div class="team-card-role">{member['role']}</div>
                    <div class="team-card-divider"></div>
                    <div class="team-card-contact">
                        <span class="team-card-contact-label">📞 Điện thoại:</span><br>
                        {member['phone']}
                    </div>
                    <div class="team-card-contact">
                        <span class="team-card-contact-label">📧 Email:</span><br>
                        <a href="mailto:{member['email']}" style="color: #0066CC; text-decoration: none;">{member['email']}</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Advisors section
    st.markdown('<div class="category-title"> Cố vấn khoa học</div>', unsafe_allow_html=True)
    cols = st.columns(len(advisors))
    for idx, member in enumerate(advisors):
        with cols[idx]:
            st.markdown(f"""
                <div class="team-card">
                    <div class="team-card-image">{member['initials']}</div>
                    <div class="team-card-name">{member['name']}</div>
                    <div class="team-card-role">{member['role']}</div>
                    <div class="team-card-divider"></div>
                    <div class="team-card-contact">
                        <span class="team-card-contact-label">📞 Điện thoại:</span><br>
                        {member['phone']}
                    </div>
                    <div class="team-card-contact">
                        <span class="team-card-contact-label">📧 Email:</span><br>
                        <a href="mailto:{member['email']}" style="color: #0066CC; text-decoration: none;">{member['email']}</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Additional info section
    st.markdown("---")
    st.markdown("""
        <div style="background: #F8F9FA; padding: 24px; border-radius: 12px; border-left: 4px solid #00AA66; margin-top: 32px;">
            <h3 style="color: #0066CC; margin-top: 0;">Thông tin thêm</h3>
            <p><strong>Trường:</strong> Trường THPT Gia Định, Phường Thạnh Mỹ Tây, Thành phố Hồ Chí Minh</p>
            <p><strong>Mã dự án:</strong> 2526_KHTN_08</p>
            <p><strong>Lĩnh vực:</strong> Sinh học trên máy tính và Sinh - Tin</p>
            <p><strong>Cuộc thi:</strong> Cuộc thi Khoa học Kỹ thuật năm học 2025-2026</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: center; margin-top: 32px; color: #567; font-size: 0.9em;">
            <p>© 2025 Nhóm Nghiên Cứu - Trường THPT Gia Định</p>
        </div>
    """, unsafe_allow_html=True)

show()
menu()