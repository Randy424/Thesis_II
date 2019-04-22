#!/bin/bash

files=("/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160813v30001.nc"
"/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160824v30001.nc"
"/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160812v30001.nc"
"/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160919v30001.nc"
"/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160815v30001.nc"
"/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160819v30001.nc"
"/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160816v30001.nc"
"/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160817v30001.nc"
"/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160818v30001.nc"
"/Net/samosproc/data/public/research/WTEE/2016/WTEE_20160820v30001.nc")

for i in ${files[*]}; do
    scp rbrunopiverger@login.coaps.fsu.edu:${i} "/Users/randybrunopiverger/Documents/Daily/Thesis II/Thesis_II_Repo/data/spike_data_RH"

done 
exit 0
