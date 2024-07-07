import streamlit as st


class Css:
    @staticmethod
    def tema():
        css = """
        <style>
        .stButton>button {
            background-color: #041360;
            color: #dae6e6;
            text-align: center;
            display: inline-block;
            width: 100%;
            padding: 12px;
        }
        .stButton>button:hover {
            background-color: #271bda;
            color: #dae6e6;
        }
        .e1f1d6gn4:nth-child(7) .ef3psqc7{
            color: #dae6e6;
            background-color: #6d0f0f;
        }
        .e1f1d6gn4:nth-child(7) .ef3psqc7:hover {
            background-color: #942020;
            color: white;
        } 
        .e1f1d6gn4:nth-child(8) .ef3psqc7{
            color: #dae6e6;
            background-color: #6d0f0f;
        }
        .e1f1d6gn4:nth-child(8) .ef3psqc7:hover {
            background-color: #942020;
            color: white;
        }
        .e1f1d6gn4:nth-child(7) .ef3psqc12:hover {
            background-color: #942020;
            color: white;
        }
        .e1f1d6gn4:nth-child(7) .ef3psqc12 {
            color: #dae6e6;
            background-color: #6d0f0f;
        }
        .e1f1d6gn4:nth-child(9) .ef3psqc12{
            color: #dae6e6;
            background-color: #6d0f0f;
        }
        .e1f1d6gn4:nth-child(9) .ef3psqc12:hover {
            background-color: #942020;
            color: white;
        }
        .e1f1d6gn4:nth-child(8) .ef3psqc12{
            color: #dae6e6;
            background-color: #6d0f0f;
            width: 100%;
            padding: 0px;
        }
        .e1f1d6gn4:nth-child(8) .ef3psqc12:hover {
            background-color: #942020;
            color: white;
        }
        .e1f1d6gn4:nth-child(5) .ef3psqc7 {
            color: #dae6e6;
            background-color: #096004;
        }
        .e1f1d6gn4:nth-child(5) .ef3psqc7:hover {
            color: #dae6e6;
            background-color: #12b716;
        }
        .e1f1d6gn4:nth-child(6) .ef3psqc12 {
            color: #dae6e6;
            background-color: #096004;
        }
        .e1f1d6gn4:nth-child(6) .ef3psqc7 {
            color: #dae6e6;
            background-color: #096004;
        }
        .e1f1d6gn4:nth-child(6) .ef3psqc7:hover {
            color: #dae6e6;
            background-color: #12b716;
        }
        .e1f1d6gn4:nth-child(6) .ef3psqc12:hover {
            color: #dae6e6;
            background-color: #12b716;
        }
        .e10yg2by1+ .e10yg2by1 .ef3psqc7 {
            color: #dae6e6;
            background-color: #6d0f0f;
            padding: 0px
        } 
        .e1f1d6gn4:nth-child(9) .ef3psqc7 {
            color: #dae6e6;
            background-color: #096004;
        }
        .e1f1d6gn4:nth-child(9) .ef3psqc7:hover {
            color: #dae6e6;
            background-color: #12b716;
        }
        .e10yg2by1+ .e10yg2by1 .ef3psqc7:hover {
            background-color: #942020;
            color: white;
        }
        .ea3mdgi8 {
            background-color: #0c1020;
        }
        .ezrtsby2 {
            background-color: #0c1020;
        }
        .eczjsme3 {
            background-color: #1a1a1d;
        }
        .e1nzilvr1 {
            color: #bec1ca;
        }
        #root :nth-child(1) {
            color: #dae6e6;
        }
        .st-emotion-cache-uko8fv .ef3psqc7 {
            background-color: #041360;
            color: #dae6e6;
        }
        .st-bx, .st-b9, .st-bw, .e116k4er1, .st-bb, .st-by, .e116k4er3 {
            background-color: #1a1a1d;
            border-color: #041360;  
        }
        .st-di {
            background-color: #0c1020;
            border-color: #041360;
        }
        .eczjsme8 {
            background-color: #0c0c33;
        }
        #number_input_4, #number_input_5 {
            background-color: #1a1a1d;
            border-color: #041360; 
        }
        .e16zdaao0 {
            color: #dae6e6;
            background-color: #096004;
            width: 100%;
            padding: 12px;
        }
        .e16zdaao0: hover {
            color: #dae6e6;
            background-color: #12b716;
            width: 100%;
            padding: 12px;
        }
        .e1f1d6gn4 p {
            text-align: center;
            font-size: 20px;
        }
        .e1f1d6gn4 #carrinho {
            text-align: center;
        }
        .e1f1d6gn4 #sistema-estoque-inteligente {
            text-align: center;
        }
        .e1f1d6gn4 #bem-vindo-informe-os-dados-de-acesso {
            text-align: center;
        }
        </style>
        """
        return st.markdown(css, unsafe_allow_html=True)
