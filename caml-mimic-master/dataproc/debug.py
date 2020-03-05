"""
    Reads NOTEEVENTS file, finds the discharge summaries, preprocesses them and writes out the filtered dataset.
"""
import csv

from nltk.tokenize import RegexpTokenizer

from tqdm import tqdm

from constants import MIMIC_3_DIR

#从原始note中提取4列数据:'SUBJECT_ID', 'HADM_ID', 'CHARTTIME', 'TEXT',去掉不是"Discharge summary"的，全部小写，然后tokenize
#retain only alphanumeric
tokenizer = RegexpTokenizer(r'\w+')

def write_discharge_summaries(out_file):
    notes_file = '%s/NOTEEVENTS.csv' % (MIMIC_3_DIR)
    print("processing notes file")
    with open(notes_file, 'r') as csvfile:
        with open(out_file, 'w', newline='') as outfile:
            print("writing to %s" % (out_file))
            outfile.write(','.join(['SUBJECT_ID', 'HADM_ID', 'CHARTTIME', 'TEXT']) + '\n')
            notereader = csv.reader(csvfile)
            #header
            next(notereader)
            i = 0
            for line in tqdm(notereader):
                subj = int(line[1])
                category = line[6]
                if category == "Discharge summary" and subj==1788:
                    note = line[10]
                    #tokenize, lowercase and remove numerics
                    tokens = [t.lower() for t in tokenizer.tokenize(note) if not t.isnumeric()]
                    text = '"' + ' '.join(tokens) + '"'
                    outfile.write(','.join([line[1], line[2], line[4], text]) + '\n')
                    break
                i += 1
    return out_file

write_discharge_summaries(out_file="%s/bugdetect.csv" % MIMIC_3_DIR)