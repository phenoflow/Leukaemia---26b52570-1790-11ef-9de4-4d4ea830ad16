# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"B67y000","system":"readv2"},{"code":"BBr0113","system":"readv2"},{"code":"BBr2600","system":"readv2"},{"code":"B68y.00","system":"readv2"},{"code":"ByuD900","system":"readv2"},{"code":"BBrAz00","system":"readv2"},{"code":"BBr0111","system":"readv2"},{"code":"BBrA400","system":"readv2"},{"code":"BBrA.00","system":"readv2"},{"code":"B673.00","system":"readv2"},{"code":"B68..00","system":"readv2"},{"code":"B624.12","system":"readv2"},{"code":"C94","system":"readv2"},{"code":"C95","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('leukaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["mmiscellaneous-leukaemia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["mmiscellaneous-leukaemia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["mmiscellaneous-leukaemia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
