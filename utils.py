import datetime


def convert_date(input_date):
    try:
        date_part, time_part = input_date.split()

        input_format = "%m/%d/%Y %H"
        output_format = "%Y-%m-%d %H:%M:%S.%f"

        if time_part in ["24", "00"]:
            time_part = "00"

        formatted_date_time = f"{date_part} {time_part}"

        return datetime.datetime.strptime(formatted_date_time, input_format).strftime(
            output_format
        )
    except:
        print("Error while converting date")


def get_date_range():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2023, 8, 31)
    date_range = []

    while start_date <= end_date:
        last_day = (start_date.replace(day=28) + datetime.timedelta(days=4)).replace(
            day=1
        ) - datetime.timedelta(days=1)

        start_str = start_date.strftime("%m%d%Y")
        end_str = last_day.strftime("%m%d%Y")

        month_dict = {"start": start_str, "end": end_str}

        date_range.append(month_dict)

        start_date = last_day + datetime.timedelta(days=1)

    return date_range
