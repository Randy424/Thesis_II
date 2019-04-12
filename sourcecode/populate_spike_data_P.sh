#!/bin/bash

files=("/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150817v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150807v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150619v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150616v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150620v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150816v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150806v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150812v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150623v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2015/ZCYL5_20150813v30001.nc")

for i in ${files[*]}; do
    scp rbrunopiverger@login.coaps.fsu.edu:${i} "/Users/randybrunopiverger/Documents/Daily/Thesis II/Thesis_II_Repo/data/spike_data"

done 
exit 0
