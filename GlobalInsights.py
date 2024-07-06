import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to convert numbers into words
def convert_to_indian_format(number):
    if number >= 1000000000000:
        return f"{number / 1000000000000:.2f} trillion"
    elif number >= 1000000000:
        return f"{number / 1000000000:.2f} billion"
    elif number >= 1000000:
        return f"{number / 1000000:.2f} million"
    else:
        return number

df = pd.read_csv('dataset.csv')

st.title('Welcome to Global Insight')

country = st.selectbox('Select a country', df['country'].unique())

# Filter data for the selected country, India, and the United States for comparison
country_data = df[df['country'] == country].squeeze()
india_data = df[df['country'] == 'India'].squeeze()
us_data = df[df['country'] == 'United States'].squeeze()

def styled_header(text, color):
    return f'<h2 style="color:{color};">{text}</h2>'

st.markdown(styled_header(f"Insights about {country}", "#1f77b4"), unsafe_allow_html=True)

# Display sections
st.subheader('General Information')
st.write(f"**Capital City:** {country_data['capital_city']}")
st.write(f"**Region:** {country_data['region']}")
st.write(f"**Continent:** {country_data['continent']}")
st.write(f"**Currency:** {country_data['currency']}")
st.write(f"**Population:** {convert_to_indian_format(country_data['population'])}")
st.write(f"**Density :** {country_data['Density (P/Km²)']} P/Km²")
st.write(f"**Land Area :** {country_data['Land Area (Km²)']} Km²")
st.write(f"**World Share:** {country_data['World Share']} %")

st.markdown(styled_header('Economic Indicators', "#2ca02c"), unsafe_allow_html=True)
st.write(f"**GDP :** {convert_to_indian_format(country_data['gdp'])} $")
st.write(f"**Inflation Rate:** {country_data['inflation']} %")
st.write(f"**CO2 Emissions:** {convert_to_indian_format(country_data['co2_emissions'])} T/Y")

st.markdown(styled_header('Health and Demographics', "#d62728"), unsafe_allow_html=True)
st.write(f"**Life Expectancy:** {country_data['life_expectancy']} Years")
st.write(f"**Health Expenditure per Capita:** {country_data['health_expenditure_capita']} $")
st.write(f"**Hospital Beds per 1000 people:** {country_data['hospital_beds']}")
st.write(f"**Suicide Rate:** {country_data['suicide_rate']} %")
st.write(f"**Birth Rate:** {country_data['birth_rate']} /1000 people")
st.write(f"**Death Rate:** {country_data['death_rate']} /1000 people")
st.write(f"**Fertility Rate:** {country_data['fertility_rate']} kids/mother")
st.write(f"**Median Age:** {country_data['median_age']} Years")
st.write(f"**Population Female:** {convert_to_indian_format(country_data['population_female'])}")
st.write(f"**Population Male:** {convert_to_indian_format(country_data['population_male'])}")
st.write(f"**Rural Population (%):** {convert_to_indian_format(country_data['rural_population'])}")
st.write(f"**Urban Population (%):** {convert_to_indian_format(country_data['urban_population'])}")

st.markdown(styled_header('Internet and Democracy', "#9467bd"), unsafe_allow_html=True)
st.write(f"**Internet Usage :** {country_data['internet_pct']} %")
st.write(f"**Type of Democracy:** {country_data['democracy_type']}")

# Comparing with India and the United States: Bar Graphs
st.header('Comparison with India and the United States 🇮🇳🇺🇸')

fig, axes = plt.subplots(7, 1, figsize=(10, 42))

# Economic Indicators Comparison
indicators = ['GDP ($)', 'CO2 Emissions (T/Y)', 'Life Expectancy (Years)', 'Health Expenditure per Capita ($)',
              'Land Area (Km²)', 'Inflation Rate (%)', 'Median Age (Years)']
country_values = [country_data['gdp'], country_data['co2_emissions'], country_data['life_expectancy'], country_data['health_expenditure_capita'],
                  country_data['Land Area (Km²)'], country_data['inflation'], country_data['median_age']]
india_values = [india_data['gdp'], india_data['co2_emissions'], india_data['life_expectancy'], india_data['health_expenditure_capita'],
                india_data['Land Area (Km²)'], india_data['inflation'], india_data['median_age']]
us_values = [us_data['gdp'], us_data['co2_emissions'], us_data['life_expectancy'], us_data['health_expenditure_capita'],
             us_data['Land Area (Km²)'], us_data['inflation'], us_data['median_age']]

axes[0].bar(country, country_values[0], color='blue', label=country)
axes[0].bar('India', india_values[0], color='green', alpha=0.5, label='India')
axes[0].bar('United States', us_values[0], color='orange', alpha=0.5, label='United States')
axes[0].set_ylabel('$')
axes[0].set_title('GDP Comparison')
axes[0].legend()

axes[1].bar(country, country_values[1], color='blue', label=country)
axes[1].bar('India', india_values[1], color='green', alpha=0.5, label='India')
axes[1].bar('United States', us_values[1], color='orange', alpha=0.5, label='United States')
axes[1].set_ylabel('T/Y')
axes[1].set_title('CO2 Emissions Comparison')
axes[1].legend()

axes[2].bar(country, country_values[2], color='blue', label=country)
axes[2].bar('India', india_values[2], color='green', alpha=0.5, label='India')
axes[2].bar('United States', us_values[2], color='orange', alpha=0.5, label='United States')
axes[2].set_ylabel('Years')
axes[2].set_title('Life Expectancy Comparison')
axes[2].legend()

axes[3].bar(country, country_values[3], color='blue', label=country)
axes[3].bar('India', india_values[3], color='green', alpha=0.5, label='India')
axes[3].bar('United States', us_values[3], color='orange', alpha=0.5, label='United States')
axes[3].set_ylabel('$')
axes[3].set_title('Health Expenditure per Capita Comparison')
axes[3].legend()

axes[4].bar(country, country_values[4], color='blue', label=country)
axes[4].bar('India', india_values[4], color='green', alpha=0.5, label='India')
axes[4].bar('United States', us_values[4], color='orange', alpha=0.5, label='United States')
axes[4].set_ylabel('Km²')
axes[4].set_title('Land Area Comparison')
axes[4].legend()

axes[5].bar(country, country_values[5], color='blue', label=country)
axes[5].bar('India', india_values[5], color='green', alpha=0.5, label='India')
axes[5].bar('United States', us_values[5], color='orange', alpha=0.5, label='United States')
axes[5].set_ylabel('%')
axes[5].set_title('Inflation Rate Comparison')
axes[5].legend()

axes[6].bar(country, country_values[6], color='blue', label=country)
axes[6].bar('India', india_values[6], color='green', alpha=0.5, label='India')
axes[6].bar('United States', us_values[6], color='orange', alpha=0.5, label='United States')
axes[6].set_ylabel('Years')
axes[6].set_title('Median Age Comparison')
axes[6].legend()

plt.tight_layout()
st.pyplot(fig)

# About section
st.sidebar.header("About")
st.sidebar.info(
    """
    This application provides comprehensive insights into various countries around the world. Select a country from the dropdown to explore detailed statistics and visualizations comparing key indicators across countries.
    
    Features:
    - View economic indicators such as GDP, CO2 emissions, and inflation rate.
    - Explore health and demographic statistics including life expectancy, health expenditure, and population demographics.
    - Compare selected country data with India and the United States for benchmarking.
    
    Data Sources:
    Data used in this application is sourced from publicly available datasets and provides a snapshot of each country's socio-economic and demographic profile.
    
    Future Enhancements:
    We are continuously updating the application to include more countries and enhance the comparison features. Stay tuned for more updates!
    """
)


st.sidebar.subheader("Connect")
st.sidebar.markdown(
    """
    **Developer:** Vedant Kale 🌏\n
    **Email:** vedant.kale22@pccoepune.org\n
    **LinkedIn:** [Connect on LinkedIn](https://www.linkedin.com/in/VedantKale106/)
    """
)

st.markdown("""
    <style>
        footer {
            visibility: hidden;
        }
        .footer {
            visibility: visible;
            position: fixed;
            right: 0;
            bottom: 0;
            text-align: right;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        Made by Vedant Kale 🌏
    </div>
""", unsafe_allow_html=True)
