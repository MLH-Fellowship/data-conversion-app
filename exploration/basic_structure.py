xml_data = {
    "ENABLE DOPPLER": "NO",
    "ENABLE MULTIPATH": "NO"
}


with open("ascii_data.sig", "wt") as f:
    f.write(f"""
    //******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     {xml_data["ENABLE DOPPLER"]}
ENABLE MULTIPATH:   {xml_data["ENABLE MULTIPATH"]}
""")