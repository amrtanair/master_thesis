#!/usr/bin/python
# -*- coding: utf-8 -*-
from allennlp_models.pretrained import load_predictor
srl_predictor = load_predictor('structured-prediction-srl-bert')
from tqdm import tqdm
import json


def collect_context(lst, target_label='B-V'):
    include_list = [
        'B-ARG0',
        'B-ARG1',
        'B-ARG2',
        'I-ARG0',
        'I-ARG1',
        'I-ARG2',
        ]
    args = []
    index = next((i for (i, (label, _)) in enumerate(lst) if label
                 == target_label), None)
    if index is not None:
        left_context = [(label, word) for (label, word) in
                        reversed(lst[:index]) if label not in 'O']
        right_context = [(label, word) for (label, word) in lst[index
                         + 1:] if label not in 'O']
        context = [left_context[::-1], right_context]

        args = [' '.join([word for (label, word) in c]) for c in
                context]
        args.append(lst[index][1])

        if args[0] == '' or args[1] == '':
            return None
        return args
    return None


def generate_srl_results_for_oie(file_path, dataset):
    result = {}
    ID = 1
    with open(file_path, 'r') as file:
        test_file = file.readlines()
    for line in tqdm(test_file):
        line = line.strip('\n')

        strID = '0' * (40 - len(str(ID))) + str(ID)
        ID = ID + 1
        result[strID] = [line]

        srl_result = srl_predictor.predict(line)
        for pairs in srl_result['verbs']:
            _ = list(zip(pairs['tags'], srl_result['words']))
            context = collect_context(_)
            if context is not None:
                result[strID].append(context)
    return (result, )


if __name__ == '__main__':

        # file_path = './datasets/OIE2016/supervised-oie/supervised-oie-benchmark/raw_sentences/test.txt'
        # file_path = './datasets/CaRB/data/test.txt'

    file_path = \
        './datasets/NYT/supervised-oie/external_datasets/mesquita_2013/processed/nyt.raw'
    dataset = 'NYT'
    print ('The dataset being used is: ', dataset)
    result = generate_srl_results_for_oie(file_path, dataset)
    result_file = dataset + '_srl_aware_oie_test.json'

    with open(result_file, 'w') as json_file:
        json.dump(result, json_file, indent=2)
    print ('Result dumped at: ', result_file)

