import streamlit as st

def main():
    st.title("🔢 Number Counter")
    st.write("Enter a list of numbers separated by space. I will count how many are positive, negative, or zero.")

    user_input = st.text_input("Enter numbers:", placeholder="e.g., 3 -1 0 5 0 -4")

    if user_input:
        try:
            numbers = list(map(int, user_input.strip().split()))
            positives = [n for n in numbers if n > 0]
            negatives = [n for n in numbers if n < 0]
            zeroes = [n for n in numbers if n == 0]

            st.subheader("📊 Results")
            st.write(f"**Positive numbers ({len(positives)}):** {positives}")
            st.write(f"**Negative numbers ({len(negatives)}):** {negatives}")
            st.write(f"**Zeroes ({len(zeroes)}):** {zeroes}")
        except ValueError:
            st.error("⚠️ Please enter valid integers separated by spaces.")

if __name__ == "__main__":
    main()