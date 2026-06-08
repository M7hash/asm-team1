import subprocess
import re


def run_nmap(host):

    result = subprocess.run(
        [
            "nmap",
            "-Pn",
            "-T4",
            "-sV",
            host
        ],
        capture_output=True,
        text=True
    )

    return parse_nmap(result.stdout)


def parse_nmap(output):

    ports = []

    pattern = r"(\d+)/tcp\s+(\w+)\s+([\w\-/]+)"

    for line in output.splitlines():

        match = re.match(pattern, line)

        if match:

            ports.append({
                "port": int(match.group(1)),
                "state": match.group(2),
                "service": match.group(3)
            })

    return ports
