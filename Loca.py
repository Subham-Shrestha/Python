# import phonenumbers
# from phonenumbers import geocoder 
# import time, random
# def start_phone_tracer(target):
#     print(f"[+] PhoneTracer v2.1 - OSINT")
#     print(f"[*] Target: {target}")
#     print(f"[*] Initiating trace...")
#     p = phonenumbers.parse(target, None)
#     r = geocoder.description_for_number(p, "en")
#     print(f"[+] Location: {r}")
#     print(f"[+] Trace complete")
# start_phone_tracer("Phone number here") 

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def start_phone_tracer(target):
    print("[+] PhoneTracer v2.1 - OSINT")
    print(f"[*] Target: {target}")
    print("[*] Initiating trace...")

    try:
        p = phonenumbers.parse(target, None)

        country_region = geocoder.description_for_number(p, "en")
        timezones = timezone.time_zones_for_number(p)
        carrier_name = carrier.name_for_number(p, "en")

        print(f"[+] Region/Country: {country_region}")

        if carrier_name:
            print(f"[+] Carrier: {carrier_name}")

        if timezones:
            print(f"[+] Timezone(s): {', '.join(timezones)}")

        # Attempt city extraction (only works for some landlines)
        if "," in country_region:
            city = country_region.split(",")[0].strip()
            print(f"[+] City (best-effort): {city}")
        else:
            print("[+] City: Not available (mobile numbers usually do not expose city)")

        print("[+] Trace complete")

    except Exception as e:
        print(f"[-] Error: {e}")

start_phone_tracer("+number")