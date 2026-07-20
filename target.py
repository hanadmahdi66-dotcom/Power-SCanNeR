import os
import subprocess
from datetime import datetime

BANNER = r"""
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗
██║  ██║██╔══██╗████╗  ██║██╔═══██╗██╔════╝
███████║███████║██╔██╗ ██║██║   ██║███████╗
██╔══██║██╔══██║██║╚██╗██║██║   ██║╚════██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

        POWER SCANNER - V1.0
        Author : hanad
        Codename : hanDeep
"""


def shot(ip):
    # Isticmaal folder-ka RECOND (wuu abuuraa haddii uusan jirin)
    log_dir = "RECOND"
    os.makedirs(log_dir, exist_ok=True)

    # Magaca faylasha - ku daray taariikh/waqti si aysan isu qarin marka dib scan la sameeyo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    normal_log = os.path.join(log_dir, f"{ip}_{timestamp}.txt")
    xml_log = os.path.join(log_dir, f"{ip}_{timestamp}.xml")
    dirb_log = os.path.join(log_dir, f"{ip}_{timestamp}_dirb.txt")

    print(f"[*] Scanning {ip} ... fadlan sug.")

    # -oN = normal output (akhris-fudud), -oX = XML output (loo isticmaali karo tools kale)
    nmap_cmd = [
        "nmap", "-A", "-p-", "-Pn", "-v",
        ip,
        "-oN", normal_log,
        "-oX", xml_log
    ]
    result = subprocess.run(nmap_cmd, capture_output=True, text=True)

    # Muuji natiijada shaashadda
    print(result.stdout)
    if result.stderr:
        print("[!] Error/Warning:", result.stderr)

    print(f"[+] Normal log waxaa lagu keydiyay: {normal_log}")
    print(f"[+] XML log waxaa lagu keydiyay: {xml_log}")

    # dirb - directory/file brute-forcing on the target (fadlan hubi in dirb la install gareeyay: apt install dirb)
    print(f"[*] Running dirb on {ip} ... fadlan sug.")
    dirb_cmd = ["dirb", f"http://{ip}", "-o", dirb_log]
    dirb_result = subprocess.run(dirb_cmd, capture_output=True, text=True)

    print(dirb_result.stdout)
    if dirb_result.stderr:
        print("[!] Dirb Error/Warning:", dirb_result.stderr)

    print(f"[+] Dirb log waxaa lagu keydiyay: {dirb_log}")


if __name__ == "__main__":
    print(BANNER)
    target = input("Enter Target To Scan: ").strip()
    shot(target)
