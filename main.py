import streamlit as st

st.title("Hello Bright Cape")


import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')


gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection(selection_mode='disabled', #single
                       use_checkbox=True,
                       rowMultiSelectWithClick=False,
                       suppressRowDeselection=False,
                       )


gb.configure_grid_options()
gridOptions = gb.build()
grid_height = st.sidebar.number_input("Grid height", min_value=200, max_value=800, value=200)
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
# data = display_table(df)


print(f"Length dataset : {len(grid_response['data'])}")
print(f"selected rows: {grid_response['selected_rows']}")



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
