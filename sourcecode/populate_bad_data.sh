#!/bin/bash

files=("/Net/samosproc/data/public/research/WTDF/2009/WTDF_20090318v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2016/ZCYL5_20160525v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2016/ZCYL5_20160628v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2016/ZCYL5_20160704v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2016/ZCYL5_20160829v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2016/ZCYL5_20160703v30001.nc"
"/Net/samosproc/data/public/research/ZCYL5/2016/ZCYL5_20160522v30001.nc"
"/Net/samosproc/data/public/research/KAQP/2011/KAQP_20110612v30101.nc"
"/Net/samosproc/data/public/research/KAQP/2010/KAQP_20101014v30001.nc"
"/Net/samosproc/data/public/research/WCX7445/2011/WCX7445_20110831v30001.nc"
"/Net/samosproc/data/public/research/WCX7445/2010/WCX7445_20100409v30001.nc")


for i in ${files[*]}; do
    scp rbrunopiverger@login.coaps.fsu.edu:${i} "/Users/randybrunopiverger/Documents/Daily/Thesis II/Thesis_II_Repo/bad_data" 

done 
exit 0
