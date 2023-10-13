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
