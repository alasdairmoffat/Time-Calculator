import datetime


def add_time(start, duration, start_day=None):

    time_format = "%I:%M %p"

    start_time = datetime.datetime.strptime(start, time_format)

    hour_delta, minute_delta = [int(d) for d in duration.split(":")]

    new_time = start_time + datetime.timedelta(hours=hour_delta, minutes=minute_delta)

    days_difference = (new_time.date() - start_time.date()).days

    output = new_time.strftime(time_format)

    if output[0] == "0":
        output = output[1:]

    if start_day:
        weekdays = (
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        )

        weekday = weekdays.index(start_day.capitalize())

        output += f", {weekdays[(weekday + days_difference) % 7]}"

    if days_difference == 0:
        pass
    elif days_difference == 1:
        output += " (next day)"
    else:
        output += f" ({days_difference} days later)"

    return output

