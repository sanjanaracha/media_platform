import streamlit as st
from d_base import conn_obj,cursor_obj

st.title("Media Platform")

if "users" not in st.session_state:
    st.session_state.users=None


def dashboard():
    st.sidebar.success("welcome user!!!")
    opt=st.sidebar.selectbox("choose:--",["UploadFiles","ViewFile","Logout"])
    st.header("Dashboard")

    if opt=="UploadFiles":
        st.header("upload your file here")
        choosedfile=st.file_uploader("choose:--",type=["pdf","jpg","jpeg","mp3","mp4","png"])

        if choosedfile:
            st.write(choosedfile.name)
            st.write(choosedfile.type)
        
    



def signup_fun():
    st.header("SignUp")
    with st.form("login_form"):
        name=st.text_input("name")
        email=st.text_input("email")
        password=st.text_input("password",type="password")
        btn=st.form_submit_button("signup")

        if btn:
            query="insert into users (name,email,password) values (%s,%s,%s)"
            values=(name,email,password)
            cursor_obj.execute(query,values)
            conn_obj.commit()
            st.write("user added successfully")

def login_fun():
    st.header("Login")
    with st.form("login"):
        email=st.text_input("email")
        password=st.text_input("password",type="password")
        btn=st.form_submit_button("Login")

        if btn:
            query="select * from users where email=%s and password=%s"
            values=(email,password)
            cursor_obj.execute(query,values)
            loggedin_user=cursor_obj.fetchone()
            st.session_state.user=loggedin_user
            st.write("loggedin successfully")
            st.rerun()


if st.session_state.users==None:
    login,signup=st.tabs(
        ["Login","SignUp"]
    )
    with signup:
        signup_fun()
    with login:
        login_fun()
else:
    dashboard()