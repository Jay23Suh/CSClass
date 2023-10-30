"""
    CS051P Lab Assignments: Stock v.s. Rain

    Author: Jayhyun Suh

    Date:   14 November 2022

    The goal of this assignment is to familiarize you with data analysis
    and visualization. You'll practice handling files in csv format,
    create and manipulate Python dictionaries, and do some basic plotting
    using the matplotlib package.
"""
import matplotlib.pyplot as plt
import csv


def parse_rainfall(fname):
    """
    Converts a file into a dictionary containing the date as key and amount of precipitation as value
    :fname: (file) name of file that
    :return: (dictionary) modified dictionary of the dates and rain
    """

    # open file
    file = open(fname, "r")
    csv_file = csv.reader(file)

    # empty dictionary
    weather_dict = {}

    # for loop to skip the first line, to make sure no-data entries are not entered into dictionary, and to make sure
    # the length of each line is the appropriate length
    counter = 0
    for line in csv_file:
        if counter > 0 and "NA" not in line and len(line) == 5:
            weather_dict[line[0]] = float(line[1])
        counter += 1

    return weather_dict


def change_date(date):
    """
    Changes the date from stock files into a compatible format with the dates from rain files
    :date: (string) dates from the stock files that are not properly formatted
    :return: (string) modified dates
    """
    # empty lists to add dates to
    day_list = []
    month_list = []
    year_list = []
    counter = 0

    # add to a list based on the day, month, and year by utilizing "/" as a dividing tool.
    for char in date:
        if char == "/":
            counter += 1
        if counter == 0:
            month_list.append(char)
        if counter == 1 and char != "/":
            day_list.append(char)
        if counter == 2 and char != "/":
            year_list.append(char)

    # modify the month based on if the length was one or two
    if len(month_list) == 1:
        new_month = "0" + str(month_list[0])
    elif len(month_list) == 2:
        new_month = str(month_list[0] + month_list[1])

    # modify the day based on if the length was one or two
    if len(day_list) == 1:
        new_day = "0" + str(day_list[0])
    elif len(day_list) == 2:
        new_day = str(day_list[0] + day_list[1])

    # since everything is from the 21st century, just add 20 in front of the year.
    new_year = "20" + str(year_list[0]) + str(year_list[1])

    # put everything back together
    final_date = new_year + "-" + new_month + "-" + new_day

    return final_date


def parse_stock(fname, sym):
    """
    Looks at a file and creates a dictionary containing the date and the difference between opening and closing price
    of a stock
    :fname: (file) file containing stock information
    :sym: (string) the desired company we want information of
    :return: (dictionary) contains the date and change in price of a stock
    """

    # open files
    file = open(fname, "r")
    csv_file = csv.reader(file)

    stock_dict = {}

    # collects data from lines of the file that contain the same symbol and are not empty and contain important data
    for line in csv_file:
        if len(line) == 7 and sym == line[6] and len(line[0]) > 1 and len(line[1]) > 0 and len(line[4]) > 0:
            # changes date into the right format
            date = change_date(line[0])
            # calculates the difference by subtracting closing and opening
            change = float(line[4]) - float(line[1])
            stock_dict[date] = round(change, 2)

    return stock_dict


def correlate_data(stock_dict, rain_dict):
    """
    Takes two dictionaries given by parse functions and creates a list of lists that contain the change in price and
    amount of rain for matching dates from the dictionaries
    :stock_dict: (dictionary) return value from parse_stock
    :rain_dict: (dictionary) return value from parse_rain
    :return: list containing lists of the change in price and rain
    """

    final_list = []

    # for every key, which is the date, in rain_dict it checks to see if the date is in stock_dict
    # if it is, appends the values (stock change and rain) to a list that is reset every for loop .
    for i in rain_dict:
        # reset list
        price_rain_list = []
        if i in stock_dict:
            price_rain_list.append(stock_dict[i])
            price_rain_list.append(rain_dict[i])
            # appended to final_list to create list within lists
            final_list.append(price_rain_list)

    return final_list


# emtpy list to be used in scatter_plot
stock_list = []


def scatter_plot(data, format, name, done):
    """
    draws a scatter plot with rain on the x-axis and change in stock prices on the y-axis.
    :data: (list) list containing stock price and amount of rain respectively
    :format: determines the color and what each marker looks like
    :name: (string) symbol of the stock
    :done: (bool) determines when scatter_plot should plot the legend and show the plot
    """

    # each time scatter_plot is called, the name of a stock is appended into stock_list
    stock_list.append(name)

    # empty lists for x and y
    x_list = []
    y_list = []

    # for all the data, append to the x and y lists the corresponding information from data
    for i in range(len(data)):
        x_list.append(data[i][1])
        y_list.append(data[i][0])

    # plot points
    plt.plot(x_list, y_list, format)

    # if done is true, plot the legend and labels. Also show the scatter_plot
    if done:
        plt.legend(stock_list)
        plt.xlabel("Rainfall")
        plt.ylabel("Price Change")
        plt.title("Rainfall vs Price Change")
        plt.show()


def main():
    """
    Gets inputs from the user on file names and the stocks they want to compare. uses other functions to analyze the
    effect of rain on prices in stocks. One stock is based in Seattle, and the other is not
    """

    # asks for inputs on the file names and the desired symbols
    rain_data = input("Enter the name of a rainfall data file:\n\t")
    stock_data = input("Enter the name of a stock data file:\n\t")
    first_symbol = input("Enter a first stock symbol (e.g. MSFT or AMZN):\n\t")
    second_symbol = input("Enter a second stock symbol (not head-quartered in Seattle):\n\t")

    # uses parse functions to get dictionaries on both stocks and rain
    stock = parse_stock(stock_data, first_symbol)
    stock_two = parse_stock(stock_data, second_symbol)
    rain = parse_rainfall(rain_data)

    # each stock is compared to rain by the function of correlate_data
    rs_list = correlate_data(stock, rain)
    rs_list_two = correlate_data(stock_two, rain)

    # second time scatter_plot is called, done is True to show and plot legends
    done_one = False
    done_two = True

    # scatter plot for each data
    scatter_plot(rs_list, 'b*', first_symbol, done_one)
    scatter_plot(rs_list_two, 'r+', second_symbol, done_two)


if __name__ == '__main__':
    main()
