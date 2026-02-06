import streamlit as st
from add_update_ui import add_update_tap
from analytics_category_ui import analytics_category_tab
from analytics_months_ui import analytics_months_tab


#image
st.markdown("<style>.stApp{background-image:url('https://images.unsplash.com/photo-1526304640581-d334cdbbf45e');"
            "background-size:cover;} .stApp::before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;"
            "backdrop-filter:blur(5px) brightness(20%);}</style>", unsafe_allow_html=True)


#Headers
st.markdown("<h1 style='white-space:nowrap;'>💰SpendWise – Personal Expense Tracker</h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;font-size:0.9rem;'>"
            "Track • Analyze • Improve your spending habits</p>", unsafe_allow_html=True)
# st.title("💰SpendWise – Personal Expense Tracker")
# st.caption("Track • Analyze • Improve your spending habits")



#Body
tab1, tab2, tab3 = st.tabs(["📝 Record Expenses", "📊 Category Insights", "📈 Monthly Trends"])
with tab1:
    add_update_tap()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()


#footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>"
    "Developed by <b>Amaan Ali</b> • © 2026"
    "</p>",
    unsafe_allow_html=True
)

