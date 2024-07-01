import os
import time

# Get arp table
def retrieve_arp_scan():
    table = os.popen("arp -n").read()
    # Each line is a entry
    entries = table.split("\n")
    # Remove first entry (headers).
    entries.pop(0)

    # Mac dict to detect duplicates.
    hwaddrs = {}
    # Ips dict
    ips = {}
    # Flag of duplicated hw address.
    duplicates = False
    for entry in entries:
        # Skip empty entries and incomplete hardware address.
        if len(entry) == 0 or 'incomplete' in entry:
            continue
        values = entry.split()
        ip = values[0]
        hwaddr = values[2]
        if hwaddr in hwaddrs:
            hwaddrs[hwaddr].append(ip)
            duplicates = True
        else:
            hwaddrs[hwaddr] = [ip]
        ips[ip] = hwaddr
    return (duplicates, ips, hwaddrs)

def compare_arps(prev, curr):
    return prev != curr

print("STARTING ARP SCANNING")
last_scan = None
count = 1
while True:
    print("##################################")
    print("# Scan " + str(count))
    print("##################################")
    count = count + 1

    # Get arp scan.
    arp = retrieve_arp_scan()

    # Check if has duplicates.
    if arp[0]:
        print("!!!!Possible ARP Spoofing!!!!")
        print("Two or more ips with same hw address: ")
        keys = arp[2].keys()
        for hwaddr in keys:
            if len(arp[2][hwaddr]) > 1:
                print("\t" + hwaddr + ": " + ", ".join(arp[2][hwaddr]))
    else:
        print("Without duplicated hw address.")



    if last_scan is None:
        # Skip comparation
        last_scan = arp[1]
        time.sleep(10)
        continue

    # Compare
    is_changed = compare_arps(last_scan, arp[1])

    if is_changed:
        print("!!!!Detected ARP Table Change!!!!")
    else:
        print("ARP Table unchanged.")
    last_scan = arp[1]
    time.sleep(10)