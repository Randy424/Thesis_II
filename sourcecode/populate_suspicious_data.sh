#!/bin/bash

files=("/Net/samosproc/data/public/research/WTDL/2013/WTDL_20130428v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2013/WTDL_20130730v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2014/WTDL_20140619v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2010/WTDL_20101105v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2010/WTDL_20100222v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2017/WTDL_20170628v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2017/WTDL_20170704v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2017/WTDL_20170808v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2017/WTDL_20171012v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2015/WTDL_20151112v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2011/WTDL_20110706v30001.nc")


for i in ${files[*]}; do
    scp rbrunopiverger@login.coaps.fsu.edu:${i} "/Users/randybrunopiverger/Documents/Daily/Thesis II/Thesis_II_Repo/data/suspicious_data" 

done 
exit 0
