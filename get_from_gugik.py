# GUGIK NMT is public API and you shouldn't stress it too much because they may accuse you of DDOS attack.
# Author of this software doesn't take ANY responsibility for inapropriate usage.
#
# GUGIK NMT jest publicznym API i nie wolno go zbyt mocno obciążać.
# Autor tego oprogramowania nie ponosi ŻADNEJ odpowiedzialności za nieprawidłowe użycie.

import sys
from config import base_dir
from gugik_getter import GetFromGugik

name = sys.argv[1]

terrain_data = GetFromGugik(calls_file_path=f"{base_dir}/api_calls/{name}.txt",
                            output_file_path=f"{base_dir}/gugik_data/{name}.txt",
                            log_file_path=f"{base_dir}/gugik_log/{name}.txt",
                            sleep_between_calls=3)

terrain_data.execute_calls()
