import tls_client
import shlex
import argparse
import json
from typing import Union

client: None | tls_client.Session = None

def to_shorted_argn(argn: str) -> str:
    t = "-" + "".join(list(map((lambda x: x[0]), argn.replace("--", "").split("_"))))
    if t == "-h":
        t = "-H"
    if t == "-p":
        t = "-P"
    return t

def init(cmd: str) -> None:
    global client
    parser = argparse.ArgumentParser()
    ada = [
        [str, "--client_identifier"],
        [str, "--ja3_string"],
        [dict, "--h2_settings"],
        [list, "--h2_settings_order"],
        [list, "--supported_signature_algorithms"],
        [list, "--supported_delegated_credentials_algorithms"],
        [list, "--supported_versions"],
        [list, "--key_share_curves"],
        [str, "--cert_compression_algo"],
        [str, "--additional_decode"],
        [list, "--pseudo_header_order"],
        [int, "--connection_flow"],
        [list, "--priority_frames"],
        [list, "--header_order"],
        [dict, "--header_priority"],
        [bool, "--random_tls_extension_order", False],
        [bool, "--force_http1", False],
        [bool, "--catch_panics", False],
        [bool, "--debug", False]
    ]
    for i in ada:
        if i[0] == dict:
            i[0] = json.loads
        if len(i) == 2:
            parser.add_argument(to_shorted_argn(i[1]), i[1], type=i[0], required=False)
        elif len(i) == 3:
            parser.add_argument(to_shorted_argn(i[1]), i[1], type=i[0], required=False, default=i[2])
        elif len(i) == 4:
            parser.add_argument(to_shorted_argn(i[1]), i[1], type=i[0], required=i[3], default=i[2])

    try:
        args = parser.parse_args(shlex.split(cmd))
        client = tls_client.Session(**vars(args))
    except SystemExit:
        print('{"s": false, "e": "Invalid arguments"}')
        return
    
def req(cmd: str) -> None:

    global client
    parser = argparse.ArgumentParser()
    # list[list[type, name, default, required]]
    ada = [
        [str, "--method", None, True],
        [str, "--url", None, True],
        [dict, "--headers"],
        [dict, "--cookies"],
        [Union[str, dict], "--data"],
        [dict, "--json"],
        [bool, "--allow_redirects", False],
        [bool, "--insecure_skip_verify", False],
        [int, "--timeout_seconds"],
    ]

    for i in ada:
        if i[0] == dict:
            i[0] = json.loads
        if len(i) == 2:
            parser.add_argument(to_shorted_argn(i[1]), i[1], type=i[0], required=False)
        elif len(i) == 3:
            parser.add_argument(to_shorted_argn(i[1]), i[1], type=i[0], required=False, default=i[2])
        elif len(i) == 4:
            parser.add_argument(to_shorted_argn(i[1]), i[1], type=i[0], required=i[3], default=i[2])
    parser.add_argument("--proxy", type=json.loads, required=False)
    parser.add_argument("--params", type=json.loads, required=False)

    try:
        args = parser.parse_args(shlex.split(cmd))
        res = client.execute_request(**vars(args))
        dictx = {
            "headers": res.headers,
            "status_code": res.status_code,
            "cookies": res.cookies.get_dict(),
            "body": res.text
        }
        print(json.dumps(dictx))
    except SystemExit:
        print('{"s": false, "e": "Invalid arguments"}')
        return
# This function is used to run commands
# It is called in a loop
# It gets the command from the user and runs it
def commandRunner() -> None:
    global client
    cmd = input("> ")
    cmd = cmd.strip()

    if cmd == "exit":
        exit()
    if cmd.startswith("init ") or cmd == "init":
        init(cmd.replace("init","").strip())
        return
    if client is None:
        print('{"s": false, "e": "Please initialize the client first"}')
        return
    if cmd == "close":
        client = None
        return
    if cmd.startswith("req ") or cmd == "req":
        req(cmd.replace("req","").strip())
        return
    
def main():
    while True:
        commandRunner()

if __name__ == "__main__":
    main()