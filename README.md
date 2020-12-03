# CS685 Final Project Repo
## Description / Notes
*  This repo contains all of the code written for our final CS 685 project. 
* All trained models and datasets used are hosted in the below drive folder. 
  * Data Folder: https://drive.google.com/drive/folders/10HFYsf_Z9G6k84Cls0kp3squUr9iqfNo?usp=sharing
  * It is not reccomended to download the entire folder at once as it is very large (~100+ gigabytes) and drive often leaves out large binary files unless explicitly zipped with an external tool. Furthermore, many folders will download as seperate zip files cluttering downloads. 

* All of the jupyter notebooks included here were run on either google colab or a Deep learning VM instance on GCP. For most of the notebooks, model checkpoints for the best (based on validation data) and  most recent epoch get saved to drive.


## Files 
* Classifier_train_eval.ipynb
  * Trains binary classifier to distinguish between stylized and normal text for each of the 4 stylizing models (twitter, poetry, lyrics, formality). Evaluates on test dataset that has 5% of outputs randomly replaced with stylized phrases. 
  * Training takes ~5 hours. Evaluation takes ~45 minutes. Times are averages of running on P100 or V100 GPUs 
  * Notes when running
    * Logging for tensorboard isn't working.
    * File paths need to be manually changed for each model being trained / evaluated
* Style_paraphrase.ipynb
  * Praphrases IWSLT14 dataset (188,204 lines) with one of four models. 
    * CDS models take 10 - 15 hours to run while formality / shakespear take 50+ on V100 GPUs hours. 
    *  Ouputted text is saved as a textfile to "IWSLT/2_Style_Paraphrased/". Output length does not always match the input file length and often requires manually adjusting 2-5 lines that have extra crlf .
* watermarking_approach_1.ipynb
    * Implements approach 1 watermarking as described in paper
    * Trains Victim model on original and stylized data. Output from the victim model is used to train an attacker model. Evaluation is performed using BLEU4 scores. 
    * Training time is  ~4 hours per model being trained and ~10 hours total per p value and replacement % combination. 
* watermarking_approach_2.ipynb
    * Implements approach 2 watermarking as described in paper
    * Trains Victim model on original and stylized data. Output from the victim model is used to train an attacker model. Evaluation is performed using BLEU4 scores. 
    * Training time is  ~4 hours per model being trained and ~10 hours total per p value and replacement % combination.  

## Folders
* Preprocessing IWSLT
  * Based on code from fairseq. Updated to allow for arbitrary stylized text to be inserted in place of original en data files. 
  * Prepares data to be tokenized and properly split by the ipynb's.
  * Contains various other files used to help stylized data match original data structure.
* Graphing
  * Python code to generate pyplots based on input csv's. 
  * Requires pandas, pyplot.
  * Output files are not saved but displayed as manual frame adjustments are needed to prevent overlap of axis. 
* drive_download
  * Very small script to allow abitrary drive files to be downloaded to GCP based on file id.
* Latex
  * Scripts to convert csv's to latex tables for use in final report.
