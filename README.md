Code for masters thesis titled: "Unsupervised Open Information Extraction with Large Language Models"
By: Amrita H Nair

Welcome !
This folder will help replicate the results reported in the thesis. The steps are as follow: 

Step 1: Install the DeepEx system -> https://github.com/wang-research-lab/deepex/. This will require installation of https://github.com/gabrielStanovsky/supervised-oie as well. 

Step 2: Run the system. An example command would be `python scripts/manager.py --task=OIE_2016 --model="bert-large-cased" --beam-size=6 --max-distance=2048 --batch-size-per-device=4 --stage=0 --cuda=0`

To replicate the results, beam size 6 is required. 

Step 3: Run the linguistic acceptability model in the notebook `BERT_linguistic_acceptability_model.ipynb`. 
The script automatically performs hyper-parameter tuning using WandB. You can use your hyperparameters if you toggle debug. The 'requirements.txt' file contains the libraries used. The CoLA dataset is automatically downloaded. The MegaAcceptability dataset is provided with this folder (data/mega_acceptability.tsv). The dataset has been cleaned and pre-processed. The original dataset can be found at: `http://megaattitude.io/projects/mega-acceptability/`

Step 4: Extract the generated triples from the DeepEx system. For example, the triples for the OIE2016 task would be saved in the folder `deepex/output/output/OIE_2016/bert-large-cased.fast_unsupervised_bidirectional_beam_search.np.score_len.1.mean.sum.1.2048.6/0_BertTokenizerFast_NPMentionGenerator_256_0_0` iff you used the arguments as given in step-2. 

Step 5: Plug in these triples in the `run_models.ipynb` notebook. But first, download unigram probabilities from 
`https://github.com/jhlau/acceptability-prediction-in-context/tree/master/code/unigram-stats`. Plug in both these files to generate evaluation scripts for each acceptability measure. 

Step 6: Use the evaluation script bundled with your chosen benchmark to obtain the F1 and AUC. 


