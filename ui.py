import streamlit as st

def apply_global_styles():
  st.markdown(
    """
    <style>
      :root {
        --primary:#0B5ED7;
        --accent:#0EA5A4;
        --success:#10B981;
        --warning:#F59E0B;
        --danger:#DC2626;
        --text:#111111;
        --muted:#567;
        --card-bg:#FFFFFF;
        --border:#E6E8EA;
        --shadow:0 2px 12px rgba(0,0,0,0.08);
        --radius:12px;
        --container:1200px;
        --space-lg:32px;
        --space-md:20px;
        --space-sm:12px;
      }
      .block-container{
        max-width: var(--container);
        padding-left: 2rem !important;
        padding-right: 2rem !important;
      }
      h1{font-size:44px; line-height:1.2;}
      h2{font-size:30px; line-height:1.3; margin-top: var(--space-lg);}
      p, li{font-size:18px; line-height:1.7;}
      .figure-wrap{ display:flex; justify-content:center; margin: 0 0 var(--space-lg) 0; }
      .figure-card{ text-align:center; border:1px solid var(--border); border-radius:var(--radius); padding: 8px 0; background: var(--card-bg); box-shadow: var(--shadow); }
      .figure-card img{ border-radius:8px; }
      .figure-caption{ font-size:18px; color:gray; margin-top: 8px; }
      .card{ background:var(--card-bg); border:1px solid var(--border); border-radius:var(--radius); box-shadow:var(--shadow); padding: var(--space-md); }
      .stat-card{ background:var(--card-bg); border:1px solid var(--border); border-radius:var(--radius); box-shadow:var(--shadow); padding: 20px; }
      .stat-title{ font-size:14px; color:var(--muted); text-transform:uppercase; letter-spacing:.04em; margin-bottom:8px; }
      .stat-value{ font-size:24px; font-weight:700; }
      .stat-subtitle{ font-size:16px; color:var(--muted); margin-top:6px; }
      .progress{ height:16px; background:#F1F3F5; border:1px solid var(--border); border-radius:999px; overflow:hidden; }
      .progress-fill{ height:100%; width: calc(var(--value) * 1%); background: linear-gradient(90deg, var(--success), var(--warning), var(--danger)); transition: width 600ms ease; }
      @keyframes fadeIn{ from{opacity:0; transform: translateY(6px);} to{opacity:1; transform:none;} }
      .fade-in{ animation: fadeIn 500ms ease both; }
      /* On-scroll reveal baseline */
      .reveal{ opacity:0; transform: translateY(6px); }
      .reveal.fade-in{ opacity:1; transform:none; }
      .rise:hover{ transform: translateY(-4px); box-shadow: 0 8px 20px rgba(0,0,0,0.12); transition: transform .2s ease, box-shadow .2s ease; }
      section[data-testid="stSidebar"] [data-testid="stSidebarContent"] a,
      section[data-testid="stSidebar"] [data-testid="stSidebarContent"] button{
        background:#ffffff !important; color:#111111 !important; border-radius:12px !important; padding: 0px 8px !important; margin: 2px 0 !important; border:1px solid rgba(0,0,0,0.08) !important; box-shadow:0 2px 8px rgba(0,0,0,0.08) !important;
      }
      section[data-testid="stSidebar"] [data-testid="stSidebarContent"] a:hover,
      section[data-testid="stSidebar"] [data-testid="stSidebarContent"] button:hover{ background:#f4f4f4 !important; }
      section[data-testid="stSidebar"] [data-testid="stSidebarContent"] a[aria-current="page"]{ border-color: rgba(0,0,0,0.2) !important; font-weight:700; }
    </style>
    <script>
      (function(){
        try{
          const els = document.querySelectorAll('.reveal');
          const obs = new IntersectionObserver((entries)=>{
            entries.forEach(e=>{
              if(e.isIntersecting){ e.target.classList.add('fade-in'); obs.unobserve(e.target); }
            });
          }, { threshold: 0.12 });
          els.forEach(el=>obs.observe(el));
        }catch(err){ /* no-op */ }
      })();
    </script>
    """,
    unsafe_allow_html=True
  )
