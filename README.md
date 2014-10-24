CondorMGGen
===========

Colleciton of scripts to generate MG events using condor slots

# Summary
This repo contains the basic ingrendients to perform MG generation
using our cluster setup at T3_US_MIT.
You will need to edit some of the files to be able to generate the desidered
events in a proper way. 
Core files

1. `runjobs.sh`
⋅⋅* the main executable. this is what is being executed by the condor job. 
2. `run_card_template.dat`
⋅⋅* this is the madgraph run card, where run setup are decided. tweak the file to change the number of generated events, turning on/off the matching, apply gen level cuts, ecc... 
3. `proc_card_mg5_template.dat`
⋅⋅* this is the madgraph process card, where the kind of process that are being generated are specified.
4. `param_card_template.dat`
⋅⋅* this is the madgraph parameter card, where the model parameters can be changed. tweak the file to set different interference scenarios, vary the DM candidate mass, ecc...
