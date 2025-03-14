from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
import warnings

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

# Read and parse the HTML file
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Function to extract table headers
def weekly_forecast():
    print("Weekly Forecast")
    print("*" * 20)
    headers = [header.text.strip() for header in soup.find_all("th")]
    print("| ".join(headers))

    # Extract table rows
    rows = soup.find_all("tr")
    for row in rows[1:]:
        data = [cell.text.strip() for cell in row.find_all("td")]
        print(f"In {data[0]} temperature will be {data[1]}, and will be {data[2]} day.") 


def highest_temperature():
    print("Highest Temperature")
    print("*" * 20)
    
    temp_days = []
    rows = soup.find_all("tr")
    for row in rows[1:]:
        data = [cell.text.strip() for cell in row.find_all("td")]
        temp_days.append(data[1])
        temp_days.sort()
        hottest_day = temp_days[-1]
    print(f"The hottest day will be {hottest_day}")


def sunny_days():
    print("Sunny Days")
    print("*" * 20)
    
    sunny_days = 0
    rows = soup.find_all("tr")
    for row in rows[1:]:
        data = [cell.text.strip() for cell in row.find_all("td")]
        if data[2] == "Sunny":
            sunny_days += 1
    print(f"There will be {sunny_days} sunny days this week.")

def average_temperature():
    print("Average Temperature")
    print("*" * 20)
    
    temp_days = []
    rows = soup.find_all("tr")
    for row in rows[1:]:
        data = [cell.text.strip() for cell in row.find_all("td")]
        data[1] = data[1].replace("°C", "")
        temp_days.append(int(data[1]))
    average_temp = sum(temp_days) / len(temp_days)
    print(f"The average temperature for the week is {average_temp} °C.")
# Main function for user choices
def main():
    while True:
        print("\nMenu:")
        print("1 - Show Weekly Forecast")
        print("2 - Highest Temperature")
        print("3 - Sunny days")
        print("4 - Average Temperature")
        print("5 - Exit")
        
        choice = input("Please enter your choice: ")

        if choice == "1":
            weekly_forecast()
        elif choice == "2":
            highest_temperature()
        elif choice == "3":
            sunny_days()
        elif choice == "4":
            average_temperature()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
