import streamlit as st
import requests

st.title("Countary Finder")

name = st.text_input("Enter country name")


if st.button("Search"):
    if name.strip() == "":
        st.warning("Please enter a country name.")

    else:
        url = "https://countries-api.davegarvey.workers.dev/search"
    response = requests.get(url, params={"q": name})

    if response.status_code == 200:
        data = response.json()

        result = data.get("results", [])
        country_data = result[0]

    if len(result) > 0:
        country_data = result[0]

        st.subheader(country_data["name"])

        col1, col2, col3 = st.columns(3)

        col1.metric("Capital", country_data["capital"])
        col2.metric("population", f"{country_data['population']:,}")
        col3.metric("region", country_data["region"])

        # st.write("Country:", country_data["name"])
        # st.write("Capital:", country_data["capital"])
        # st.write("Population:", country_data["population"])
        # st.write("Region:", country_data["region"])
    else:
        st.error("Country not Found!")


# else:
#     st.error("Something went Wrong , try again")
