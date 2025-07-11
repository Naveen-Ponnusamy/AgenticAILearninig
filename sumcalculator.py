import streamlit as st

def main():
    st.title("🔢 Sum of Numbers Between Min and Max")

    st.write("Enter two integers. The app will calculate the sum from min to max (inclusive).")

    # Separate input boxes for min and max values
    min_val = st.number_input("Enter minimum value:", step=1)
    max_val = st.number_input("Enter maximum value:", step=1)

    if st.button("Calculate Sum"):
        if min_val > max_val:
            st.error("⚠️ Minimum value must be less than or equal to maximum value.")
        else:
            total = 0
            for i in range(int(min_val), int(max_val) + 1):
                total += i

            st.success(f"Sum of numbers from {int(min_val)} to {int(max_val)} is: {total}")

if __name__ == "__main__":
    main()
