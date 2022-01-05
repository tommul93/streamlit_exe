import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import pandas as pd




def main():
    st.title("Hello!")
    st.text("This is an example application that test the ability to create an .exe from an web-application")

    st.subheader("steps")

    st.text("1) download & install nodejs (https://nodejs.org/en/)")
    st.text("2) install natifier --> cmd: npm install -g nativefier")
    st.text("1) ")
    st.text("Name your application : --name '<you .exe name>' '<your streamlit sharing website url>' --platform <'windows' or 'mac' or 'linux'>")
    st.text("Name your application : --name streamlit_exe https://share.streamlit.io/tommul93/streamlit_exe/main/main.py --platform windows")
    # nativefier --name streamlit_exe https://share.streamlit.io/tommul93/streamlit_exe/main/main.py --platform windows

    st.subheader("src")
    st.text("- https://github.com/nativefier/nativefier ")
    st.text("- https://discuss.streamlit.io/t/streamlit-deployment-as-an-executable-file-exe-for-windows-macos-and-android/6812 ")

    st.subheader("example_app:")

    #data
    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')


    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(
        selection_mode='disabled',
        use_checkbox=True,
        rowMultiSelectWithClick=False,
        suppressRowDeselection=False)

    gb.configure_grid_options()
    gridOptions = gb.build()
    grid_height = st.sidebar.number_input("Grid height", min_value=5, max_value=800, value=200)
    grid_response = AgGrid(
        df,
        editable=True,
        fit_columns_on_grid_load=True,
        data_return_mode=DataReturnMode.FILTERED,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True, #Set it to True to allow jsfunction to be injected
        )

    df = grid_response['data']
    selected = grid_response['selected_rows']
    selected_df = pd.DataFrame(selected)



    print(f"Length dataset : {len(grid_response['data'])}")
    print(f"selected rows: {grid_response['selected_rows']}")


if __name__ == "__main__":
    main()
