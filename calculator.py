import streamlit as st
import numpy as np
import statistics as stats
import math
import matplotlib.pyplot as plt

st.title("Calculator")
function = st.selectbox(
    "Select function",
    ["None", "Statistics", "Graphs", "Math", "Quadratic Equation"])

if function == "Math":
    x = st.number_input("Enter the first number")
    y = st.number_input("Enter the second number")
    st.write("Select operation")
    add = st.button("Add")
    if add:
        st.write(x + y)
    sub = st.button("Subtract")
    if sub:
        st.write(x - y)
    mul = st.button("Multiply")
    if mul:
        st.write(x * y)
    div = st.button("Divide")
    if div:
        st.write(x / y)

if function == "Statistics":
    data_input = st.text_area("Enter numbers separated by commas:")

    # Process the input into a list of integers
    if data_input:
        try:
            data_list = [int(x.strip()) for x in data_input.split(',')]
        except ValueError:
            st.error("Please enter valid integers separated by commas.")
            data_list = []
    Mean = st.button("Mean")
    if Mean:
        mean = np.mean(data_list)
        st.subheader(f"Mean: {mean}")
    Median = st.button("Median")
    if Median:
        median = np.median(data_list)
        st.subheader(f"Median: {median}")
    Mode = st.button("Mode")
    if Mode:
        if data_list:
            # Calculate Mode (handle multiple modes)
            try:
                mode = stats.mode(data_list)
            except stats.StatisticsError:  # Multiple modes case
                mode = "Multiple modes found"
        st.write(stats.mode(data_list))
        st.subheader(f"Mode: {mode}")

if function == "Quadratic Equation":

    X = st.number_input("Enter the coefficient of \(x^{2}\)")
    Y = st.number_input("Enter the coefficient of x ")
    Z = st.number_input("Enter the constant number")
    sub = st.button("Submit")
    D = (Y**2) - (4 * X * Z)
    if sub:
        if D < 0:
            st.write("No real roots")

        elif D > 0:
            st.write("Real and unequal roots")
            d = math.sqrt(D)
            d1 = ((-Y) + d) / (2 * X)
            d2 = ((-Y) - d) / (2 * X)
            st.write(d1, d2)

        elif D == 0:
            st.write("Real and equal roots")
            d1 = (-Y) / (2 * X)
            st.write(d1)

if function == "Graphs":

    def plot_graph(x, y):
        st.pyplot.line(x, y)

    def pie_chart(labels, values):
        st.pyplot.pie(values, labels=x)
        x = st.text_input("Enter x values separated by commas:")
        y = st.text_area("Enter y values separated by commas:")

        try:
            x_list = [str(x.strip()) for x in x.split(',')]
            y_list = [float(y.strip()) for y in y.split(',')]
        except ValueError:
            st.error("Please enter valid numbers separated by commas.")
            x_list = []
            y_list = []
            a = np.array(x_list)
            b = np.array(y_list)
            st.write("Select graph type")
            pie = st.button("Pie chart")
            if pie:
                fig, ax = plt.subplots()
                ax.pie(b, labels=a, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')
                st.pyplot(fig)

        bar = st.button("Bar chart")

        if bar:
            fig, ax = st.subplots()
            ax.bar(a, b)
            st.pyplot(fig)
