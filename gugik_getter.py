import copy
import time
import urllib.request


class GugikApiCallsPreparer:
    def __init__(self, file_path, x_start, x_end, x_step, y_start, y_end, y_step, points_in_one_call,
                 max_calls_in_a_file=5000):
        self.file_path_to_save_calls = file_path
        self.x_start = x_start
        self.x_end = x_end
        self.x_step = x_step
        self.y_start = y_start
        self.y_end = y_end
        self.y_step = y_step
        self.points_in_one_call = points_in_one_call
        self.points_list = []
        self.divided_points_list = []
        self.calls_list = []
        self.max_calls_in_a_file = max_calls_in_a_file

    def generate_points_and_save(self):
        self.generate_points()
        self.divide_list()
        self.save_points()

    def generate_list_of_points(self):
        y_points = range(self.y_start, self.y_end, self.y_step)  # y to tak naprawde x w PUWG 1992
        x_points = range(self.x_start, self.x_end, self.y_step)  # x to tak naprawde y w PUWG 1992

        for x in x_points:
            for y in y_points:
                self.points_list.append(
                    {
                        "x": x,
                        "y": y
                    }
                )

    def generate_points(self):
        self.generate_list_of_points()
        if self.points_in_one_call == 1:
            for point in self.points_list:
                self.calls_list.append(
                    f"https://services.gugik.gov.pl/nmt/?request=GetHByXY&x={point['x']}&y={point['y']}\n")
        else:
            counter = 1
            basic_call = "https://services.gugik.gov.pl/nmt/?request=GetHByPointList&list="
            call = basic_call
            for point in self.points_list:
                if counter > 1:
                    call += ","
                call += f"{point['x']} {point['y']}"
                if counter == self.points_in_one_call:
                    counter = 0
                    call += "\n"
                    self.calls_list.append(call)
                    call = basic_call
                counter += 1
            if counter > 1:
                call += "\n"
                self.calls_list.append(call)

    def save_points(self):
        with open(self.file_path_to_save_calls, "w") as f:
            f.writelines(self.calls_list)
        counter = 0
        for i in self.divided_points_list:
            if counter < 10:
                counter_str = f"0{counter}"
            else:
                counter_str = f"1{counter}"
            file_name = self.file_path_to_save_calls.replace(".txt", f"{counter_str}.txt")
            with open(file_name, "w") as f:
                f.writelines(i)
            counter += 1

    def divide_list(self):
        counter = 0
        sub_list = []
        for call in self.calls_list:
            sub_list.append(call)
            counter += 1
            if counter >= self.max_calls_in_a_file:
                counter = 0
                self.divided_points_list.append(copy.deepcopy(sub_list))
                sub_list = []
        if sub_list:
            self.divided_points_list.append(copy.deepcopy(sub_list))


class GetFromGugik:
    def __init__(self, calls_file_path, output_file_path, log_file_path, sleep_between_calls=1):
        self.calls = self.read_calls(calls_file_path)
        self.output_file_path = output_file_path
        self.log_file_path = log_file_path
        self.sleep = sleep_between_calls

    @staticmethod
    def read_calls(file_path):
        with open(file_path, "r") as f:
            return f.readlines()

    def execute_calls(self):
        for call in self.calls:
            call_corrected = call.replace(" ", "%20")
            print(call_corrected)
            returned = ""
            try:
                returned = urllib.request.urlopen(call_corrected)
                returned = returned.read()
                returned = returned.decode("utf-8")
            except Exception as e:
                returned = e
            print(returned)
            print("\n\n")
            if "GetHByXY" in call:
                x = call[call.find("x=")+2:call.find("&y=")]
                y = call[call.find("y=")+2:]
                y = y.replace("\n", "")
                returned = f"{x}, {y}, {returned}"
            with open(self.output_file_path, "a") as f:
                f.write(f"{returned}\n")
            with open(self.log_file_path, "a") as f:
                f.write(f"{call}\n{returned}\n\n")
                time.sleep(self.sleep)


class CorrectErrors:
    def __init__(self, file_to_be_corrected_path, sleep_between_calls=1):
        self.input_file_path = file_to_be_corrected_path
        self.output_file_path = f"{self.input_file_path}_corrected.txt"
        self.sleep = sleep_between_calls
        self.errors_list = ["Error", "Bad", "closed", "connection", "gateway", "Errno", "timed"]

    def correct_in_loop(self):
        lines = []
        with open(self.input_file_path, "r") as f:
            lines = f.readlines()

        with (open(self.output_file_path, "w") as f):
            for i in lines:
                print(i)
                if "HTTP Error 502: Bad Gateway" in i or "Remote end closed connection without response" in i or "timed out" in i or "Errno -3" in i:
                    x_y = i.split(",")
                    x = x_y[0].strip()
                    y = x_y[1].strip()
                    url = f"https://services.gugik.gov.pl/nmt/?request=GetHByXY&x={x}&y={y}"
                    print(url)
                    try:
                        returned = urllib.request.urlopen(url)
                        returned = returned.read()
                        returned = returned.decode("utf-8")
                        print(returned)
                        print("\n\n")
                    except Exception as e:
                        returned = e
                    time.sleep(1)
                    f.write(f"{x}, {y}, {returned}\n")
                else:
                    f.write(i)

    def check_errors_in_file(self):

        file_contents = ""
        with open(self.input_file_path, "r") as f:
            file_contents = f.read()
        for error in self.errors_list:
            if file_contents.find(error) >= 0:
                print(error)
