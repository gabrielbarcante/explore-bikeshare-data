import re
import timeit
from sys import exit

import pandas as pd


def main():

    city, month, day = starting_program()

    print("\nJust one moment... loanding the data\n")
    filename = citys_data[city][0]
    df = pd.read_csv(filename)
    print("Data loaded. Now applying filters...\n")

    # Convert column Start Time to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Extract month, day of week and hour from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month_name()
    df["day"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour

    # Create column with the start station --> end station
    df["id_Start_End"] = df["Start Station"] + " --> " + df["End Station"]

    # Filtering the data frame
    if month:
        df = df[df["month"] == month]
    if day:
        df = df[df["day"] == day]

    # Descriptive statistics
    # 1 Popular times of travel
    # Most popular day
    if not day:
        start = timeit.default_timer()

        aux_calculation = df["day"].mode()
        aux_calculation = "\n".join(aux_calculation)

        time = timeit.default_timer() - start
        print_calculation(
            "What is the most popular day for traveling?", aux_calculation, time
        )

    # Most popular month
    if not month:
        start = timeit.default_timer()

        aux_calculation = df["month"].mode()
        aux_calculation = "\n".join(aux_calculation)

        time = timeit.default_timer() - start
        print_calculation(
            "What is the most popular month for traveling?", aux_calculation, time,
        )

    # Most popular hour
    start = timeit.default_timer()

    aux_calculation = df["hour"].mode().astype("str")
    aux_calculation = "\n".join(aux_calculation)

    time = timeit.default_timer() - start
    print_calculation(
        "What is the most popular hour of the day to start your travels?",
        aux_calculation,
        time,
    )

    # 2 Popular stations and trip
    # Most common start station
    start = timeit.default_timer()

    aux_calculation = df["Start Station"].mode()
    aux_calculation = "\n".join(aux_calculation)

    time = timeit.default_timer() - start
    print_calculation(
        "What is the most popular Start Station?", aux_calculation, time,
    )

    # Most common end station
    start = timeit.default_timer()

    aux_calculation = df["End Station"].mode()
    aux_calculation = "\n".join(aux_calculation)

    time = timeit.default_timer() - start
    print_calculation(
        "What is the most popular End Station?", aux_calculation, time,
    )

    # Most common trip from start to end
    start = timeit.default_timer()

    aux_calculation = df["id_Start_End"].mode()
    aux_calculation = "\n".join(aux_calculation)
    aux_calculation = f"Start Station --> End Station\n{aux_calculation}"

    time = timeit.default_timer() - start
    print_calculation(
        "What was the most popular trip from start to end?", aux_calculation, time,
    )

    # 3 Trip duration
    # Total travel time
    start = timeit.default_timer()

    aux_calculation = df["Trip Duration"].sum()
    aux_calculation = pd.to_timedelta(aux_calculation, unit="s")

    time = timeit.default_timer() - start
    print_calculation(
        "What was the total traveling done?", aux_calculation, time,
    )

    # Average travel time
    start = timeit.default_timer()

    aux_calculation = df["Trip Duration"].mean()
    aux_calculation = pd.to_timedelta(aux_calculation, unit="s")

    time = timeit.default_timer() - start
    print_calculation(
        "What was the average time spent on each trip?", aux_calculation, time,
    )

    # 4 User info
    # Counts of each user type
    start = timeit.default_timer()

    aux_calculation = df["User Type"].value_counts()

    time = timeit.default_timer() - start
    print_calculation(
        "What is the breakdown of users?", aux_calculation, time,
    )

    if city == "chicago" or city == "new york city":
        # Counts of each gender
        start = timeit.default_timer()

        aux_calculation = df["Gender"].value_counts()

        time = timeit.default_timer() - start
        print_calculation(
            "What is the breakdown of gender?", aux_calculation, time,
        )

        # Earliest, most recent, most common year of birth
        start = timeit.default_timer()

        aux_calculation = "Oldest: {}\n".format(df["Birth Year"].min())
        aux_calculation = "{}Youngest: {}\n".format(
            aux_calculation, df["Birth Year"].max()
        )
        aux_calculation = "{}Most popular year: {}".format(
            aux_calculation, ", ".join(df["Birth Year"].mode().astype("str"))
        )

        time = timeit.default_timer() - start
        print_calculation(
            "What is the oldest, youngest, and most popular year of birth?",
            aux_calculation,
            time,
        )

    # Print 5 lines of raw data if the answer is 'yes', and continue these prompts and displays until the user says 'no'
    print_raw_data(df.iloc[:, range(df.shape[1] - 4)])

    restart_program()


def starting_program():
    print("\nHello! Let's explore some US bikeshare data!")

    while True:
        city = input(
            "Would you like to see data for Chicago, New York City, or Washington?\n"
        )
        if city in citys_data:
            break
        else:
            for key, items_city in citys_data.items():
                if re.search(items_city[1], city, re.IGNORECASE):
                    city = key
                    break
            if city in citys_data:
                break

    while True:
        time = input(
            "\nWould you like to filter the data by month(m), day(d), both(b), or not at all? Type 'none'(n) for no time filter.\n"
        )
        if time in times:
            break
        else:
            for key, pattern in times.items():
                if re.search(pattern, time, re.IGNORECASE):
                    time = key
                    break
            if time in times:
                break

    if time == "month" or time == "both":
        while True:
            month = input(
                "\nWhich month? January, February, March, April, May, or June?\n"
            )
            if month in months:
                break
            else:
                for key, pattern in months.items():
                    if re.search(pattern, month, re.IGNORECASE):
                        month = key
                        break
                if month in months:
                    break
    else:
        month = None

    if time == "day" or time == "both":
        while True:
            day = input(
                "\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n"
            )
            if day in days:
                break
            else:
                for key, pattern in days.items():
                    if re.search(pattern, day, re.IGNORECASE):
                        day = key
                        break
                if day in days:
                    break
    else:
        day = None

    return (city, month, day)


def print_calculation(question, answer, time):
    print("Calculating statistic...\n")
    print(question)
    print(answer)
    print(f"That took {time} seconds\n")


def print_raw_data(df):
    i = 0
    while True:
        answer = input(
            "\nWould you like to view individual Trip data? Type 'yes' or 'no'.\n"
        )
        if re.search(r"^y(es)?$", answer, re.IGNORECASE):
            print(df[i : i + 5])
            i += 5
        elif re.search(r"^n(o)?$", answer, re.IGNORECASE):
            break


def restart_program():
    while True:
        answer = input("\nWould you like to restart? Type 'yes' or 'no'.\n")
        if re.search(r"^y(es)?$", answer, re.IGNORECASE):
            main()
        elif re.search(r"^n(o)?$", answer, re.IGNORECASE):
            exit()


citys_data = {
    "chicago": ["chicago.csv", r"^c(hicago)?$"],
    "new york city": ["new_york_city.csv", r"^n(ew( )*)?y(ork( )*)?c(ity( )*)?$"],
    "washington": ["washington.csv", r"^w(ashington)?$"],
}

times = {
    "month": r"^m(onth)?$",
    "day": r"^d(ay)?$",
    "both": r"b(oth)?$",
    "none": r"n(one)?$",
}

months = {
    "January": r"^jan(uary)?$",
    "February": r"^feb(ruary)?$",
    "March": r"^mar(ch)?$",
    "April": r"^ap(ril)?$",
    "May": r"^may$",
    "June": r"^june$",
}

days = {
    "Monday": r"^mon(day)?$",
    "Tuesday": r"^tue(sday)?$",
    "Wednesday": r"^wed(nesday)?$",
    "Thursday": r"^thu(rsday)?$",
    "Friday": r"^fri(day)?$",
    "Saturday": r"^sat(urday)?$",
    "Sunday": r"sun(day)?$",
}


if __name__ == "__main__":
    main()
