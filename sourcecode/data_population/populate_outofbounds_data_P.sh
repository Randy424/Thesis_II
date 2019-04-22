#!/bin/bash

files=("/Net/samosproc/data/public/research/KAQP/2012/KAQP_20120324v30001.nc"
"/Net/samosproc/data/public/research/WTDO/2017/WTDO_20170501v30001.nc"
"/Net/samosproc/data/public/research/WTDO/2017/WTDO_20170502v30001.nc"
"/Net/samosproc/data/public/research/WTEU/2011/WTEU_20110726v30001.nc"
"/Net/samosproc/data/public/research/WTEU/2010/WTEU_20100429v30001.nc"
"/Net/samosproc/data/public/research/WTEU/2010/WTEU_20100701v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2010/WTDL_20100310v30001.nc"
"/Net/samosproc/data/public/research/WCX7445/2009/WCX7445_20090208v30001.nc"
"/Net/samosproc/data/public/research/WCX7445/2011/WCX7445_20110412v30001.nc")


for i in ${files[*]}; do
    scp rbrunopiverger@login.coaps.fsu.edu:${i} "/Users/randybrunopiverger/Documents/Daily/Thesis II/Thesis_II_Repo/data/outofbounds_data" 

done 
exit 0
