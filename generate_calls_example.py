from config import base_dir
from gugik_getter import GugikApiCallsPreparer

kotlina_klodzka = GugikApiCallsPreparer(file_path=f"{base_dir}/api_calls/kotlina_klodzka.txt",
                                        x_start=245000,
                                        x_end=310000,
                                        x_step=130,
                                        y_start=295000,
                                        y_end=360000,
                                        y_step=130,
                                        points_in_one_call=1,
                                        max_calls_in_a_file=36000)

kotlina_klodzka.generate_points_and_save()

szczecin_okolice = GugikApiCallsPreparer(file_path=f"{base_dir}/api_calls/szczecin_okolice.txt",
                                        x_start=609382,
                                        x_end=642323,
                                        x_step=65,
                                        y_start=197348,
                                        y_end=230000,
                                        y_step=65,
                                        points_in_one_call=1,
                                        max_calls_in_a_file=30000)

szczecin_okolice.generate_points_and_save()
